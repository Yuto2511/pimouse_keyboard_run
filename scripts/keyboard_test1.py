#!/usr/bin/env python
#encoding: utf8

import sys, termios

fd = sys.stdin.fileno()

old = termios.tcgetattr(fd)
new = termios.tcgetattr(fd)

new[3] &= ~termios.ICANON
new[3] &= ~termios.ECHO

try:
    termios.tcsetattr(fd, termios.TCSANOW, new)
    ch = sys.stdin.read(1)

finally:
    termios.tcsetattr(fd, termios.TCSANOW, old)

print(ch)
print(type(ch))
