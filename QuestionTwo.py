

import os
def find_files(suffix, path):
  
    found = []
    if os.path.isdir(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)) and file.endswith(suffix):

                found.append(file)
            if os.path.isdir(os.path.join(path, file)):
                found.extend(find_files(suffix, os.path.join(path, file)))

    return found
    
print(find_files(".c", ".testdir1"))
print(find_files("cheese", ".md"))
