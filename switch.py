'''switch.py and testswitch.py are both licensed under the GLPv3
A copy should have been included with them (LICENSE.txt)
however if one was not provided you can read the full lincense at
http://opensource.org/licenses/gpl-3.0.html

copyright Lars Schweighauser, 2013
'''

class Switch():
    def __init__(self, goal):
        if goal == None:              #sets a goal of None, to False
            goal = False;             #because default uses None
        self.goal = goal; 

    def Case(self, x):
        self.x = x;
        if self.x == self.goal:       #checks the case 
            return True;              #against the goal
        return False;
                     #returns False if the check fails
    def Default():
        return True;
      
def switch(switchvalue):
    global case, default;
    current_switch = Switch(switchvalue);
    case = current_switch.Case;
    default = current_switch.Default;
    return True;

if __name__ == "__main__":

    while switch(54): 
        if case(2123):
            print("That's not 54.");
            break;
        if case(54):
            print ("That's the one.");

        if case("Hello"):
            print ("I'm looking for a number.");
            break;
        if default:
            print ("This is the default value.");
            break;
        break; 


