'''
Created on Mar 1, 2014

@author: Nick Crawford
'''

class Stack(object):
    
    def __init__(self, initial_set=[]):
        if isinstance(initial_set, list):
            self.objs = initial_set
        else:
            self.objs = [initial_set]
        
    def push(self, obj):
        self.objs.append(obj)
        
    def pop(self):
        return self.objs.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.objs[-1]
        
    def is_empty(self):
        return len(self.objs) == 0
    
    def __repr__(self):
        return '%s(initial_set=%s)' % (self.__class__.__name__, self.objs)
    
    def __str__(self):
        return str(self.objs)
    
    def __iter__(self):
        return iter(self.objs)