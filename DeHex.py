import binascii 

def dehexify(hexfile):
        Input = open(hexfile, "r").read()
        dehex = binascii.hexlify(Input)
        print(dehex)

dehexify("DeHex.txt")

