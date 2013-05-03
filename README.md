PySwitch
========

A simple module that adds the switch:case functionality to Python.  
To use:   
1) Import Switch from switch.py   
from switch import Switch

2) Next create a Switch object with the value you want to use.  
switchobj = Switch(x);

3) Then define the case keyword as switchobj.case for less typing.  
case = switchobj.case;

4) Finally make a while loop with True and write your code.   
while True:   
	if case(1):   
		do;   
		break;    
	if case(2):   
		do;   
		#don't break this time    
	if case(3):     
		do;   
		break;    
	if not case(None):    
		print("This is the default");  
		break;  
	break; #make sure to add an extra break, just in case.  
 
The source code itself contains an example of this. (minus the import statement.)   
 
