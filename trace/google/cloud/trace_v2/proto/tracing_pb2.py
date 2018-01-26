# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/cloudtrace_v2/proto/tracing.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.devtools.cloudtrace_v2.proto import trace_pb2 as google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/cloudtrace_v2/proto/tracing.proto',
  package='google.devtools.cloudtrace.v2',
  syntax='proto3',
  serialized_pb=_b('\n1google/devtools/cloudtrace_v2/proto/tracing.proto\x12\x1dgoogle.devtools.cloudtrace.v2\x1a\x1cgoogle/api/annotations.proto\x1a/google/devtools/cloudtrace_v2/proto/trace.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"Z\n\x16\x42\x61tchWriteSpansRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x05spans\x18\x02 \x03(\x0b\x32#.google.devtools.cloudtrace.v2.Span2\xaf\x02\n\x0cTraceService\x12\x94\x01\n\x0f\x42\x61tchWriteSpans\x12\x35.google.devtools.cloudtrace.v2.BatchWriteSpansRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,\"\'/v2/{name=projects/*}/traces:batchWrite:\x01*\x12\x87\x01\n\nCreateSpan\x12#.google.devtools.cloudtrace.v2.Span\x1a#.google.devtools.cloudtrace.v2.Span\"/\x82\xd3\xe4\x93\x02)\"$/v2/{name=projects/*/traces/*}/spans:\x01*B\xac\x01\n!com.google.devtools.cloudtrace.v2B\x0cTracingProtoP\x01ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v2;cloudtrace\xaa\x02\x15Google.Cloud.Trace.V2\xca\x02\x15Google\\Cloud\\Trace\\V2b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATCHWRITESPANSREQUEST = _descriptor.Descriptor(
  name='BatchWriteSpansRequest',
  full_name='google.devtools.cloudtrace.v2.BatchWriteSpansRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.cloudtrace.v2.BatchWriteSpansRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spans', full_name='google.devtools.cloudtrace.v2.BatchWriteSpansRequest.spans', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=315,
)

_BATCHWRITESPANSREQUEST.fields_by_name['spans'].message_type = google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2._SPAN
DESCRIPTOR.message_types_by_name['BatchWriteSpansRequest'] = _BATCHWRITESPANSREQUEST

BatchWriteSpansRequest = _reflection.GeneratedProtocolMessageType('BatchWriteSpansRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHWRITESPANSREQUEST,
  __module__ = 'google.devtools.cloudtrace_v2.proto.tracing_pb2'
  ,
  __doc__ = """The request message for the ``BatchWriteSpans`` method.
  
  
  Attributes:
      name:
          Required. The name of the project where the spans belong. The
          format is ``projects/[PROJECT_ID]``.
      spans:
          A list of new spans. The span names must not match existing
          spans, or the results are undefined.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v2.BatchWriteSpansRequest)
  ))
_sym_db.RegisterMessage(BatchWriteSpansRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.devtools.cloudtrace.v2B\014TracingProtoP\001ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v2;cloudtrace\252\002\025Google.Cloud.Trace.V2\312\002\025Google\\Cloud\\Trace\\V2'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class TraceServiceStub(object):
    """This file describes an API for collecting and viewing traces and spans
    within a trace.  A Trace is a collection of spans corresponding to a single
    operation or set of operations for an application. A span is an individual
    timed event which forms a node of the trace tree. A single trace may
    contain span(s) from multiple services.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.BatchWriteSpans = channel.unary_unary(
          '/google.devtools.cloudtrace.v2.TraceService/BatchWriteSpans',
          request_serializer=BatchWriteSpansRequest.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          )
      self.CreateSpan = channel.unary_unary(
          '/google.devtools.cloudtrace.v2.TraceService/CreateSpan',
          request_serializer=google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.Span.SerializeToString,
          response_deserializer=google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.Span.FromString,
          )


  class TraceServiceServicer(object):
    """This file describes an API for collecting and viewing traces and spans
    within a trace.  A Trace is a collection of spans corresponding to a single
    operation or set of operations for an application. A span is an individual
    timed event which forms a node of the trace tree. A single trace may
    contain span(s) from multiple services.
    """

    def BatchWriteSpans(self, request, context):
      """Sends new spans to new or existing traces. You cannot update
      existing spans.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def CreateSpan(self, request, context):
      """Creates a new span.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TraceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'BatchWriteSpans': grpc.unary_unary_rpc_method_handler(
            servicer.BatchWriteSpans,
            request_deserializer=BatchWriteSpansRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        'CreateSpan': grpc.unary_unary_rpc_method_handler(
            servicer.CreateSpan,
            request_deserializer=google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.Span.FromString,
            response_serializer=google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.Span.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'google.devtools.cloudtrace.v2.TraceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTraceServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """This file describes an API for collecting and viewing traces and spans
    within a trace.  A Trace is a collection of spans corresponding to a single
    operation or set of operations for an application. A span is an individual
    timed event which forms a node of the trace tree. A single trace may
    contain span(s) from multiple services.
    """
    def BatchWriteSpans(self, request, context):
      """Sends new spans to new or existing traces. You cannot update
      existing spans.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def CreateSpan(self, request, context):
      """Creates a new span.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTraceServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """This file describes an API for collecting and viewing traces and spans
    within a trace.  A Trace is a collection of spans corresponding to a single
    operation or set of operations for an application. A span is an individual
    timed event which forms a node of the trace tree. A single trace may
    contain span(s) from multiple services.
    """
    def BatchWriteSpans(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Sends new spans to new or existing traces. You cannot update
      existing spans.
      """
      raise NotImplementedError()
    BatchWriteSpans.future = None
    def CreateSpan(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Creates a new span.
      """
      raise NotImplementedError()
    CreateSpan.future = None


  def beta_create_TraceService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('google.devtools.cloudtrace.v2.TraceService', 'BatchWriteSpans'): BatchWriteSpansRequest.FromString,
      ('google.devtools.cloudtrace.v2.TraceService', 'CreateSpan'): google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.Span.FromString,
    }
    response_serializers = {
      ('google.devtools.cloudtrace.v2.TraceService', 'BatchWriteSpans'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('google.devtools.cloudtrace.v2.TraceService', 'CreateSpan'): google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.Span.SerializeToString,
    }
    method_implementations = {
      ('google.devtools.cloudtrace.v2.TraceService', 'BatchWriteSpans'): face_utilities.unary_unary_inline(servicer.BatchWriteSpans),
      ('google.devtools.cloudtrace.v2.TraceService', 'CreateSpan'): face_utilities.unary_unary_inline(servicer.CreateSpan),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_TraceService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('google.devtools.cloudtrace.v2.TraceService', 'BatchWriteSpans'): BatchWriteSpansRequest.SerializeToString,
      ('google.devtools.cloudtrace.v2.TraceService', 'CreateSpan'): google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.Span.SerializeToString,
    }
    response_deserializers = {
      ('google.devtools.cloudtrace.v2.TraceService', 'BatchWriteSpans'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('google.devtools.cloudtrace.v2.TraceService', 'CreateSpan'): google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.Span.FromString,
    }
    cardinalities = {
      'BatchWriteSpans': cardinality.Cardinality.UNARY_UNARY,
      'CreateSpan': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'google.devtools.cloudtrace.v2.TraceService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
