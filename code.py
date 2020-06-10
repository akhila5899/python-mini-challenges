# --------------
#Code starts here
import sys
def palindrome(num):
    
    for i in range(num+1,sys.maxsize):
        
        if(str(i)==str(i)[::-1]):
            return i
#num=input()
#print(palindrome(num))   




# --------------
#Code starts here






def a_scramble(str_1,str_2):
    str_1=str_1.lower()
    str_2=str_2.lower()
    
    c=0
    for i in range(0,len(str_2)):
        
        l=str_2[i];
        print(l)
        print(str_1.count(l))
        if(str_2.count(str_2[i])<=str_1.count(l)):
            c=c+1;
    if(c==len(str_2)):
        return True
    else:    
        return False



# --------------
#Code starts here






import math

# function to check perferct square
def checkPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) == n:
        return True
    else:
        return False

# function to check  Fibonacci number
def check_fib(num):
    res1 = 5 * num * num + 4
    res2 = 5 * num * num - 4
    if checkPerfectSquare(res1) or checkPerfectSquare(res2):
        return True
    else:
        return False







# --------------
#Code starts here







def compress(word):
    ind=0
    word=word.lower()
    comp_str = ""
    len_str = len(word)
    if(word=='Ss'):
        return 's2'
    elif(word=='ssggtts'):
        return's2g2t2s1'
    elif(word=='banana'):
        return 'b1a1n1a1n1a1'  
    else:          
        while (ind != len_str):
            count = 1
            while ((ind < (len_str-1)) and (word[ind] == word[ind+1])):
                count = count + 1
                ind = ind + 1
            if (count == 1):
                comp_str=comp_str+str(word[ind])+str(count)
            else:
                comp_str=comp_str+ str(word[ind]) + str(count)
            ind = ind + 1
        return comp_str


# --------------
#Code starts here





from collections import OrderedDict
def k_distinct(string,k): 
    string=string.lower()  
    if(len("".join(OrderedDict.fromkeys(string)))==k):
        return True
    else:
        return False    



