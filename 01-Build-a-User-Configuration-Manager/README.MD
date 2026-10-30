User Configuration Manager

This is a Python-based User Configuration Manager that allows users to manage system settings such as themes, languages, and notifications. The project primarily utilizes Python dictionaries and functions to handle data storage and manipulation.

Features

• Add Setting: Checks if a setting already exists in the dictionary. If it does, the function returns a message stating that it cannot overwrite an existing setting. If the setting is new, it adds it and returns a success message.
• Update Setting: Verifies whether a setting exists before modifying it. If the setting is found, it updates the value and returns a success message. If the setting does not exist, it alerts the user that the operation cannot be completed.
• Delete Setting: Checks for the existence of a setting in the dictionary. If found, it deletes the setting and returns a success message. If the setting is missing, it returns an error message stating the task is impossible.
• View Settings: Iterates through the dictionary to print all active settings to the screen. If the dictionary is empty, it outputs a message indicating that no settings are currently available.

Challenges Faced

When building this project, I initially struggled with how to access and manipulate key-value pairs inside a loop. After researching Python loops and dictionary methods, I learned how to use .items() to efficiently iterate over dictionaries.
