File Sync Script:
This Python script synchronizes files in a target directory with a master file by comparing their checksums. If the checksum of a file does not match the checksum of the master file, it replaces the outdated file with the master file.

Requirements:
Python 3.6 or higher
Basic understanding of file paths and directories

Installation:
Make sure Python is installed on your system.(windows 10 and up Win+R , type: cmd , ENTER , type: python, enter | python will install automaticly from win store)
download the .py file to your desktop

Setup:
Before running the script, you'll need to modify the paths and file names to match your system's configuration.

Target Directory:
Define the directory where the files to be synced are located.

Update the Script:
In the script, locate and modify the following variables:

base_directory:
The base directory where your target files are stored.
settings_directory: The specific subdirectory containing the files you want to sync (e.g., settings_CloneFirmware).
master_core_char: The path to the master character file (e.g., core_char_2120070626.dat).
master_core_user: The path to the master user file (e.g., core_user_26284228.dat).

# Base directory and settings directory(Both of these will need to be set to your settings directory and your profile, unless you make a profile called CloneFirmware)

base_directory = r'C:\Users\someone\AppData\Local\CCP\EVE\c_program_files_(x86)_eve_tq_tranquility'

# Profile name, ex: if your profile is CloneFirmware
settings_directory = os.path.join(base_directory, 'settings_CloneFirmware')

# Paths to the master files, the numbers are the EVE id of your account and charictor you want to be the master for sync
master_core_char = os.path.join(settings_directory, 'core_char_2120070626.dat')
master_core_user = os.path.join(settings_directory, 'core_user_26284228.dat')

How It Works
1. Checksum Calculation
The script computes the checksum of each file (using SHA-256 by default) in the target directory and compares it to the checksum of the master file.

2. File Synchronization
If a file’s checksum does not match the master file's checksum, the script replaces the file with the master file.
If the checksums are the same, the script will confirm that the file is already in sync and do nothing.
3. File Matching
The script looks for files in the target directory that match the following patterns:

Files starting with core_char_ (for character-related files).
Files starting with core_user_ (for user-related files).
Files must also have a .dat extension.

Running the Script:

click on it on your desktop


Example Output:
Checksum mismatch for core_char_123456.dat. Copying the master file.
core_char_123456.dat is already in sync with the master file.
Checksum mismatch for core_user_987654.dat. Copying the master file.

Troubleshooting
Permission Issues: Ensure the script has permission to read from and write to the target directory and master files.
File Not Found: Double-check that all file paths are correct and that the files exist at those locations.
