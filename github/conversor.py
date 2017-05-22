'''
Created on 16 de mai de 2017

@author: alexsandrospecht
'''
import xml.etree.ElementTree as ET

class Conversor(object):
    
    def __init__(self, xml):
        self.xml = xml
        
    def converter(self):
        root = ET.parse(self.xml).getroot()
        
        exitFile = open("saida.txt","w") 
                                     
        for item in root:            
            for value in list(item):
                exitFile.write(value.tag + ',') 
            break
        
        exitFile.write('\n') 
        
        for reg in root:    
            lista = list(reg)
            for element in lista:
                exitFile.write(element.text + ',')
            exitFile.write('\n')     
            