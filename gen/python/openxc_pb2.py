# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openxc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='openxc.proto',
  package='openxc',
  serialized_pb=_b('\n\x0copenxc.proto\x12\x06openxc\"\x88\x03\n\x0eVehicleMessage\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.openxc.VehicleMessage.Type\x12\'\n\x0b\x63\x61n_message\x18\x02 \x01(\x0b\x32\x12.openxc.CanMessage\x12-\n\x0esimple_message\x18\x03 \x01(\x0b\x32\x15.openxc.SimpleMessage\x12\x37\n\x13\x64iagnostic_response\x18\x04 \x01(\x0b\x32\x1a.openxc.DiagnosticResponse\x12/\n\x0f\x63ontrol_command\x18\x05 \x01(\x0b\x32\x16.openxc.ControlCommand\x12\x31\n\x10\x63ommand_response\x18\x06 \x01(\x0b\x32\x17.openxc.CommandResponse\"V\n\x04Type\x12\x07\n\x03\x43\x41N\x10\x01\x12\n\n\x06SIMPLE\x10\x02\x12\x0e\n\nDIAGNOSTIC\x10\x03\x12\x13\n\x0f\x43ONTROL_COMMAND\x10\x04\x12\x14\n\x10\x43OMMAND_RESPONSE\x10\x05\"\x94\x01\n\nCanMessage\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x34\n\x0c\x66rame_format\x18\x04 \x01(\x0e\x32\x1e.openxc.CanMessage.FrameFormat\")\n\x0b\x46rameFormat\x12\x0c\n\x08STANDARD\x10\x01\x12\x0c\n\x08\x45XTENDED\x10\x02\"\xb8\x04\n\x0e\x43ontrolCommand\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.openxc.ControlCommand.Type\x12<\n\x12\x64iagnostic_request\x18\x02 \x01(\x0b\x32 .openxc.DiagnosticControlCommand\x12G\n\x18passthrough_mode_request\x18\x03 \x01(\x0b\x32%.openxc.PassthroughModeControlCommand\x12O\n acceptance_filter_bypass_command\x18\x04 \x01(\x0b\x32%.openxc.AcceptanceFilterBypassCommand\x12<\n\x16payload_format_command\x18\x05 \x01(\x0b\x32\x1c.openxc.PayloadFormatCommand\x12O\n predefined_obd2_requests_command\x18\x06 \x01(\x0b\x32%.openxc.PredefinedObd2RequestsCommand\"\x93\x01\n\x04Type\x12\x0b\n\x07VERSION\x10\x01\x12\r\n\tDEVICE_ID\x10\x02\x12\x0e\n\nDIAGNOSTIC\x10\x03\x12\x0f\n\x0bPASSTHROUGH\x10\x04\x12\x1c\n\x18\x41\x43\x43\x45PTANCE_FILTER_BYPASS\x10\x05\x12\x12\n\x0ePAYLOAD_FORMAT\x10\x06\x12\x1c\n\x18PREDEFINED_OBD2_REQUESTS\x10\x07\"\x9e\x01\n\x18\x44iagnosticControlCommand\x12*\n\x07request\x18\x01 \x01(\x0b\x32\x19.openxc.DiagnosticRequest\x12\x37\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\'.openxc.DiagnosticControlCommand.Action\"\x1d\n\x06\x41\x63tion\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06\x43\x41NCEL\x10\x02\"=\n\x1dPassthroughModeControlCommand\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"<\n\x1d\x41\x63\x63\x65ptanceFilterBypassCommand\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x0e\n\x06\x62ypass\x18\x02 \x01(\x08\"{\n\x14PayloadFormatCommand\x12:\n\x06\x66ormat\x18\x01 \x01(\x0e\x32*.openxc.PayloadFormatCommand.PayloadFormat\"\'\n\rPayloadFormat\x12\x08\n\x04JSON\x10\x01\x12\x0c\n\x08PROTOBUF\x10\x02\"0\n\x1dPredefinedObd2RequestsCommand\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"]\n\x0f\x43ommandResponse\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.openxc.ControlCommand.Type\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x08\"\xfd\x01\n\x11\x44iagnosticRequest\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x0c\n\x04mode\x18\x03 \x01(\r\x12\x0b\n\x03pid\x18\x04 \x01(\r\x12\x0f\n\x07payload\x18\x05 \x01(\x0c\x12\x1a\n\x12multiple_responses\x18\x06 \x01(\x08\x12\x11\n\tfrequency\x18\x07 \x01(\x01\x12\x0c\n\x04name\x18\x08 \x01(\t\x12;\n\x0c\x64\x65\x63oded_type\x18\t \x01(\x0e\x32%.openxc.DiagnosticRequest.DecodedType\"!\n\x0b\x44\x65\x63odedType\x12\x08\n\x04NONE\x10\x01\x12\x08\n\x04OBD2\x10\x02\"\xa1\x01\n\x12\x44iagnosticResponse\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x0c\n\x04mode\x18\x03 \x01(\r\x12\x0b\n\x03pid\x18\x04 \x01(\r\x12\x0f\n\x07success\x18\x05 \x01(\x08\x12\x1e\n\x16negative_response_code\x18\x06 \x01(\r\x12\x0f\n\x07payload\x18\x07 \x01(\x0c\x12\r\n\x05value\x18\x08 \x01(\x01\"\xa2\x01\n\x0c\x44ynamicField\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.openxc.DynamicField.Type\x12\x14\n\x0cstring_value\x18\x02 \x01(\t\x12\x15\n\rnumeric_value\x18\x03 \x01(\x01\x12\x15\n\rboolean_value\x18\x04 \x01(\x08\"%\n\x04Type\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03NUM\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\"g\n\rSimpleMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.openxc.DynamicField\x12#\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x14.openxc.DynamicFieldB\x1c\n\ncom.openxcB\x0e\x42inaryMessages')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_VEHICLEMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.VehicleMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CAN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIAGNOSTIC', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_COMMAND', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_RESPONSE', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=331,
  serialized_end=417,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEMESSAGE_TYPE)

