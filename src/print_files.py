

import os
from sys import argv


if __name__ == "__main__":
    
    errmsg = f"Usage: python {argv[0]} <target> <directory>" 
    
    if len(argv) < len(errmsg.split(" ")[2:]):
        exit( errmsg )

    target = argv[1]
    targetdir = argv[2]

    orgdir = os.getcwd() 
    
    try:
        os.chdir( targetdir )
    except Exception as e:
        exit(e)

    assert os.getcwd != orgdir, f"Didn't go through with changing directory. "
    
    for dirpath, dirnames, filenames in os.walk( os.getcwd() ):
        if target not in filenames:
            continue

        filepath = os.path.join(dirpath, target)

        with open(filepath, "r") as f:
            txt = f.read()

            print(txt)

            if "NOT PASSED" in txt:
                print( f"NOT PASSED in {filepath}" )

            if input( f"At file: {filepath} \nCont.? (n) " ) == "n":
                break

        print("\n", "#" * 64)
    
    os.chdir( orgdir )
