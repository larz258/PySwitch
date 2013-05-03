'''switch.py and testswitch.py are both licensed under the GLPv3
A copy should have been included with them (LICENSE.txt)
however if one was not provided you can read the full lincense at
http://opensource.org/licenses/gpl-3.0.html

copyright Lars Schweighauser, 2013
'''

from random import randrange;
class Switch():
    def __init__(self, goal):
        if goal == None:              #sets a goal of None, to False
            goal = False;             #because default uses None
        self.goal = goal;

    def case(self, x):
        self.x = x;
        if self.x == self.goal:       #checks the case 
            return True;              #against the goal
        return False;                 #returns False if the check fails
def build(switchname, switchvalue):
    switchname = Switch(switchvalue);
    return switchname, switchname.case;

class SwitchTester():

    def test_output(self):
        Hello = Switch(None);
        for i in range(100000):
            Hello.goal = randrange(1, 4324324785487234234234);
            if Hello.case(Hello.goal) == True:
                print("Test passed: Input %s equals the expected input %s and the output was True." %(Hello.goal, Hello.goal));
            else:
                print("Test failed.")


if __name__ == '__main__':
    test = SwitchTester();
    test.test_output();