_CANMESSAGE_FRAMEFORMAT = _descriptor.EnumDescriptor(
  name='FrameFormat',
  full_name='openxc.CanMessage.FrameFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STANDARD', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTENDED', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=527,
  serialized_end=568,
)
_sym_db.RegisterEnumDescriptor(_CANMESSAGE_FRAMEFORMAT)

_CONTROLCOMMAND_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.ControlCommand.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERSION', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_ID', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIAGNOSTIC', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSTHROUGH', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCEPTANCE_FILTER_BYPASS', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYLOAD_FORMAT', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREDEFINED_OBD2_REQUESTS', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=992,
  serialized_end=1139,
)
_sym_db.RegisterEnumDescriptor(_CONTROLCOMMAND_TYPE)

_DIAGNOSTICCONTROLCOMMAND_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='openxc.DiagnosticControlCommand.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1271,
  serialized_end=1300,
)
_sym_db.RegisterEnumDescriptor(_DIAGNOSTICCONTROLCOMMAND_ACTION)

_PAYLOADFORMATCOMMAND_PAYLOADFORMAT = _descriptor.EnumDescriptor(
  name='PayloadFormat',
  full_name='openxc.PayloadFormatCommand.PayloadFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JSON', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTOBUF', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1511,
  serialized_end=1550,
)
_sym_db.RegisterEnumDescriptor(_PAYLOADFORMATCOMMAND_PAYLOADFORMAT)

_DIAGNOSTICREQUEST_DECODEDTYPE = _descriptor.EnumDescriptor(
  name='DecodedType',
  full_name='openxc.DiagnosticRequest.DecodedType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OBD2', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1918,
  serialized_end=1951,
)
_sym_db.RegisterEnumDescriptor(_DIAGNOSTICREQUEST_DECODEDTYPE)

_DYNAMICFIELD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.DynamicField.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUM', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2243,
  serialized_end=2280,
)
_sym_db.RegisterEnumDescriptor(_DYNAMICFIELD_TYPE)


_VEHICLEMESSAGE = _descriptor.Descriptor(
  name='VehicleMessage',
  full_name='openxc.VehicleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.VehicleMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='can_message', full_name='openxc.VehicleMessage.can_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simple_message', full_name='openxc.VehicleMessage.simple_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diagnostic_response', full_name='openxc.VehicleMessage.diagnostic_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control_command', full_name='openxc.VehicleMessage.control_command', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command_response', full_name='openxc.VehicleMessage.command_response', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VEHICLEMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=417,
)


_CANMESSAGE = _descriptor.Descriptor(
  name='CanMessage',
  full_name='openxc.CanMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.CanMessage.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='openxc.CanMessage.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='openxc.CanMessage.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frame_format', full_name='openxc.CanMessage.frame_format', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CANMESSAGE_FRAMEFORMAT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=568,
)


_CONTROLCOMMAND = _descriptor.Descriptor(
  name='ControlCommand',
  full_name='openxc.ControlCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.ControlCommand.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diagnostic_request', full_name='openxc.ControlCommand.diagnostic_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passthrough_mode_request', full_name='openxc.ControlCommand.passthrough_mode_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acceptance_filter_bypass_command', full_name='openxc.ControlCommand.acceptance_filter_bypass_command', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_format_command', full_name='openxc.ControlCommand.payload_format_command', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predefined_obd2_requests_command', full_name='openxc.ControlCommand.predefined_obd2_requests_command', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTROLCOMMAND_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=571,
  serialized_end=1139,
)


_DIAGNOSTICCONTROLCOMMAND = _descriptor.Descriptor(
  name='DiagnosticControlCommand',
  full_name='openxc.DiagnosticControlCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='openxc.DiagnosticControlCommand.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='openxc.DiagnosticControlCommand.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DIAGNOSTICCONTROLCOMMAND_ACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1142,
  serialized_end=1300,
)


_PASSTHROUGHMODECONTROLCOMMAND = _descriptor.Descriptor(
  name='PassthroughModeControlCommand',
  full_name='openxc.PassthroughModeControlCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.PassthroughModeControlCommand.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='openxc.PassthroughModeControlCommand.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1302,
  serialized_end=1363,
)


_ACCEPTANCEFILTERBYPASSCOMMAND = _descriptor.Descriptor(
  name='AcceptanceFilterBypassCommand',
  full_name='openxc.AcceptanceFilterBypassCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.AcceptanceFilterBypassCommand.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bypass', full_name='openxc.AcceptanceFilterBypassCommand.bypass', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1365,
  serialized_end=1425,
)


_PAYLOADFORMATCOMMAND = _descriptor.Descriptor(
  name='PayloadFormatCommand',
  full_name='openxc.PayloadFormatCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='openxc.PayloadFormatCommand.format', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PAYLOADFORMATCOMMAND_PAYLOADFORMAT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1427,
  serialized_end=1550,
)


_PREDEFINEDOBD2REQUESTSCOMMAND = _descriptor.Descriptor(
  name='PredefinedObd2RequestsCommand',
  full_name='openxc.PredefinedObd2RequestsCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='openxc.PredefinedObd2RequestsCommand.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1552,
  serialized_end=1600,
)


_COMMANDRESPONSE = _descriptor.Descriptor(
  name='CommandResponse',
  full_name='openxc.CommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.CommandResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='openxc.CommandResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='openxc.CommandResponse.status', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1602,
  serialized_end=1695,
)


_DIAGNOSTICREQUEST = _descriptor.Descriptor(
  name='DiagnosticRequest',
  full_name='openxc.DiagnosticRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.DiagnosticRequest.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='openxc.DiagnosticRequest.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='openxc.DiagnosticRequest.mode', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='openxc.DiagnosticRequest.pid', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='openxc.DiagnosticRequest.payload', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiple_responses', full_name='openxc.DiagnosticRequest.multiple_responses', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='openxc.DiagnosticRequest.frequency', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.DiagnosticRequest.name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decoded_type', full_name='openxc.DiagnosticRequest.decoded_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DIAGNOSTICREQUEST_DECODEDTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1698,
  serialized_end=1951,
)


_DIAGNOSTICRESPONSE = _descriptor.Descriptor(
  name='DiagnosticResponse',
  full_name='openxc.DiagnosticResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.DiagnosticResponse.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='openxc.DiagnosticResponse.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='openxc.DiagnosticResponse.mode', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='openxc.DiagnosticResponse.pid', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success', full_name='openxc.DiagnosticResponse.success', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negative_response_code', full_name='openxc.DiagnosticResponse.negative_response_code', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='openxc.DiagnosticResponse.payload', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.DiagnosticResponse.value', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1954,
  serialized_end=2115,
)


_DYNAMICFIELD = _descriptor.Descriptor(
  name='DynamicField',
  full_name='openxc.DynamicField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.DynamicField.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='openxc.DynamicField.string_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_value', full_name='openxc.DynamicField.numeric_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='openxc.DynamicField.boolean_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DYNAMICFIELD_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2118,
  serialized_end=2280,
)


_SIMPLEMESSAGE = _descriptor.Descriptor(
  name='SimpleMessage',
  full_name='openxc.SimpleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.SimpleMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openxc.SimpleMessage.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='openxc.SimpleMessage.event', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2282,
  serialized_end=2385,
)

