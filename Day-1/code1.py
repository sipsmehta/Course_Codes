#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello,python")


# In[2]:


#create a variable in py 
my_variable= "hi"
print(my_variable)


# In[3]:


# ; >> For side by side placing a data 
# , Is used to deal with conditional cases 
# def is for the fuction declarations
#creating my first func in py 
#cube of number 

def cube(num):
    cube_num= num** 3
    return cube_num
    


# In[5]:


# for reading a file or just any data --> r at the start 

print(f"2 cubed is {cube(2)}")


# In[6]:


#run of circles
#inrange is a inbuild py func that takes care of the start and end _point
#inrange func is taken care of inside py libarary numpy 
for i in range(2,11):
    print(i)


# In[11]:


i= 2
while i < 11: 
    print(i)
    i=i+1
      
      


# In[14]:


#my problem is doubling a number 
def doubles(num):
    return num*2 #multiplying each output by 2 

my_num = 2
for i in range (0, 3):
    my_num= doubles(my_num)
    print(my_num)


# In[31]:


#print number is even or odd 
# taking a number input from a user
#displaying 9 consequetive no with even or odd

def even_odd(num):
    if num%2==0: 
        print("even")
    else :
        print("odd")
    for i in range(0, 20 , 2):
        print(num+i)
        
def even_odd_uncessary(num):
    if num%2 ==0:
        print("even")
    else:
        print("odd")
        
    for i in range(0 , 18, 2):
        print(num+i, sep='', end=', ' , flush=True) #flush checking your code buffer removing unnecsary funcyion calls 
    print(num+i, sep='', end='.\n' , flush=False)
        
if __name__ == '__main__':
      
    
     even_odd_uncessary(9)
     
    


# In[33]:


#differentiating by python
# first python pkg - SYMPY--- It is a py pkg that deals with derrivatives , integrals , limits , series 
# numpy is dealing maths cal for set theories & matrix arrays 

from sympy import * 
from sympy import * 
x , y , z = symbols('x,y,z')
init_printing(use_unicode=True)


# In[35]:


# Implementing Google Text to Speech
get_ipython().system('pip install gTTS')
get_ipython().system('pip install playsound')
from gtts import gTTS
#playsound pkg is used to get any sound data from Gtts and save it in a sound file
from playsound import playsound
text_val = 'Hello'
language ='en'
obj = gTTS(text = text_val , lang = language , slow= False)
obj.save("exam.mp3")
playsound("exam.mp3")


# In[ ]:
