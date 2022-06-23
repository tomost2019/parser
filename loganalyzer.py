import sys

# SETTINGS.
# You can change some settings for the script below. See the comments for each of them. 

# Logfile mode.
logfile_mode = "r"

# SCRIPT BEGINS.
# Do not change anything below here. Change the settings in the variables above instead. 

# Input for the logfile path and action from the command line. 
logfile_path = sys.argv[1]
user_input = sys.argv[2]

# With statement open the logfile path with the chosen mode. No need to close the file within with statement. 
# Convert the data into proper data structure.
# Converts from string > list > dictionaries within the list. Loop through the list to extract the dicationaries. 
# Add custom error handlers with the try statement. 

try:
    with open(logfile_path, logfile_mode, encoding='utf-8') as file:
        all_data = []
        dict_keys = ["date", "type", "message"]
        for all in file:
            dict_values = all.split("] ")
            dict_values = [rm.replace("[", "") for rm in dict_values]
            dict_structure = {key:value for key, value in zip(dict_keys, dict_values)}
            all_data.append(dict_structure)
except FileNotFoundError:
    print("\nThe file does not exist.\n")
    exit()
except PermissionError:
    print("\nYou don't have the permission to open the file.\n")
    exit()
except Exception:
    print("\nUnexpected error occured.\n")
    exit()

# Function for counting the errors in the dictionaries. 
def count_errors():
    count = 0
    for dict_data in all_data:
        if dict_data['type'] == "error":
            count = count + 1
    return count

# Function for counting the notice in the dictionaries. 
def count_notice():
    count = 0
    for dict_data in all_data:
        if dict_data['type'] == "notice":
            count = count + 1
    return count

# Executes each input depending on the action from the command line. 
if user_input == "statistics":
    print("\nerror:", count_errors())
    print("\nnotice:", count_notice(), "\n")
elif user_input == "error":
    for dict_data in all_data:
        if dict_data['type'] == "error":
            print("\n", dict_data['date'], dict_data['message'])
elif user_input == "notice":
    for dict_data in all_data:
        if dict_data['type'] == "notice":
            print("\n", dict_data['date'], dict_data['message'])
else:
    print("\nNo valid option\n")