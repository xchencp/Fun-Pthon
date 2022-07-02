#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""In this game, you have $1000 in hand. Good luck and have fun!"""


# In[37]:


"""Adjustment area: """
Beginning_Cash = 100
win_transaction_fee = 10

from random import randint
from IPython.display import clear_output
cash = Beginning_Cash
while cash>0:
    print ("You have %d in hand." %cash)
    x = int(input ("Please input the money for this game (max is %d)"%cash))
    clear_output(wait=True)
    if x<=cash:
        a = randint(1,6) 
        b = randint(1,6) 
        c = randint(1,6)
        print("Casino : %d + %d + %d = "%(a,b,c),a+b+c)
        A = randint(1,6) 
        B = randint(1,6)
        C = randint(1,6)
        print("Player : %d + %d + %d = "%(A,B,C),A+B+C)
        if a+b+c>A+B+C:
            print("Casino wins!")
            cash = cash - x
        else:
            if a+b+c<A+B+C :
                print("Player wins!")
                cash = cash + x -win_transaction_fee
            else:
                print("The same.")
    else:
        print("Please input a smaller number!")
print("You lost all your money.")


# In[ ]:




