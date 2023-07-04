import subprocess
import re

def printing(PATH_TO_IMG, q):
    # Create a connection to the CUPS server
    string = PATH_TO_IMG
    pattern = r"result_print(\d{4}-\d{2}-\d{2})"

    match = re.search(pattern, string)
    
    print(match)

    # subprocess.run("cd /Users/dogg/vs_code/PHOTO/static/image", shell=True)
    
    replaced_string = PATH_TO_IMG[19:].replace(" ", "\ ")

    command = 'cd /Users/dogg/vs_code/PHOTO/static/image; lp -d Canon_SELPHY_CP1500 -o media=Custom.100x148mm -o borderless=True '+replaced_string

    print(command)
    for i in range(q):
        subprocess.run(command, shell=True)
        pass
    
    subprocess.run("cd ..", shell=True)
    subprocess.run("cd ..", shell=True)


    
