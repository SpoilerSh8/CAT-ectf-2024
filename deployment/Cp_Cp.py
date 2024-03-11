
import os
import time
print('hello COMP')

# Wait for 10 seconds
time.sleep(10)

# Command you want to run after waiting
command = "mv component/ectf_params.h component/inc/ectf_params.h"

# Run the command
os.system(command)