#!/usr/bin/env python3
islower = __import__('7-islower').islower

def islower(c):
    # Check if the ASCII value of the character is within the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')
