import os
import subprocess


files = os.listdir()

for file in files:
    try:
        with open(file, 'r') as f:
            orig_data = f.read()
        with open(file, 'w') as f:
            _ = f.write('r\'\'\'' + file + '\n')
            truncated_name = ' '.join(file.split('_')[2:])[:-3]
            _ = f.write(subprocess.check_output(['figlet', truncated_name]).decode())
            _ = f.write('\n\'\'\'')
            _ = f.write(orig_data)
    except IsADirectoryError as e:
    	pass
