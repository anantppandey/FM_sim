# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from eufs_msgs/SLAMErr.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class SLAMErr(genpy.Message):
  _md5sum = "dc71d228c77971f0462d47d101a48d17"
  _type = "eufs_msgs/SLAMErr"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# Message for the error of our SLAM algorithm. All of them are based on euclidean distances, besides the map similarity,
# which can be interpreted as a percentage of how well our algorithm describes the map.

Header header

float64 x_err
float64 y_err
float64 z_err
float64 x_orient_err
float64 y_orient_err
float64 z_orient_err
float64 w_orient_err
float64 map_similarity

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','x_err','y_err','z_err','x_orient_err','y_orient_err','z_orient_err','w_orient_err','map_similarity']
  _slot_types = ['std_msgs/Header','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,x_err,y_err,z_err,x_orient_err,y_orient_err,z_orient_err,w_orient_err,map_similarity

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SLAMErr, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.x_err is None:
        self.x_err = 0.
      if self.y_err is None:
        self.y_err = 0.
      if self.z_err is None:
        self.z_err = 0.
      if self.x_orient_err is None:
        self.x_orient_err = 0.
      if self.y_orient_err is None:
        self.y_orient_err = 0.
      if self.z_orient_err is None:
        self.z_orient_err = 0.
      if self.w_orient_err is None:
        self.w_orient_err = 0.
      if self.map_similarity is None:
        self.map_similarity = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.x_err = 0.
      self.y_err = 0.
      self.z_err = 0.
      self.x_orient_err = 0.
      self.y_orient_err = 0.
      self.z_orient_err = 0.
      self.w_orient_err = 0.
      self.map_similarity = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_8d().pack(_x.x_err, _x.y_err, _x.z_err, _x.x_orient_err, _x.y_orient_err, _x.z_orient_err, _x.w_orient_err, _x.map_similarity))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.x_err, _x.y_err, _x.z_err, _x.x_orient_err, _x.y_orient_err, _x.z_orient_err, _x.w_orient_err, _x.map_similarity,) = _get_struct_8d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_8d().pack(_x.x_err, _x.y_err, _x.z_err, _x.x_orient_err, _x.y_orient_err, _x.z_orient_err, _x.w_orient_err, _x.map_similarity))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.x_err, _x.y_err, _x.z_err, _x.x_orient_err, _x.y_orient_err, _x.z_orient_err, _x.w_orient_err, _x.map_similarity,) = _get_struct_8d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_8d = None
def _get_struct_8d():
    global _struct_8d
    if _struct_8d is None:
        _struct_8d = struct.Struct("<8d")
    return _struct_8d
