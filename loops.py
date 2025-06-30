number = int(input("enter no. to check"))
flag=False

if number> 1 :
    for i in range(2,number):
         if(number%i)==0:
          flag=True
         break
    if flag:
         print(number,"this is not a prime no")
    else:
         print(number,"this is  a prime no")
