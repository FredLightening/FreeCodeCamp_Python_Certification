This is a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications using python. I implemented functions to add, update,delete and view user settings.

The scope of this project uses dictionaries and functions majorly to complete the tasks: 

The add function checks if the setting you want to add is already in the settings dictionary and returns a message telling you that it cannot add an already existing setting. It also returns a message of success if the setting was successfully added.
The update function checks if the setting you want to update is in the settings dictionary and updates it if it is there and returns a message stating it cannot be done if the setting is not in the dictionary. It also returns a success message if the setting is successfully.
The delete function checks if the setting is in the setting dictionary and deletes it if it is there but if the setting is not in the dictionary, then the setting does not delete but returns a message signifying impossibility of the task asked. It also returns a message of success to signify the deletion of the setting. 
The view function checks if the dictionary has any settings in it and prints out the settings unto the screen and if there is not any setting in the dictionary, the function prints a message signalling an empty dictionary.

Challenges faced:
At the time I was writing this code, I did not know about how key value pairs can be used in a for loop so I had to research on for loops and how to iterate over a dictionary.
