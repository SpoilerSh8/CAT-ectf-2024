
import os
import time

# Wait for 6 seconds
time.sleep(6)

# Command you want to run after waiting
command = "mv application_processor/ectf_params.h application_processor/inc/ectf_params.h"

# Run the command
os.system(command)