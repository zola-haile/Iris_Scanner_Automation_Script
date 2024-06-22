Iris Scanner Automation Script
This project contains a Python script to automate interactions with the IriTech IDDK-2000 Iris Scanner demo application using the pexpect library. The script repeatedly runs the iris capturing process and handles various prompts and configurations required by the application.
Prerequisites
Python 3.x
pexpect library
Installation
Install Python 3.x from the official Python website.
Install pexpectusing pip:
sh
Copy code
pip install pexpect
Setup
Ensure the IriTech IDDK-2000 Iris Scanner software is installed at the specified location (/opt/IriTech/IDDK-2000-3.3.1-OSX/demo/source). Update the DYLD_LIBRARY_PATH environment variable as shown in the script.
Usage
Clone the repository or download the script to your local machine.
Run the script:
sh
Copy code
python script_name.py
Replacescript_name.py with the name of your script file.
Script Details
Environment Setup: The DYLD_LIBRARY_PATH environment variable is set to include the IriTech demo software directory.
Process Automation: The script uses pexpect to interact with the IriTech demo application. It simulates user inputs for various configuration prompts and options.
Looping: The script runs in a loop to continuously capture iris images. It handles errors and reattempts the capture process as needed.
Logging: Interaction logs are written to pexpect.log.
Output: The captured iris image is moved to a specified directory (/Users/czajkademo1/Desktop/pyDemo/LeftEye.jp2).
Script Flow
Start the IriTech demo application:
python
Copy code
child = pexpect.spawn(executable)
Interact with the application prompts: The script sends appropriate inputs to each prompt.
Capture Process: Handles the entire capturing process including retries in case of errors.
Save Image: The captured image is saved and moved to the specified directory.
Continue or Quit: The script prompts the user to continue or quit after each capture cycle.
Customization
Update the executable path if your IriTech software is installed in a different location.
Modify the output path for the captured images as needed.
Troubleshooting
Ensure the IriTech software is correctly installed and the executable path is accurate.
Check the pexpect.log file for detailed logs of the interaction with the IriTech demo application.
Ensure Python and pexpect are correctly installed and configured on your system.
