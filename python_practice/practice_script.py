'''
This script contains an example class that we will write. The class will be called algebra, and it will contain some simple methods to do algebraic manipulation.'''

sample_int = 5

class Algebra :
    def __init__(self, x, y) :
        #we are defining the arguments as attributes of the object itself
        self.x = y
        self.y = y
        
    def add( self ) :
        return self.x + self.y

    def divide( self ) :
        return self.x / self.y
    
    def multiply ( self ) :
        return self.x * self.y

    def subtract ( self ) :
        return self.x -  self.y

    def complicated_algebra( self ) :
        return self.multiply() + self.subtract()
    
    def modify_x(self) :
        self.x = self.x * 2
