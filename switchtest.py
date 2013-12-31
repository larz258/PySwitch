from pyswitch import switch
switch(54)
case(2123, '''
print("That\'s not 54.")
''')
case(54, '''
print ("That\'s the one.")
''', 0)

case("Hello", '''
print ("I\'m looking for a number")
''')
default('''
print("This is the default value")'''
)
