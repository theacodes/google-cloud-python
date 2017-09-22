# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import grpc
import mock
import pytest

from google.api.core import exceptions
from google.api.core.helpers import grpc_helpers


def test__patch_callable_name():
    callable = mock.Mock(spec=['__class__'])
    callable.__class__ = mock.Mock(spec=['__name__'])
    callable.__class__.__name__ = 'TestCallable'

    grpc_helpers._patch_callable_name(callable)

    assert callable.__name__ == 'TestCallable'


def test__patch_callable_name_no_op():
    callable = mock.Mock(spec=['__name__'])
    callable.__name__ = 'test_callable'

    grpc_helpers._patch_callable_name(callable)

    assert callable.__name__ == 'test_callable'


class RpcErrorImpl(grpc.RpcError, grpc.Call):
    def __init__(self, code):
        super(RpcErrorImpl, self).__init__()
        self._code = code

    def code(self):
        return self._code

    def details(self):
        return None


def test_wrap_unary_errors():
    grpc_error = RpcErrorImpl(grpc.StatusCode.INVALID_ARGUMENT)
    callable = mock.Mock(spec=['__call__'], side_effect=grpc_error)

    wrapped_callable = grpc_helpers._wrap_unary_errors(callable)

    with pytest.raises(exceptions.InvalidArgument) as exc_info:
        wrapped_callable(1, 2, three='four')

    callable.assert_called_once_with(1, 2, three='four')
    assert exc_info.value.response == grpc_error


def test_wrap_stream_errors_invocation():
    grpc_error = RpcErrorImpl(grpc.StatusCode.INVALID_ARGUMENT)
    callable = mock.Mock(spec=['__call__'], side_effect=grpc_error)

    wrapped_callable = grpc_helpers._wrap_stream_errors(callable)

    with pytest.raises(exceptions.InvalidArgument) as exc_info:
        wrapped_callable(1, 2, three='four')

    callable.assert_called_once_with(1, 2, three='four')
    assert exc_info.value.response == grpc_error


class RpcResponseIteratorImpl(object):
    def __init__(self, exception):
        self._exception = exception

    # Note: This matches grpc._channel._Rendezvous._next which is what is
    # patched by _wrap_stream_errors.
    def _next(self):
        raise self._exception

    def __next__(self):  # pragma: NO COVER
        return self._next()

    def next(self):  # pragma: NO COVER
        return self._next()


def test_wrap_stream_errors_iterator():
    grpc_error = RpcErrorImpl(grpc.StatusCode.UNAVAILABLE)
    response_iter = RpcResponseIteratorImpl(grpc_error)
    callable = mock.Mock(spec=['__call__'], return_value=response_iter)

    wrapped_callable = grpc_helpers._wrap_stream_errors(callable)

    got_iterator = wrapped_callable(1, 2, three='four')

    with pytest.raises(exceptions.ServiceUnavailable) as exc_info:
        next(got_iterator)

    assert got_iterator == response_iter
    callable.assert_called_once_with(1, 2, three='four')
    assert exc_info.value.response == grpc_error


@mock.patch('google.api.core.helpers.grpc_helpers._wrap_unary_errors')
def test_wrap_errors_non_streaming(wrap_unary_errors):
    callable = mock.create_autospec(grpc.UnaryUnaryMultiCallable)

    result = grpc_helpers.wrap_errors(callable)

    assert result == wrap_unary_errors.return_value
    wrap_unary_errors.assert_called_once_with(callable)


@mock.patch('google.api.core.helpers.grpc_helpers._wrap_stream_errors')
def test_wrap_errors_streaming(wrap_stream_errors):
    callable = mock.create_autospec(grpc.UnaryStreamMultiCallable)

    result = grpc_helpers.wrap_errors(callable)

    assert result == wrap_stream_errors.return_value
    wrap_stream_errors.assert_called_once_with(callable)