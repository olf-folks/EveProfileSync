import hashlib
import os
import shutil

# Function to compute the checksum of a file
def compute_checksum(file_path, hash_algo='sha256'):
    hash_func = hashlib.new(hash_algo)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Function to perform the checksum comparison and file copy
def sync_files(master_file_path, directory_path, file_pattern):
    # Compute checksum of the master file
    master_checksum = compute_checksum(master_file_path)

    # List all files in the directory
    for filename in os.listdir(directory_path):
        # Process files matching the pattern (e.g., core_user_*.dat or core_char_*.dat)
        if filename.startswith(file_pattern) and filename.endswith('.dat'):
            file_path = os.path.join(directory_path, filename)
            
            # Compute the checksum of the current file
            current_checksum = compute_checksum(file_path)
            
            # If checksums don't match, copy the master file to this location
            if current_checksum != master_checksum:
                print(f"Checksum mismatch for {filename}. Copying the master file.")
                shutil.copy(master_file_path, file_path)
            else:
                print(f"{filename} is already in sync with the master file.")

# Define your base directory and settings directory
base_directory = r'C:\Users\someone\AppData\Local\CCP\EVE\d_program_files_(x86)_eve_tq_tranquility'

# Ex: profile is named CloneFirmware
settings_directory = os.path.join(base_directory, 'settings_CloneFirmware')

# Paths to the master files
master_core_char = os.path.join(settings_directory, 'core_char_2120070626.dat')
master_core_user = os.path.join(settings_directory, 'core_user_26284228.dat')

# Sync the core_char files
sync_files(master_core_char, settings_directory, 'core_char_')

# Sync the core_user files
sync_files(master_core_user, settings_directory, 'core_user_')
