'''
Created on 18 de mai de 2017

@author: alexsandrospecht
'''
import sys

def main():
    Conversor(sys.argv[1]).converter()

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from github.conversor import Conversor
    main()        
    