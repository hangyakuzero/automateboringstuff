# a python tool to mimic the wc tool in unix
# argument parser, -c number of bytes, -l number of lines, -m number of characters
import os

with open("test1.txt", "r") as f:
    lines = f.readlines()
    l = len(lines)
    f.seek(0)
    size = os.path.getsize("test1.txt")
    content = len(f.read())
    print(content)
    print(l)
    print(size)
