import os
with open('C:\\Users\\rodster\\Documents\\GitHub\\wfuzz\\urlascii2.txt','a+') as f:
    f.truncate()
    for x in range(0,256):
        payload=str(x)
        
        aaa=str(hex(int(payload))).replace('0x','')
        if int(payload)<16:
            aaa='0'+aaa        
        f.write('%'+aaa)
        f.write(os.linesep)
    f.close()
