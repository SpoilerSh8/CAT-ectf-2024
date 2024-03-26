
import os
import time

# Wait for 03 seconds
time.sleep(0.3)

# Command you want to run after waiting
command = "mv application_processor/ectf_params.h application_processor/inc/ectf_params.h; mv save_directory/public.pem application_processor/src/public.pem; mv save_directory/signature.bin application_processor/src/signature.bin"

# Run the command
os.system(command)