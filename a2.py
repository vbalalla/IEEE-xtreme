h = int(input())
m = int(input())

l = ["o\'clock","one minute","two minutes","three minutes","four minutes",
     "five minutes","six minutes","seven minutes","eight minutes","nine minutes",
     "ten minutes","eleven minutes","twelve minutes","thirteen minutes","fourteen minutes","quarter",
     "sixteen minutes","seventeen minutues","eighteen minutes","nineteen minutes",
     "twenty minutes","twenty one minutes","twenty two minutes","twenty three minutes",
     "twenty four minutes","twenty five minutes","twenty six minutes","twenty seven minutes",
     "twenty eight minutes","twenty nine minutes"]

s = ["twelve","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]

if (m==30):
    print("half past " + s[h])
elif (m==0):
    print(s[h] + " " + l[0])
elif (m<30):
    print (l[m] + " past " + s[h])
else:
    print(l[60-m] + " to " + s[h+1])
          
        
