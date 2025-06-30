#a=10
# b,c=10,20
# d=e=f=30
# print(a)
# print(c)


# a=int(input("Enter a value"))
# b=int(input("Enter b value"))
# print(a)
# print(a+b)
# d,e,f=map(int,input("enter d ,e,f").split())
# print(e)


# no=int(input("Enter no to check"))
# if no%10==7 or no/10==7:
#     print("lucky no")
# else:
#         print("not lucky")




# for i in range(10):
#     print(i,end=",")

# for i in range(10,100):
#    if i%10==6 or i/10==6:  
#        print(i,end=",")



n=10
list1=[]
for i in range(n):
    if i%2==0:
        list1.append(i)
print(list1)
#comprehension
list2=[x for x in range(n) if x%2==1]
print(list2)