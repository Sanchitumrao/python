name="sanchit"
print("length of name:",len(name))

# string checking methods(functions)

print(name.endswith("it")) # .endswith(substring) returns True if the string ends with the specified substring, otherwise False.
print(name.startswith("it"))# .startswith(substring) returns True if the string starts with the specified substring, otherwise False.
print(name.isalnum())# .isalnum() returns True if all characters in the string are alphanumeric (letters and numbers), otherwise False.
print(name.isalpha())# .isalpha() returns True if all characters in the string are alphabetic (letters), otherwise False.
print(name.isdigit())# .isdigit() returns True if all characters in the string are digits (numbers), otherwise False.
print(name.islower())# .islower() returns True if all characters in the string are lowercase, otherwise False.
print(name.isupper())# .isupper() returns True if all characters in the string are uppercase, otherwise False.
print(name.isspace())# .isspace() returns True if all characters in the string are whitespace, otherwise False.
print(name.isnumeric())# .isnumeric() returns True if all characters in the string are numeric, otherwise False.
print(name.isidentifier())# .isidentifier() returns True if the string is a valid identifier (variable name), otherwise False.
print(name.isprintable())# .isprintable() returns True if all characters in the string are printable, otherwise False.
print(name.isdecimal())# .isdecimal() returns True if all characters in the string are decimal characters, otherwise False.
print(name.isascii())# .isascii() returns True if all characters in the string are ASCII characters, otherwise False.




# string modification methods

print(name.capitalize()) # .capitalize() returns a copy of the string with the first character capitalized and the rest lowercased.
print(name.upper())# .upper() returns a copy of the string with all characters converted to uppercase.
print(name.lower())# .lower() returns a copy of the string with all characters converted to lowercase.
print(name.title())# .title() returns a copy of the string with the first character of each word capitalized.
print(name.swapcase())# .swapcase() returns a copy of the string with uppercase characters converted to lowercase and vice versa.
print("  Hello! Python".strip())# .strip() returns a copy of the string with leading and trailing whitespace removed.
print(name.replace("sanchit","Hello! Sanchit"))# .replace(old, new) returns a copy of the string with all occurrences of the substring old replaced by new.
