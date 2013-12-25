import builtins
class Switch():
    def __init__(self, goal):                   # goal is the value to be checked against.
        self.goal = goal 

    def Case(self, to_check, code, set_state):                   # case checks it's argument against the goal.
        if state:
            if to_check == self.goal:
                if set_state == 0:
                    return exec(code)
                if set_state == 1:
                    builtins.state = False
                    return exec(code)

    def Default(self, code, set_state):
        if state:
            if set_state == 0:
                return exec(code)

            if set_state == 1:
                builtins.state = False
                return exec(code)

def switch(switch_target):                       
    try: del current_switch                     # deletes any already existing switch object.
    except NameError: pass
    current_switch = Switch(switch_target)      # creates a Switch object with switch_target as the goal.
    builtins.case = current_switch.Case         # adds the case function to builtins. 
    builtins.default = current_switch.Default   # adds the default function to builtins.
    builtins.state = True                             
                                                # while switch(arg):