_VEHICLEMESSAGE.fields_by_name['type'].enum_type = _VEHICLEMESSAGE_TYPE
_VEHICLEMESSAGE.fields_by_name['can_message'].message_type = _CANMESSAGE
_VEHICLEMESSAGE.fields_by_name['simple_message'].message_type = _SIMPLEMESSAGE
_VEHICLEMESSAGE.fields_by_name['diagnostic_response'].message_type = _DIAGNOSTICRESPONSE
_VEHICLEMESSAGE.fields_by_name['control_command'].message_type = _CONTROLCOMMAND
_VEHICLEMESSAGE.fields_by_name['command_response'].message_type = _COMMANDRESPONSE
_VEHICLEMESSAGE_TYPE.containing_type = _VEHICLEMESSAGE
_CANMESSAGE.fields_by_name['frame_format'].enum_type = _CANMESSAGE_FRAMEFORMAT
_CANMESSAGE_FRAMEFORMAT.containing_type = _CANMESSAGE
_CONTROLCOMMAND.fields_by_name['type'].enum_type = _CONTROLCOMMAND_TYPE
_CONTROLCOMMAND.fields_by_name['diagnostic_request'].message_type = _DIAGNOSTICCONTROLCOMMAND
_CONTROLCOMMAND.fields_by_name['passthrough_mode_request'].message_type = _PASSTHROUGHMODECONTROLCOMMAND
_CONTROLCOMMAND.fields_by_name['acceptance_filter_bypass_command'].message_type = _ACCEPTANCEFILTERBYPASSCOMMAND
_CONTROLCOMMAND.fields_by_name['payload_format_command'].message_type = _PAYLOADFORMATCOMMAND
_CONTROLCOMMAND.fields_by_name['predefined_obd2_requests_command'].message_type = _PREDEFINEDOBD2REQUESTSCOMMAND
_CONTROLCOMMAND_TYPE.containing_type = _CONTROLCOMMAND
_DIAGNOSTICCONTROLCOMMAND.fields_by_name['request'].message_type = _DIAGNOSTICREQUEST
_DIAGNOSTICCONTROLCOMMAND.fields_by_name['action'].enum_type = _DIAGNOSTICCONTROLCOMMAND_ACTION
_DIAGNOSTICCONTROLCOMMAND_ACTION.containing_type = _DIAGNOSTICCONTROLCOMMAND
_PAYLOADFORMATCOMMAND.fields_by_name['format'].enum_type = _PAYLOADFORMATCOMMAND_PAYLOADFORMAT
_PAYLOADFORMATCOMMAND_PAYLOADFORMAT.containing_type = _PAYLOADFORMATCOMMAND
_COMMANDRESPONSE.fields_by_name['type'].enum_type = _CONTROLCOMMAND_TYPE
_DIAGNOSTICREQUEST.fields_by_name['decoded_type'].enum_type = _DIAGNOSTICREQUEST_DECODEDTYPE
_DIAGNOSTICREQUEST_DECODEDTYPE.containing_type = _DIAGNOSTICREQUEST
_DYNAMICFIELD.fields_by_name['type'].enum_type = _DYNAMICFIELD_TYPE
_DYNAMICFIELD_TYPE.containing_type = _DYNAMICFIELD
_SIMPLEMESSAGE.fields_by_name['value'].message_type = _DYNAMICFIELD
_SIMPLEMESSAGE.fields_by_name['event'].message_type = _DYNAMICFIELD
DESCRIPTOR.message_types_by_name['VehicleMessage'] = _VEHICLEMESSAGE
DESCRIPTOR.message_types_by_name['CanMessage'] = _CANMESSAGE
DESCRIPTOR.message_types_by_name['ControlCommand'] = _CONTROLCOMMAND
DESCRIPTOR.message_types_by_name['DiagnosticControlCommand'] = _DIAGNOSTICCONTROLCOMMAND
DESCRIPTOR.message_types_by_name['PassthroughModeControlCommand'] = _PASSTHROUGHMODECONTROLCOMMAND
DESCRIPTOR.message_types_by_name['AcceptanceFilterBypassCommand'] = _ACCEPTANCEFILTERBYPASSCOMMAND
DESCRIPTOR.message_types_by_name['PayloadFormatCommand'] = _PAYLOADFORMATCOMMAND
DESCRIPTOR.message_types_by_name['PredefinedObd2RequestsCommand'] = _PREDEFINEDOBD2REQUESTSCOMMAND
DESCRIPTOR.message_types_by_name['CommandResponse'] = _COMMANDRESPONSE
DESCRIPTOR.message_types_by_name['DiagnosticRequest'] = _DIAGNOSTICREQUEST
DESCRIPTOR.message_types_by_name['DiagnosticResponse'] = _DIAGNOSTICRESPONSE
DESCRIPTOR.message_types_by_name['DynamicField'] = _DYNAMICFIELD
DESCRIPTOR.message_types_by_name['SimpleMessage'] = _SIMPLEMESSAGE

