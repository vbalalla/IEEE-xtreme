t = int(input())
for i in range(t):
    a1 = int(input())
    r1 = input()
    r2 = input()
    r3 = input()
    r4 = input()
    a2 = int(input())
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()

    if(a1==1):
        t1 = r1
    elif(a1==2):
        t1 = r2
    elif(a1==3):
        t1 = r3
    elif(a1==4):
        t1 = r4
    else:
        print("Volunteer cheated!")

    if(a2==1):
        t2 = s1
    elif(a2==2):
        t2 = s2
    elif(a2==3):
        t2 = s3
    elif(a2==4):
        t2 = s4
    else:
        print("Volunteer cheated!")

    l1 = t1.split(" ")
    print(l1)
    l2 = t2.split(" ")
    print(l2)
    l3 = []

    for i in l1:
        for j in l2:
            if(i==j):
                l3.append(j)

    if(len(l3) == 0):
        print("Volunteer cheated!")
    elif(len(l3)>1):
        print("Bad magician!")
    else:
        print(l3[0])
            
