n=int(input("Enter the limit : "))
k1,k2=0,1
c=0
a=[k1,k2]
while c<n:
    k=k1+k2
    k1=k2
    k2=k
    c+=1
    a.append(k)
print(a)
