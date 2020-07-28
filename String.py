import binascii
Input = raw_input("enter a string: \n")
def strToBinary(Input):
	
	bin_conv = []
    
	for c in Input:
       		ascii_val = ord(c)
    		binary_val = bin(ascii_val)
       		bin_conv.append(binary_val[2:])
    
	return(' '.join(bin_conv))



print (strToBinary(Input))

