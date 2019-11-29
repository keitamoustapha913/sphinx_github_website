"""
This is an example of dummy codes for trial

"""

import logging 
from abc import ABC, abstractmethod 
  
def main(): 
    """ Configure the logging system """

    logging.basicConfig(filename ='app.log', 
                        level = logging.ERROR) 
      
    # Variables (to make the calls that follow work) 
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
      
    # Example logging calls (insert into your program) 
    logging.critical('Host %s unknown', hostname) 
    logging.error("Couldn't find %r", item) 
    logging.warning('Feature is deprecated') 
    logging.info('Opening file %r, mode = %r', filename, mode) 
    logging.debug('Got here') 


class Polygon(ABC): 
  
    "abstract method "
    def noofsides(self): 
        pass
  
class Triangle(Polygon): 
  
    "Triangle overriding abstract method "
    def noofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    " Pentagon overriding abstract method" 
    def noofsides(self): 
        print("I have 5 sides") 
  
class Hexagon(Polygon): 
  
    " Hexagon overriding abstract method" 
    def noofsides(self): 
        print("I have 6 sides") 
  
class Quadrilateral(Polygon): 
  
    "Quadrilateral overriding abstract method "
    def noofsides(self): 
        print("I have 4 sides") 
  

      
if __name__ == '__main__':
    main() 
    # Driver code 
    R = Triangle() 
    R.noofsides() 
    
    K = Quadrilateral() 
    K.noofsides() 
    
    R = Pentagon() 
    R.noofsides() 
    
    K = Hexagon() 
    K.noofsides() 