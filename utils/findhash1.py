from hashlib import shake_256
from sys import stdin, stdout

from jelly import jellify, jelly_eval

objects = stdin.read()

try:
    objects = jellify(eval(objects))
except Exception:
    objects = jelly_eval(objects, [])

for object in objects:
    stdout.buffer.write(shake_256(repr(object).encode("utf-8")).digest(512))
