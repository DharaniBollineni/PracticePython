#commandline Parameters

'''
it is possible to pass the arguments to python programs when they are executed.
use()
.argv refers to the number of arguments passed and argv[] is a pointer array which points to each argument which is passed to main
the python sys module provides access to any command-line arguments via the sys.argv. this serves
two purposes:
-sys.argv is the list of command-line arguments
-len(sys.argv) is the number of command-line arguments
'''

import sys
print(len(sys.argv))
print(sys.argv)
