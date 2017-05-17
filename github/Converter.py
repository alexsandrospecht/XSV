'''
Created on 16 de mai de 2017

@author: alexsandrospecht
'''
import xml.etree.ElementTree as ET

class Converter(object):
    
    def __init__(self, xml):
        self.xml = xml
        
    def converter(self):
        root = ET.fromstring(self.xml)
        
        for reg in root:
            lista = list(reg)
            for element in lista:
                print(element.tag, element.text)
