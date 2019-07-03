#String Formatting
#Given an integer n print the following values for each integer from to 1 to n

#bin(x) gives the binary value of number
#oct(x) gives the octalk value of the number
#hex(x) gives the hex value of the number
  
    
def print_formatted(number):
    # your code goes here
    target = bin(number)
    sp = len(target[1:])
    
    for i in range(1,number+1):
        octal_n = oct(i)
        hex_n = hex(i)
        bin_n = bin(i)        
        print(' '*(sp-1-len(str(i)))+str(i)+' '*(sp-len(octal_n[2:]))+octal_n[2:]+' '*(sp-len(hex_n[2:]))+hex_n[2:].upper()+' '*(sp-len(bin_n[2:]))+bin_n[2:])

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)