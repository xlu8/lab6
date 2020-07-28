import binascii
import sys
def Bi_to_Hex(readfile,writefile):
         
       Hex = ""
       byte = ""
       with open(readfile,"rb") as r:
              byte = r.read(1)
              while byte != "":
                         Hex += binascii.hexlify(byte)
                         byte =r.read(1)
       print("Hexadecimal array:")
       print(Hex)
       f = open(writefile, "w")
       f.write(Hex)
       f.close()
Bi_to_Hex("hello2.txt", "HexDump_result.txt")

