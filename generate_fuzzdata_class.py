#!/usr/bin/env python
   
class fuzzdata(object):
          
    '''abstract factory'''
    #---------------------------------------------
    def init():
        '''initiate something'''
        print 'product starting'
        
          
    #def factory_make():
        
    #generate ascii character function
    #usage() like this 'make_ascii(0,255,c:\\1.txt)'
    def make_ascii(start,end,output_path_file) :
        import struct
        import binascii
        import os                  
        if os.path.exists(output_path_file):
            if '.' in output_path_file:
                dir_path,suffix=output_path_file.split('.')
                dir_path=dir_path+'1'
                output_path_file=dir_path+suffix
        with open(output_path_file,'a+') as f:
            f.truncate()
            for x in xrange(start,end+1):
                charact=chr(x+ord('a'))
                f.write(charact)
                f.write(os.linesep)
            f.close()
        print output_path_file
        
        
        #no suffix file
        #usage() like this 'make_01_character(0,255,c:\\1)'
        #---------------------------------------------------------------
    def make_01_character(self,start,end,output_path_file):
        import struct
        import binascii
        import os        
        if os.path.exists(output_path_file):
            if '.' in output_path_file:
                dir_path,suffix=output_path_file.split('.')
                dir_path=dir_path+'1'
                output_path_file=dir_path+suffix        
        with open(output_path_file,'wb+') as f:
            f.truncate()
            for x in xrange(start,end+1):
                hex_number=str(x)
                if(len(hex_number)==1):
                    hex_number='0'+hex_number
                if(len(hex_number)==3):
                    hex_number=str(hex(int(hex_number))).replace('0x','')
                bindata=binascii.a2b_hex(hex_number)
                f.write(struct.pack('s',bindata))
                f.write(os.linesep)
            f.close()
        print output_path_file     
    pass
if __name__=='__main__':
    priduct=fuzzdata()
    priduct.make_01_character(0,255,'d:\\abb')
    #print '111'
