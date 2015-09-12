l = input().split(" ")
x = int(l[0])
y = int(l[1])
n = int(input())

lst = []

for i in range(n+1):
    lst.append(0)

lst[1] = x
lst[2] = y

for i in range(3,n+1):
    lst[i] = lst[i-1] - lst[i-2]

print(lst[n]%1000000007)    
