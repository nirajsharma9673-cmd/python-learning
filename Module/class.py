# import calc (normally) for call calc.add()
import calc as c # to give module a alias name 
#from calc import add,sub 
#from calc import * (for all function)
#from calc import add as a (giving alias name to function )
c.add(1,5,6)
c.sub(10,20)
c.mult(56,56,89)
c.div(8956,5698)

# for calling variable or data types
from calc import creator as c
print(c)