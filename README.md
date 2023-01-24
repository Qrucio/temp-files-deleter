# Temporary Files Deleter

This program is designed to delete all **unnecessary temporary files** from your computer. It will delete files from the following directories:

• temp 

• %temp%

• prefetch

## Usage

- Make sure you have Python installed on your computer. You can download it from [here](https://www.python.org/downloads/)
- Clone or download this repository
- Run the **Temp Files Deleter.exe** file or open command prompt and run the **temp_files_deleter.py** file
- The program will display the number of files that couldn't be deleted after it's done.

# Note
- This program uses os.getlogin() which may not work on all systems, and you should use an alternative method to get the username if it's not working on your system.
- Please make sure that you are running the script with admin privileges, as the prefetch folder is a protected folder and requires admin permissions.

# Additional Information

- The script automatically fetches the paths from the user's computer and specifies the "temp" folder, "%temp%" folder, and "prefetch" folder as the paths to be deleted.
- It will close after 5 seconds
- If you want to change the time before the program closes, you can change the value of the timeout variable in the script.
