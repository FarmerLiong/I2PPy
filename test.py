from inspect import getmembers, isfunction

import sys
print(getmembers(sys, isfunction))