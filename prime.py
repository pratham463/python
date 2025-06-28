num=29
flag=False
if num> 1 :
    for i in range(2,num):
         if(num%i)==0:
          flag=True
         break
    if flag:
         print(num,"this is not a prime no")
    else:
         print(num,"this is  a prime no")