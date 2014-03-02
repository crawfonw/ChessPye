'''
Created on Jun 20, 2013

@author: nick
'''

class Player(object):
    
    def __init__(self, name, type, color):
        self.name = name
        self.type = type
        self.color = color
        
    def __str__(self):
        return self.name