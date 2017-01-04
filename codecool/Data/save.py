import sys
print("modules will be searched in the following paths:")
for path in sys.path:
    print(path)
print("python version: " + sys.version)