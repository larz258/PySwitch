import builtins
class Switch():
    def __init__(self, goal):                   
        self.goal = goal 

    def Case(self, to_check, code, set_state=1):
        if state:
            if to_check == self.goal:
                if set_state == 0:
                    return exec(code)
                if set_state == 1:
                    builtins.state = False
                    return exec(code)

    def Default(self, code):
        if state:
            return exec(code)

def switch(switch_target):                       
    try: del current_switch                    
    except NameError: pass
    current_switch = Switch(switch_target)
    builtins.case = current_switch.Case
    builtins.default = current_switch.Default
    builtins.state = True                             

