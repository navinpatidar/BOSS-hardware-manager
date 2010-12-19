#!/usr/bin/python

from  xml.dom.minidom import parse
import re 
class xml_parser:
	def __init__(self,path):
		self.path=path
		dom=parse(self.path)
		i=0
		for node in   dom.getElementsByTagName("node"):
    			 
    			 for n in node.childNodes:
				 if n.nodeType == n.ELEMENT_NODE:
				    t=re.compile(r'<.*?>(\w*)')
				    value = t.match(n.toxml()).group(1)
				    #print n.toxml()
				    print " "*i,n.nodeName,":",value
            			    
    			 else:
            			 i=i+1
		


xml_parser("./resources/hw.xml")

		
