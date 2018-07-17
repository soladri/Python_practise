f=list(range(1,10))
g=list(filter(lambda x:((x%3==0) | (x%5==0)),f))
h=sum(g[:])
print(h)