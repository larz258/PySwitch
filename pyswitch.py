'''PySwitch.py is licensed under the GLPv3
A copy should have been included with it (LICENSE),
however if one was not provided you can read the full lincense at
http://opensource.org/licenses/gpl-3.0.html

copyright Lars Schweighauser, 2013
'''
import builtins
class Switch():
    def __init__(self, goal):                   # goal is the value to be checked against.
        self.goal = goal 

    def Case(self, to_check):                   # case checks it's argument against the goal.
        if to_check == self.goal: 
            return True
        return False

    def Default():                              # takes no arguments and always returns true. Because the default case
        return True                             # should always execute if no other case has.

def switch(switch_target):                       
    try: del current_switch                     # deletes any already existing switch object.
    except NameError: pass
    current_switch = Switch(switch_target)      # creates a Switch object with switch_target as the goal.
    builtins.case = current_switch.Case         # adds the case function to builtins. 
    builtins.default = current_switch.Default   # adds the default function to builtins.
    return True                                 # returning true creates a quick loop when you write 
                                                # while switch(arg):
