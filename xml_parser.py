#!/usr/bin/python

from xml.dom.minidom import parse
import re
class xml_parser:
     def __init__(self,path):
	self.path=path
	dom=parse(self.path)
	i=0
	node_info={}
	t=re.compile(r'<.*?>([-\.\w]*)')

	for node in dom.getElementsByTagName("node"):
    		temp={}
		id=node.attributes["id"].value
		#print id
     		for n in node.childNodes:
			if n.nodeType == n.ELEMENT_NODE:
			   if n.nodeName=="configuration":
				pass 
			   elif n.nodeName== "capabilities" :
			         cap=[]
			         for j in n.childNodes:
					 #print j.toxml()
					# print t.match(j.toxml())
					cap.append(t.match(j.toxml()).group(1))
					 #i.attributes["id"].value
					pass
			         temp[n.nodeName]=cap
			   elif n.nodeName=="node":
				 pass
			   else:
			#	t=re.compile(r'<.*?>(\w*)')
				value = t.match(n.toxml()).group(1)
				temp[n.nodeName]=value
			#	print " "*i,n.nodeName,":",value
            
     		else:
			i=i+1
		node_info[id]=temp
	print node_info


xml_parser("./resources/hw.xml")


