def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    #pass  # implement me

    dict = {}

    for key, value in zip(keys, values):
        dict[key] = value
    return dict


def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    #pass  # implement me

    # d3 = {**d1, **d2}
    # return d3
    d3 = d1.copy()
    d3.update(d2)
    return d3

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    #
    #pass  # implement me
    return dict.fromkeys(lst, d1)

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    pass  # implement me
    result_dict = {}
    for key, value  in datadict.items():
        if key in keylist:
            result_dict[key] = value
    return  result_dict


def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    #pass
    for key in keylist:
        if key in datadict:
            del datadict[key]
    return datadict

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    #pass
    #('val1' in d.values())
    # if datadict.get('key') in datadict:
    #     return True
    # else:
    #     return False

    return key in datadict or key in datadict.values();
    #return datadict.get(key) == value


def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    #pass
    return min(ddd, key = ddd.get)

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    #pass
    return max(ddd, key = ddd.get)