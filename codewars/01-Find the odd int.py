m=dict()

def find_it(seq):
    global m
    
    for i in seq:m[i]=0
    for i in seq:
        m[i]+=1

    for i in m:
        x=m.get(i)
        if x%2!=0:
            return x

    
    return None



print(find_it([1,1,2,2,2,2,3,3,3]))



