for k in range(0,15):
    print(k)

for i in range(5,1000,5):
    print(i)

for j in range(1,100):
    if j%5==0:
        print("%d coding"%j)
    if j%10==0:
        print("%d coding dojo"%j)
sum=0   
for e in range(0,500000):
    if e % 2 != 0:
        sum=sum+1
print(sum)


for s in range(0,2018,-4):
    print(s)


# def countdown(x):
#     while x!=0:
#               print(x)
#               x=x-4
# countdown(2018)

# countdown = 2018
# while countdown:
#     print (countdown)
#     countdown -= 4
# print( "Blastoff!")

def flex_counter(LowNum,highNum,mlut):
    for i in range(LowNum,highNum):
        if i%mlut==0:
            print(i)
flex_counter(2,10,3)