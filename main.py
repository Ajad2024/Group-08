import sys
import ifcopenshell
sys.path.append('path_to_rules_directory')

from rules import windowRule
from rules import doorRule
from rules import doorType
from rules import numberofDoor

model = ifcopenshell.open("D:/BIM/CES_BLD_24_06_ARC.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)
doorTypeResult= doorType.checkRule(model)
numberofDoorResult = numberofDoor.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
print("Door Type result:", doorTypeResult)
print("Door result:", numberofDoorResult)
