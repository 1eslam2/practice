def Clr_Bit (x,y):
   binary_number=bin(x)[2:] 
   n=[]
   for i in binary_number[::-1]:
      n+=i
   n[y]="0"         # deleting element from list 
   n.reverse()      # reverse sequance in list to comeback to the original sequence of bits 
   n="".join(n)     # make list elements as one element 
   return n 

def Set_Bit(x,y):
   binary_number=bin(x)[2:] 
   n=[]
   for i in binary_number[::-1]:  # reversing to make usaccess on right element
      n+=i
   if n[y]=="0":
      n[y]="1"
   n.reverse()   
   n="".join(n)     # the same thing we did in first function 
   return n 

def Get_Bit(x,y):
   binary_number=bin(x)[2:] 
   n=[]
   for i in binary_number[::-1]:
      n+=i
   print("the bit is :"+str(n[y]))

def Togglr_Bit(x,y):
   binary_number=bin(x)[2:] 
   n=[]
   for i in binary_number[::-1]: 
      n+=i
   if n[y]=="0":
      n[y]="1"
   else:
      n[y]="0"
   n.reverse()    # the same thing we did in first and second function 
   n="".join(n)      
   return n 



