def strings_to_lengths(string_list):
    return {s: len(s) for s in string_list}


strings = ["apple", "banana", "cherry"]
lengths = strings_to_lengths(strings)
print(lengths)
