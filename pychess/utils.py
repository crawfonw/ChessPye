'''
Created on Jun 22, 2013

@author: nick

'''

def enum(**enums):
    return type('Enum', (), enums)

def ctl(i):
    return chr(97 + i)