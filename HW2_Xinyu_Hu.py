#!/usr/bin/env python
# coding: utf-8

# ### Write your full name and Perm number below

# Full name: Xinyu, Hu
# 
# Perm number: X303556
# 
# Change the filename to HW2_ followed by your last name and first name with an underscore between them. For example, Abraham Lincoln's homework filename would be "HW2_Lincoln_Abraham.ipynb"

# ### **Week 2 - Homework**
# 
# Practice and repetition is the key to master this week's materials. So, this week's homework is an extension to the practice script. If you finished the practice, it should be easy.
# 
# ---
# 

# #### Problem 1 (2.5 pt)
# 
# Write a function, `sum_sqr_list(l)` that performs the following tasks.
# 
# - This function receives a list `l` as an argument.
# 
# - It returns a list of two values: One is the sum of all values in the list, and the other is the sum of squares of all values.
# 
# - At the top of the function, it checks if the argument is a list.  If it is not a list, it prints error "Error: The argument is not a list."
# 
# - If the argument is a list, it calculates the sum of all values in the list and the sum of squares of all values in the list.
# 
# - It returns a list with two values: sum and sum of sequares. If the argument was not a list, it returns [0, 0].
# 
# 
# 
# Using this function should look like below:
# ![HW2_1.png](attachment:HW2_1.png)

# In[5]:


# Complete the following function.

# DO NOT CHANGE THE FUNCTION NAME AND ARGUMENTS!!! They will be used to test your answers.

def sum_sqr_list(l):

    sum = sqsum = 0
    
    if type(l) != type(list()):
        print("Error: The argument is not a list.")
        return [0,0]
    else:
        for i in l:
            sum += i
            sqsum += i*i
            
    return [sum,sqsum]


# In[6]:


# The following code is provided for your test.
# You can modify it as you want, to test your function.

l = {1, 2, 3, 4, 5}
a = sum_sqr_list(l)
print(a)

l = [1, 2, 3, 4, 5]
a = sum_sqr_list(l)
print(a)


# ---
# #### Problem 2 (2.5 pt)
# Write a function, `make_dict(keys,values)` that performs the following tasks.
# 
# - This function receives two lists `keys` and `values` as arguments.
# 
# - It returns a dictionary using these two lists, pairing corresponding items.
# 
# - The function should test if the number of elements in two lists is the same. If not, it should print "Error: the lengths of two lists are not the same"
# 
# 
# Using this function should look like below:
# ![HW2_2.png](attachment:HW2_2.png)

# In[22]:


# Complete the following function.

# DO NOT CHANGE THE FUNCTION NAME AND ARGUMENTS!!! They will be used to test your answers.

def make_dict(keys, values):
    if len(keys) != len(values):
        print("Error: the lengths of two lists are not the same")
        return 0
    else:
        hash = {}
        for i in range(len(keys)) :
            hash[keys[i]] = values[i]
    return hash
        


# In[23]:


# The following code is provided for your test.
# You can modify it as you want, to test your function.

k = ['a','b','c','d']
v = [1,2,3,4]
d = make_dict(k,v)
print(d)
print(' ')

k = ['A','B','C']
v = [[1,2,3], ['n','m','p','q','x'], ['USA', 'China', 'Chile', 'Kenya']]
d = make_dict(k,v)
print(d)


# ---
# #### Problem 3 (2.5 pt)
# Write a function, `append_n_elements_from_2nd_to_1st(la, lb, n)` that performs the following tasks.
# 
# - This function receives two lists `la` and `lb`, and a number `n` as arguments.
# 
# - It moves the last `n` elements in `lb` to `la` in the reversed order. See expected outcome below.
# 
# - It checks if the number of elements in `lb` is equal to or greater than `n`. If not, it prints "Error: the 2nd list must have at least 'n' number of elements."
# 
# 
# Using this function should look like below:
# ![HW2_3.png](attachment:HW2_3.png)

# In[52]:


# Complete the following function.

# DO NOT CHANGE THE FUNCTION NAME AND ARGUMENTS!!! They will be used to test your answers.

def append_n_elements_from_2nd_to_1st(la, lb, n):
    if n > len(lb):
        print("Error: the 2nd list must have at least 'n' number of elements.")
        return 0
    else :
        for i in range(n):
            la += [lb[len(lb) - i - 1]]
            del lb[len(lb) - 1]
        return la
    


# In[53]:


# The following code is provided for your test.
# You can modify it as you want, to test your function.

A = [1,2,3]
B = [4,5,6,7,8,9]
append_n_elements_from_2nd_to_1st(A, B, 4)
print(A)
print(B)
print(' ')

A = [1,2,3,4,5,6]
B = [7,8,9]
append_n_elements_from_2nd_to_1st(A, B, 6)
print(A)
print(B)


# ---
# #### Problem 4 (2.5 pt)
# Complete a class, `petClass()`, which was used in the lecture video.
# 
# - Add a function `changeName()` that will change the name of the pet.
# 
# - Add another function `nickName()` that will assign a nick to the pet. You need to add another class member variable, `nick`, to make the testing script to work properly.
# 
# 
# Using this class should look like below:
# ![HW2_4.png](attachment:HW2_4.png)

# In[16]:


# Complete the following class.

# DO NOT CHANGE THE CLASS NAME!!!

class petClass():
    def __init__(self, name, color="brown"):
        self.name = name
        self.color = color
        self.nick = "no nick yet"
    
    def petColor(self):
        print(self.name, 'is', self.color)
        
    def dye(self, color):
        self.color = color
        self.petColor()
        
    def changeName(self,newname):
        self.name = newname
    
    def nick(self):
        if self.nick == "no nick yet":
            print("no nick yet")
        else:
            print(self.nick)    
        
    def nickName(self,newnick):
        self.nick = newnick


# In[17]:


# The following code is provided for your test.
# You can modify it as you want, to test your function.

myDog = petClass('Spot', 'black and white')
print(myDog.name)
print(" ")

myDog.changeName('Cow')
print(myDog.name)
print(" ")

print(myDog.nick)
myDog.nickName('Ticky')
print(myDog.nick)
print(" ")


# ---
# ## **Check your code before you commit and push your homework**
# 
# ### If there is any error in your code, including any practice code you wrote to test your answers, your homework will not be scored.
# 
# #### Here are steps you must take to make sure there is no error in your script.
# 1. You must first restart the kernel. It is in the menu "kernel->Restart Kernel". Or click the restart button.
# ![restart_kernel.png](attachment:restart_kernel.png)
# 2. Run all cells. You can do this by clicking the menu "Run->Run all cells".
# 3. Fix any errors.
# 4. Repeate 1-3 until you don't see any errors.
# 5. **IMPORTNAT: Clear All Outputs (Right mouse click->Clear All Output)**
# 6. **IMPORTNAT: Save your file and change the filename to "HWn_Lastname_Firstname.ipynb"**
# 7. **Run the following cell and make sure you don't see any errors. This is the code that the TA or the instructor will use to generate testable code.**

# In[ ]:


# If the name of the student is Abraham Lincoln, then the code should look
# like below.

get_ipython().system("jupyter nbconvert --to script 'HW2_Xinyu_Hu.ipynb' # Change this to your name (name of this file)")
import HW2_Xinyu_Hu as hw  # Change this to your name
dir(hw)

# After running this code, you should see, at the bottom, the function names
# of your homework answers.

# If you see errors, please make sure the file names, module names are all
# properly set up. Then restart the kernel and try it again.


# In[ ]:




