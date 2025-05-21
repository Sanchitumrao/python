#String searching functions
print("Hello! Python".find("Python"))# .find(substring) returns the lowest index of the substring if found, otherwise -1.
print("Hello! Python".rfind("Python"))# .rfind(substring) returns the highest index of the substring if found, otherwise -1.
print("Hello! Python".index("Python"))# .index(substring) returns the lowest index of the substring if found, otherwise raises ValueError.
print("Hello! Python".rindex("Python"))# .rindex(substring) returns the highest index of the substring if found, otherwise raises ValueError.
print("Banana".count("a"))# .count(substring) returns the number of occurrences of the substring in the string.
print("Banana Papaya".count("a", 0, 5))# .count(substring, start, end) returns the number of occurrences of the substring in the string between start and end.

# string splitting and joining functions


print("Hello! Python".split())# .split() splits the string into a list of substrings based on whitespace by default.
print("Hello! Python".split("!"))# .split(separator) splits the string into a list of substrings based on the specified separator.
print("Hello! Python Developer".split(" ", 1))# .split(separator, maxsplit) splits the string into a list of substrings based on the specified separator, with a maximum number of splits.
print("hello world".split()) # ["hello", "world"]

print("-".join(["Hello", "Python"]))# .join(iterable) joins the elements of the iterable into a single string, using the string as a separator.

# string formatting functions

print("Hello! {}".format("Python"))# .format() formats the string using the specified values.
print("Hello! {0} {1}".format("Python", "Developer"))# .format() formats the string using the specified values with positional arguments.
print("Hello! {name} {age}".format(name="Sanchit", age=20))# .format() formats the string using the specified values with keyword arguments.
print("Pi= {0:.2f}".format(3.14159))# .format() formats the string using the specified values with formatting options.

name = "John"
f"Hello, {name}"  # "Hello, John"
print(f"Hello, {name}")# f-string formatting
print(f"Hello, {name.upper()}")# f-string formatting with method call
