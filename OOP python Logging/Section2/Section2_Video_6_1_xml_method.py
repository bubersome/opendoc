'''
Created on Jun 18, 2019
@author: Burkhard A. Meier
'''







import xml.etree.ElementTree as ET

 
class PythonClassXML(object):
    def __init__(self, name='default name', items=None):      
        self.name = name    
        self.items = items                        

    def xml(self):                                              # method to return data in XML
        pythonclass = ET.Element('pythonclass')                 # create Element
        name = ET.SubElement(pythonclass, 'name')               # add SubElement belonging to Element          
        name.text = self.name                                   # add attribute to the SubElement
        items = ET.SubElement(pythonclass, 'items')             # add SubElement belonging to Element
        items_dict = self.items                                 # save self.items under different name to avoid self.items.items()
        if items_dict:
            for key, value in items_dict.items():               # loop through (nested) dictionary
                an_item = ET.SubElement(items, str(key))        # add SubElement belonging to SubElement 
                an_item.text = str(value)                       # add attribute to the SubElement

        return pythonclass
    
    
    
    
    
    
    
    
    
    
    
