
import os
import time

# Wait for 0.3 seconds
time.sleep(0.3)

# Command you want to run after waiting
command = "mv component/ectf_params.h component/inc/ectf_params.h"

# Run the command
os.system(command)