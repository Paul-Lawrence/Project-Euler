import functions as funcs

n = 1000000
divsums= funcs.divcount(n)

chainlength = [0]*(n+1)
max_chain = 1
for i in range(n+1):
    #print(i)
    current = i
    chaincount = 0
    #nextsum = divsums[i]
    chainset = []
    if chainlength[i] != 0:
        pass
    elif divsums[i] == 1:
        chainlength[i] = -1
    else:
        while chainlength[current]==0:
            chainset.append(current)
            current = divsums[current]
            #print(current)
            #print(chainset)
            if current >= n:
                for num in chainset:
                    chainlength[num] = -1
                    current = 0
            elif chainlength[current]==-1 :
                for num in chainset:
                    chainlength[num] = -1
            elif current in chainset:
                #print(current,chainlength[current])
                #print(current, chainset)
                #print('loop', current)
                ind = chainset.index(current)
                #print(chainset[ind:])
                for num in chainset[0:ind]:
                    chainlength[num]= -1
                for num in chainset[ind:]:
                    #print(num, chainlength[num])
                    chainlength[num]=len(chainset[ind:])
#print(divsums)
#print(chainlength)
for x in range(n+1):
    if chainlength[x]>1:
        print(x, chainlength[x])
#print([x for x in range(n+1) if chainlength[x]>1])
chainmax = max(chainlength)
print([x for x in range(n+1) if chainlength[x]==chainmax])