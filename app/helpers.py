import os

def get_first_match_or_none(cmd):
    found = False
    output = ""
    paths = os.environ["PATH"].split(os.pathsep)
    for path in paths:
        full = f"{path}{os.sep}{cmd}"
        if os.access(full, os.X_OK):
            found = True
            output = full
    if found:
        return output
    else:
        return None

def is_executable(cmd):
    return (get_first_match_or_none(cmd) != None)
