
import os
import time

print('hello AP')
# Wait for 10 seconds
time.sleep(10)

# Command you want to run after waiting
command = "mv application_processor/ectf_params.h application_processor/inc/ectf_params.h"

# Run the command
os.system(command)