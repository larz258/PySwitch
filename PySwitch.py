'''PySwitch.py is licensed under the GLPv3
A copy should have been included with it (LICENSE),
however if one was not provided you can read the full lincense at
http://opensource.org/licenses/gpl-3.0.html

copyright Lars Schweighauser, 2013
'''
import builtins
class Switch():
    def __init__(self, goal):
        if goal == None:
            goal = False;
        self.goal = goal; 

    def Case(self, x):
        self.x = x;
        if self.x == self.goal: 
            return True;
        return False;

    def Default():
        return True;

def switch(switchvalue):
    current_switch = Switch(switchvalue);
    builtins.case = current_switch.Case;
    builtins.default = current_switch.Default;
    return True;
