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
        
        file = open("saida.txt","w") 
               
#         for item in root.iter(root.tag):
#             print(item.attrib)
#         for item in root:
#             print(reg)
#             file.write(reg. + ',') 
        
        file.write('\n') 
        
        for reg in root:    
            lista = list(reg)
            for element in lista:
                file.write(element.text + ',') 
            file.write('\n')     
            