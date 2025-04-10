#installation of  external modules
# External modules are modules that are not included with Python by default and need to be installed separately.

# You can install external modules using pip, the package manager for Python.

# install pijokes module
# pip install pijokes

# import the module
import pyjokes as j #pyjokes is an external module that provides a collection of jokes.
joke = j.get_joke()
print("Joke:", joke)
