if __name__ == '__main__':
    N = int(input())

ins = 'insert'
rem = 'remove'
appen = 'append'
outlist=[]

for i in range(N):
    data = input().split() 
    if(ins in data[0] ):
        outlist.insert(int(data[-2]),int(data[-1]))
    elif(appen in data[0] ):
        outlist.append(int(data[-1]))    
    elif(rem in data[0] ):
        outlist.remove(int(data[-1]))
    elif('sort' == data[0] ):
        outlist.sort()
    elif('reverse' == data[0] ):
        outlist.reverse()
    elif('pop' == data[0] ):
        outlist.pop()
    else:
        print(outlist)
        
        
        
            
        

    