#!/usr/bin/env python
import os
with open('C:\\Users\\rodster\\Documents\\GitHub\\wfuzz\\a-z.txt','a+') as f:
    f.truncate()
    for x in range(0,26):
        charact=chr(x+ord('a'))
        f.write(charact)
        f.write(os.linesep)
    f.close()