VehicleMessage = _reflection.GeneratedProtocolMessageType('VehicleMessage', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLEMESSAGE,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.VehicleMessage)
  ))
_sym_db.RegisterMessage(VehicleMessage)

CanMessage = _reflection.GeneratedProtocolMessageType('CanMessage', (_message.Message,), dict(
  DESCRIPTOR = _CANMESSAGE,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.CanMessage)
  ))
_sym_db.RegisterMessage(CanMessage)

ControlCommand = _reflection.GeneratedProtocolMessageType('ControlCommand', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLCOMMAND,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.ControlCommand)
  ))
_sym_db.RegisterMessage(ControlCommand)

DiagnosticControlCommand = _reflection.GeneratedProtocolMessageType('DiagnosticControlCommand', (_message.Message,), dict(
  DESCRIPTOR = _DIAGNOSTICCONTROLCOMMAND,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.DiagnosticControlCommand)
  ))
_sym_db.RegisterMessage(DiagnosticControlCommand)

PassthroughModeControlCommand = _reflection.GeneratedProtocolMessageType('PassthroughModeControlCommand', (_message.Message,), dict(
  DESCRIPTOR = _PASSTHROUGHMODECONTROLCOMMAND,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.PassthroughModeControlCommand)
  ))
_sym_db.RegisterMessage(PassthroughModeControlCommand)

AcceptanceFilterBypassCommand = _reflection.GeneratedProtocolMessageType('AcceptanceFilterBypassCommand', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTANCEFILTERBYPASSCOMMAND,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.AcceptanceFilterBypassCommand)
  ))
_sym_db.RegisterMessage(AcceptanceFilterBypassCommand)

PayloadFormatCommand = _reflection.GeneratedProtocolMessageType('PayloadFormatCommand', (_message.Message,), dict(
  DESCRIPTOR = _PAYLOADFORMATCOMMAND,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.PayloadFormatCommand)
  ))
_sym_db.RegisterMessage(PayloadFormatCommand)

PredefinedObd2RequestsCommand = _reflection.GeneratedProtocolMessageType('PredefinedObd2RequestsCommand', (_message.Message,), dict(
  DESCRIPTOR = _PREDEFINEDOBD2REQUESTSCOMMAND,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.PredefinedObd2RequestsCommand)
  ))
_sym_db.RegisterMessage(PredefinedObd2RequestsCommand)

CommandResponse = _reflection.GeneratedProtocolMessageType('CommandResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDRESPONSE,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.CommandResponse)
  ))
_sym_db.RegisterMessage(CommandResponse)

DiagnosticRequest = _reflection.GeneratedProtocolMessageType('DiagnosticRequest', (_message.Message,), dict(
  DESCRIPTOR = _DIAGNOSTICREQUEST,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.DiagnosticRequest)
  ))
_sym_db.RegisterMessage(DiagnosticRequest)

DiagnosticResponse = _reflection.GeneratedProtocolMessageType('DiagnosticResponse', (_message.Message,), dict(
  DESCRIPTOR = _DIAGNOSTICRESPONSE,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.DiagnosticResponse)
  ))
_sym_db.RegisterMessage(DiagnosticResponse)

DynamicField = _reflection.GeneratedProtocolMessageType('DynamicField', (_message.Message,), dict(
  DESCRIPTOR = _DYNAMICFIELD,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.DynamicField)
  ))
_sym_db.RegisterMessage(DynamicField)

SimpleMessage = _reflection.GeneratedProtocolMessageType('SimpleMessage', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLEMESSAGE,
  __module__ = 'openxc_pb2'
  # @@protoc_insertion_point(class_scope:openxc.SimpleMessage)
  ))
_sym_db.RegisterMessage(SimpleMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\ncom.openxcB\016BinaryMessages'))
# @@protoc_insertion_point(module_scope)
