#!/usr/bin/env python
# encoding: utf-8

import ctypes

class ICMP(ctypes.Structure):
    """ICMP Structure"""
    _fields_ = [
        ('type', ctypes.c_ubyte),
        ('code', ctypes.c_ubyte),
        ('checksum', ctypes.c_ushort),
        ('unused', ctypes.c_ushort),
        ('next_hop_mtu', ctypes.c_ushort)
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass
