from genericpath import isfile
import os
def find_files(suffix, path):
    listFound = []
    if os.path.isfile(path) and path.endswith(".c"):
        listFound.append(path)
        return listFound
    elif os.path.isfile(path) andgit  not path.endswith(".c"):
        return listFound
        
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return None