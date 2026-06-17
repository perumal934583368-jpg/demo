"""for i in range(1,10):#rows
    for j in range (1,10):#columns
        if i== 1 and j<10:
          print("@ ",end="")
        elif i<10 and j==1:
         print("@ ",end="")
        else:
            print(j,"",end="")
    print()"""
"""for i in range(1,4):#rows
 for j in range (1,6):#columns
   if i==1 and j==3:
       print("@ ",end="")
   elif i==2 and j==2:
       print("@ ",end="")
   elif i==2 and j==3:
       print("@ ",end="")
   elif i==2 and j==4:
       print("@ ",end="")
   elif i==3 and j==1:
       print("@ ",end="")
   elif i==3 and j==5:
       print("@  ",end="")
   else:
       print(""," ",end="")
 print()"""
n=int(input("enter your table:"))
for i in range(1,11):
   print(i,"*",n,"=",i*n)
