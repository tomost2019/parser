# SETTINGS.
# You can change some settings for the script below. See the comments for each of them. 

# Logfile mode.
logfile_mode = "r"
# Text for instructions.
instructions = '\nWhich data would you like to see? Type below for the correct action.\n\n1) Type "statistics" or "stats" to show statistics for errors and notice.\n2) Type "errors" to show details about errors.\n3) Type "notice" to show details about notice.\n'

# SCRIPT BEGINS.
# Do not change anything below here. Change the settings in the variables above instead. 

# Input for the logfile path. 
print("\nType filepath:\n")
logfile_path = input()

# With statement open the logfile path with the chosen mode. No need to close the file within with statement. 
# Convert the data into proper data structure.
# Converts from string > list > dictionaries within the list. Loop through the list to extract the dicationaries. 
# Add custom error handlers with the try statement. 
# Takes the user input for the program. 
try:
    with open(logfile_path, logfile_mode) as file:
        all_data = []
        dict_keys = ["date", "type", "message"]
        for all in file:
            dict_values = all.split("] ")
            dict_values = [rm.replace("[", "") for rm in dict_values]
            dict_structure = {key:value for key, value in zip(dict_keys, dict_values)}
            all_data.append(dict_structure)
        print(instructions)
        user_input = input().lower()
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

# Executes each input chosen by the user in the program. 
if user_input == "statistics" or user_input == "stats":
    print("\nerrors:", count_errors())
    print("\nnotice:", count_notice(), "\n")
elif user_input == "errors":
    for dict_data in all_data:
        if dict_data['type'] == "error":
            print("\n", dict_data['date'], dict_data['message'])
elif user_input == "notice":
    for dict_data in all_data:
        if dict_data['type'] == "notice":
            print("\n", dict_data['date'], dict_data['message'])
else:
    print("\nNo valid option\n")