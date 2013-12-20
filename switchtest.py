from PySwitch import switch

while switch(54):                      # sets the value to check against and creates the case and the default functions. 
    if case(2123):
        print("That's not 54.");       
        break;
    if case(54):
        print ("That's the one.");
                                       # no break here allows for the default to execute too.
    if case("Hello"):
        print ("I'm looking for a number.");
        break;
    if default:
        print ("This is the default value.");
        break;
