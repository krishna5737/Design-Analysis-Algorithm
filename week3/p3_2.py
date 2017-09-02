comparisons = 0

def quickSort(ar, l, r): 
    global comparisons
    
    if l >= r:
        return 
    p = ar[r]
    (ar[r],ar[l]) = (ar[l],ar[r])
    comparisons += (r-l)
    
    i = l+1
    for j in range(l+1, r+1):
        if ar[j] < p:
            (ar[i],ar[j])=(ar[j],ar[i])
            i += 1
    (ar[l],ar[i-1]) = (ar[i-1],ar[l])
    
    quickSort(ar, l, i-2)
    quickSort(ar, i, r)
    

r = [1,3,5,2,4,6]
'''f = open('r.txt', 'r')
r = []

for line in f.readlines():
    r.append(int(line))
'''    
quickSort(r,0,len(r)-1)
print(comparisons)
