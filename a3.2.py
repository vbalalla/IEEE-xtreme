l = input().split(" ")
a1 = int(l[0])
a2 = int(l[1])
n = int(input())
t1 = int(l[0])
t2 = int(l[1])

for i in range((n-1)%6):
    ans = a2 - a1
    a1 = a2
    a2 = ans
        
print(a1%1000000007)
