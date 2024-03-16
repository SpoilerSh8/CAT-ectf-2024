
import os
import time

# Wait for 0.5 seconds
time.sleep(0.5)

# Command you want to run after waiting
command = "mv application_processor/ectf_params.h application_processor/inc/ectf_params.h"

# Run the command
os.system(command)