import os

cmd = "attrib -h -r -s /s /d I:\*.*"

returned_value = os.system(cmd)
print('returned value:', returned_value)