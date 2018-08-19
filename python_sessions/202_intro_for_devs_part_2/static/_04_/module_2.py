import os
import sys


template = '''
Module 2 can be accessed from Module 1. This is because:

{directory}

... was automatically added to the path when Module 1 was executed directly
from the interpreter. The PYTHONPATH list would therefore be:

{python_path}

... and the contents of that folder are:

{contents}

... so Module 2 is visible on the PYTHONPATH to Module 1.

'''

filled_template = template.format(
    directory=os.path.abspath(sys.path[0]),
    python_path='\n'.join(sys.path),
    contents='\n'.join(os.listdir(os.path.abspath(sys.path[0])))
)

print(filled_template)
