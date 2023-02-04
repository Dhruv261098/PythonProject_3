# subprocess library: Allow our python script to interect with the CLI or shell, It have many fanctions.

import subprocess

# we are using check_call function here
# The parameter of chech_call funtion is depend upon what we want to execute in command line,
# each element in the list represent the argument in the command
# first element python3 and second is example.py as we want to run that program.

subprocess.check_call(['python','Example.py'])



