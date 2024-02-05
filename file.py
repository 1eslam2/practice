from module import Get_Bit
from module import Clr_Bit
from module import Togglr_Bit
from module import Set_Bit

x=int(input("please enter a number :")) 
y=int(input("enter the position of the bit :"))
print("the number befor any operation in binary :"+str(bin(x)[2:]))

result_clr=Clr_Bit(x,y)  # calling the function 
n1=int(result_clr,base=2)  # convert from binary to decimal with built in function (int())
print("the number afte clearing in binary is :"+str(result_clr))
print("the number afte clearing in decimal is :"+str(n1))

result_set=Set_Bit(x,y)
n2=int(result_set,base=2)  
print("the number afte seting in binary is :"+str(result_set))
print("the number afte seting in decimal is :"+str(n2))

result_toggle=Togglr_Bit(x,y)
n3=int(result_toggle,base=2)
print("the number afte toggling in binary is :"+str(result_toggle))
print("the number afte toggling in decimal is :"+str(n3))

Get_Bit(x,y)