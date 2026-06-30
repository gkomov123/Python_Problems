# Write a function that merges two dictionaries. If a key 
# exists in both dictionaries, sum their values. If a key exists in only one, include it as is.

def merge_dict(d1: dict, d2: dict) -> dict:
    result = d1.copy()

    # .get(key,0) returns 0 if the key doesn't exist yet
    for key, value in d2.items():
        result[key] = result.get(key,0) + value
    
    return result


dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

print(merge_dict(dict_a, dict_b))