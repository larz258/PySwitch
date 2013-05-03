class Switch():
  def __init__(self, goal):
    if goal == None:            #sets a goal of None, to False
      goal = False;             #because default uses None
    self.goal = goal; 

  def case(self, x):
    self.x = x;
    if self.x == self.goal:     #checks the case 
      return True;              #against the goal
    return False;               #returns False if the check fails

if __name__ == "__main__":      #Doesn't execute this code when imported.
  MySwitch = Switch(54);        #creates a Switch object 
  case = MySwitch.case;         #creates a case keyword to minimize the amount of typing needed later.

  while True:                   #Creates an infinite loop so that you can break the cases. 
    if case(2123):              #checks the case
      print("That's not 54.");  #does some code
      break;                    #breaks the loop ending the check
    if case(54):
      print ("That's the one.");
                                #this does not break, allowing for multiple cases to be activated.
    if case("Hello"):
      print ("I'm looking for a number.");
      break;
    if not case(None):                          #The default case checks against a value
      print ("This is the default value you."); #that will always return False. The 'not' makes
      break;                                    #that False become True.
    break;                                      #This break is incase no other cases activate. 
                                                #Although the default should always activate, that is only if
                                                #someone bothers to write a default. 
