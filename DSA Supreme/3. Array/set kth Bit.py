
def setBit(n:int,k:int):
    '''
    Setting kth right bit of the binary representation
    of the number
    '''   
     
    binVal = bin(n)[2:]
    binLen = len(binVal)
    # print("Bin Value:",binVal)
    # print("K:",k)
    if binLen<k:
        padLen = k- binLen
        binVal = '0'*padLen + binVal
    binLen = len(binVal)
    # print("Bin length:",binLen)
    update_pos = binLen - k
    # print("Update position:",update_pos)
    if binVal[update_pos] =='0':
        binVal = binVal[:update_pos] + '1' + binVal[update_pos+1:]
    else:
        binVal = binVal[:update_pos] + '0' + binVal[update_pos+1:]
    # print("Bin Value:",binVal)
    # print("Decimal Value:",int(binVal,2))
    
    
setBit(10,1)
setBit(10,2)
setBit(10,3)
setBit(10,4)
setBit(10,5)
setBit(10,6)
setBit(10,7)


def setBit(n:int,k:int):
    print( n | k<<1)

setBit(10,1)
setBit(15,3)
setBit(10,3)
setBit(10,4)
setBit(10,5)
setBit(10,6)
setBit(10,7)