
import os
import time

# Wait for 6 seconds
time.sleep(6)

# Command you want to run after waiting
command = "mv component/ectf_params.h component/inc/ectf_params.h"

# Run the command
os.system(command)