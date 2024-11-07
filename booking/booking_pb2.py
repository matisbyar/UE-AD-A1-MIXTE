# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: booking.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'booking.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rbooking.proto\"7\n\x0b\x42ookingData\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x18\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\t.DateData\"2\n\x08\x44\x61teData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x18\n\x06movies\x18\x02 \x03(\x0b\x32\x08.MovieId\"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\t\"\x15\n\x07MovieId\x12\n\n\x02id\x18\x01 \x01(\t\"\'\n\x08Showtime\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05movie\x18\x02 \x01(\t\";\n\x0e\x41\x64\x64\x42ookingData\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\r\n\x05movie\x18\x03 \x01(\t\">\n\x11\x44\x65leteBookingData\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\r\n\x05movie\x18\x03 \x01(\t\"1\n\x12\x41\x64\x64\x42ookingResponse\x12\x1b\n\x08response\x18\x01 \x01(\x0b\x32\t.Response\"4\n\x15\x44\x65leteBookingResponse\x12\x1b\n\x08response\x18\x01 \x01(\x0b\x32\t.Response\",\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\x82\x02\n\x07\x42ooking\x12(\n\x0eGetAllBookings\x12\x06.Empty\x1a\x0c.BookingData0\x01\x12)\n\x10GetUsersBookings\x12\x07.UserId\x1a\x0c.BookingData\x12\x31\n\x14GetShowtimesBookings\x12\t.Showtime\x1a\x0c.BookingData0\x01\x12\x32\n\nAddBooking\x12\x0f.AddBookingData\x1a\x13.AddBookingResponse\x12;\n\rDeleteBooking\x12\x12.DeleteBookingData\x1a\x16.DeleteBookingResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_BOOKINGDATA']._serialized_start = 17
    _globals['_BOOKINGDATA']._serialized_end = 72
    _globals['_DATEDATA']._serialized_start = 74
    _globals['_DATEDATA']._serialized_end = 124
    _globals['_USERID']._serialized_start = 126
    _globals['_USERID']._serialized_end = 146
    _globals['_MOVIEID']._serialized_start = 148
    _globals['_MOVIEID']._serialized_end = 169
    _globals['_SHOWTIME']._serialized_start = 171
    _globals['_SHOWTIME']._serialized_end = 210
    _globals['_ADDBOOKINGDATA']._serialized_start = 212
    _globals['_ADDBOOKINGDATA']._serialized_end = 271
    _globals['_DELETEBOOKINGDATA']._serialized_start = 273
    _globals['_DELETEBOOKINGDATA']._serialized_end = 335
    _globals['_ADDBOOKINGRESPONSE']._serialized_start = 337
    _globals['_ADDBOOKINGRESPONSE']._serialized_end = 386
    _globals['_DELETEBOOKINGRESPONSE']._serialized_start = 388
    _globals['_DELETEBOOKINGRESPONSE']._serialized_end = 440
    _globals['_RESPONSE']._serialized_start = 442
    _globals['_RESPONSE']._serialized_end = 486
    _globals['_EMPTY']._serialized_start = 488
    _globals['_EMPTY']._serialized_end = 495
    _globals['_BOOKING']._serialized_start = 498
    _globals['_BOOKING']._serialized_end = 756
# @@protoc_insertion_point(module_scope)
