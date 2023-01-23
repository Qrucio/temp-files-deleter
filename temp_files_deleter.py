import os
import shutil
import time

# Timeout in seconds
timeout = 5


# Define the paths to be deleted
paths = ["C:\\Users\\"+os.getlogin()+"\\AppData\\Local\\Temp", "C:\\Windows\\Temp", "C:\\Windows\\Prefetch"]

# Initialize a counter for the number of files that couldn't be deleted
failed_deletes = 0

# Iterate over the paths
for path in paths:
    # Check if the path exists
    if os.path.exists(path):
        # Iterate over the files and folders in the path
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                # Increment the counter
                failed_deletes += 1
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    else:
        print(f'{path} does not exist')

# Print the number of files that couldn't be deleted
print(f"\nNumber of files that couldn't be deleted: {failed_deletes}")
time.sleep(timeout)
