#n=int(input("Enter a number:"))
#for i in range(0,n):
 #   print("*",end="")


#n=int(input("enter a number"))
#m=int(input("enter a number"))
#for i in range(0,n):
 #   for j in range (0,m):
  #      print("*",end="")
#print()  ;

#n=int(input("enter a number"))
#for i in range(1,n+1):
 #   for j in range(i):
 #       print("*",end=" ")
 #   print()    

#n=int(input("enter a number"))
#for i in range(n,0,-1):
#    for j in range(i):
 #       print("*",end=" ")
  #  print()    



#n=int(input("enter a number"))
#for i in range(1,n+1):
 #   for j in range(1,i+1):
  #      if(j%2==0):
   #       print("*",end=" ")
    #    else:
     #     print(j,end=" ")   
     # 
# N=int(input("enter a number:"))
# for i in range(1,N+1):
    # for j in range (N+1-i):
    #    if(j==1 or j==N):
        #  print("*")
    # else:
        #  print("_")   
# print()

n=int(input("enter a number:"))
for i in range (1,n+1):
    for j in range(n-i):
       print("_",end=" ")
    for j in range(i):
       print("*")
print()       











