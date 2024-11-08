# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in booking_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllBookings = channel.unary_stream(
            '/Booking/GetAllBookings',
            request_serializer=booking__pb2.EmptyBooking.SerializeToString,
            response_deserializer=booking__pb2.BookingData.FromString,
            _registered_method=True)
        self.GetUsersBookings = channel.unary_unary(
            '/Booking/GetUsersBookings',
            request_serializer=booking__pb2.UserId.SerializeToString,
            response_deserializer=booking__pb2.BookingData.FromString,
            _registered_method=True)
        self.GetShowtimesBookings = channel.unary_stream(
            '/Booking/GetShowtimesBookings',
            request_serializer=booking__pb2.Showtime.SerializeToString,
            response_deserializer=booking__pb2.BookingData.FromString,
            _registered_method=True)
        self.AddBooking = channel.unary_unary(
            '/Booking/AddBooking',
            request_serializer=booking__pb2.AddBookingData.SerializeToString,
            response_deserializer=booking__pb2.AddBookingResponse.FromString,
            _registered_method=True)
        self.DeleteBooking = channel.unary_unary(
            '/Booking/DeleteBooking',
            request_serializer=booking__pb2.DeleteBookingData.SerializeToString,
            response_deserializer=booking__pb2.DeleteBookingResponse.FromString,
            _registered_method=True)


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShowtimesBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAllBookings': grpc.unary_stream_rpc_method_handler(
            servicer.GetAllBookings,
            request_deserializer=booking__pb2.EmptyBooking.FromString,
            response_serializer=booking__pb2.BookingData.SerializeToString,
        ),
        'GetUsersBookings': grpc.unary_unary_rpc_method_handler(
            servicer.GetUsersBookings,
            request_deserializer=booking__pb2.UserId.FromString,
            response_serializer=booking__pb2.BookingData.SerializeToString,
        ),
        'GetShowtimesBookings': grpc.unary_stream_rpc_method_handler(
            servicer.GetShowtimesBookings,
            request_deserializer=booking__pb2.Showtime.FromString,
            response_serializer=booking__pb2.BookingData.SerializeToString,
        ),
        'AddBooking': grpc.unary_unary_rpc_method_handler(
            servicer.AddBooking,
            request_deserializer=booking__pb2.AddBookingData.FromString,
            response_serializer=booking__pb2.AddBookingResponse.SerializeToString,
        ),
        'DeleteBooking': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBooking,
            request_deserializer=booking__pb2.DeleteBookingData.FromString,
            response_serializer=booking__pb2.DeleteBookingResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Booking', rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllBookings(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/Booking/GetAllBookings',
            booking__pb2.EmptyBooking.SerializeToString,
            booking__pb2.BookingData.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUsersBookings(request,
                         target,
                         options=(),
                         channel_credentials=None,
                         call_credentials=None,
                         insecure=False,
                         compression=None,
                         wait_for_ready=None,
                         timeout=None,
                         metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Booking/GetUsersBookings',
            booking__pb2.UserId.SerializeToString,
            booking__pb2.BookingData.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetShowtimesBookings(request,
                             target,
                             options=(),
                             channel_credentials=None,
                             call_credentials=None,
                             insecure=False,
                             compression=None,
                             wait_for_ready=None,
                             timeout=None,
                             metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/Booking/GetShowtimesBookings',
            booking__pb2.Showtime.SerializeToString,
            booking__pb2.BookingData.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddBooking(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Booking/AddBooking',
            booking__pb2.AddBookingData.SerializeToString,
            booking__pb2.AddBookingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteBooking(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Booking/DeleteBooking',
            booking__pb2.DeleteBookingData.SerializeToString,
            booking__pb2.DeleteBookingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)