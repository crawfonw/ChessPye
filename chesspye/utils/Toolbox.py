'''
Created on Mar 1, 2014

@author: Nick Crawford
'''

def enum(**enums):
    return type('Enum', (), enums)

def ctl(i):
    return chr(97 + i)

def letter_to_number(s):
    return ord(s) - 97
    
def scalar_mult_tuple(alpha, tup):
    return tuple(alpha*i for i in tup)