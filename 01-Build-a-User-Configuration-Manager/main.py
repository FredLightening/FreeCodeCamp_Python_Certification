test_settings={'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

def add_setting(setting_dict,kv_tup):

    key=kv_tup[0].lower()
    value=kv_tup[1].lower()
    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting_dict[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting_dict,kv_tup):
    key=kv_tup[0].lower()
    value=kv_tup[1].lower()
    if key in setting_dict:
        setting_dict[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        # setting_dict[key]=value
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting_dict,KEY):
    key=KEY.lower()
    # value=kv_tup[1].lower()
    if key in setting_dict:
        del setting_dict[key]
        # print(setting_dict)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(setting_dict):
    new_setting_dict=""

    for KEY,value in setting_dict.items():
        key=KEY.capitalize()
        kv=f'{key}: {value}\n'
        new_setting_dict+=kv

    if not setting_dict:
        return "No settings available."
    else:
        return f"Current User Settings:\n{new_setting_dict}"

print(view_settings(test_settings))
