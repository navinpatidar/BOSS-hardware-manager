#!/usr/bin/python

<<<<<<< HEAD
from xml.dom.minidom import parse
import re
class xml_parser():
   def __init__(self,path):
      self.path=path
      dom=parse(self.path)
      first_node=dom.getElementsByTagName("node")[0]
      first_node_key=(first_node.attributes["id"].value,first_node.attributes["class"].value,first_node.attributes["handle"].value)
      self.first_node_key=first_node_key
      node_info={}
      i=-1	
      for node in dom.getElementsByTagName("node"):
    	 temp={}
	 node_id=(node.attributes["id"].value,node.attributes["class"].value,node.attributes["handle"].value)
	 node_list=[]
	 i+=1
	 for n in node.childNodes:
            if n.nodeType == n.ELEMENT_NODE:
               if n.nodeName=="configuration":
	           con={}
		   for j in n.childNodes:
			try:
			   con[j.attributes["id"].value]=j.attributes["value"].value
			except TypeError :
			   pass
		   temp[n.nodeName]=con
			
               elif n.nodeName== "capabilities" :
	          cap=[]
	          for j in n.childNodes:
			try:
		        	cap.append(j.toprettyxml().split("\n")[1].split("\t")[1])
			except IndexError :
				pass
		    
		     
		  temp[n.nodeName]=cap
	       elif n.nodeName=="resources":
		   res={}
		   for j in n.childNodes:
			#print j.toprettyxml().split('"')[1].split(';')
			try:
			   tem=j.toprettyxml().split('"')[1].split(';')
			   res[tem[0].split("&")[0]]=tem[2]
			except IndexError:
			   pass
		   temp[n.nodeName]=res  
	       elif n.nodeName=="node":
	          node_list.append((n.attributes["id"].value,n.attributes["class"].value,n.attributes["handle"].value))
	       else:
	          temp[n.nodeName]= n.toprettyxml().split("\n")[1].split("\t")[1]
	          #print " "*i,n.nodeName,":",value
            
         else:
            temp["child_nodes"]=node_list
	    node_info[node_id]=temp
      self.hw_info=node_info



=======
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

		
>>>>>>> 45d4cf71f811309a843c810f6a28cba498ab3903
