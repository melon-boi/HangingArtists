import requests, os, warnings, time, pyperclip
from PIL import Image 
from pathlib import Path
from colorama import Fore

warnings.filterwarnings("ignore", category=DeprecationWarning) 

os.system("cls")
os.system("mode con: cols=90 lines=30")
os.system("title Hanging Artists │ made by melon boi")

print(f"""
{Fore.LIGHTMAGENTA_EX}
     _                       _                          _   _     _       
    | |__   __ _ _ __   __ _(_)_ __   __ _    __ _ _ __| |_(_)___| |_ ___   {Fore.RESET}v 1.0
    {Fore.MAGENTA}| '_ \ / _` | '_ \ / _` | | '_ \ / _` |  / _` | '__| __| / __| __/ __|
    | | | | (_| | | | | (_| | | | | | (_| | | (_| | |  | |_| \__ \ |_\__ \\
    |_| |_|\__,_|_| |_|\__, |_|_| |_|\__, |  \__,_|_|   \__|_|___/\__|___/
                       |___/         |___/                                

                {Fore.RESET}The Best & Free Starving Artists script!


""")

time.sleep(1.5)

image_url = input(f"{Fore.MAGENTA} > {Fore.RESET}Enter a square image link: ")
time.sleep(2)

print(f"{Fore.MAGENTA} > {Fore.RESET}Success! Generating Image..")

img_data = requests.get(image_url).content
with open('Script_Maker/Images/File.png', 'wb') as handler:
    handler.write(img_data)

my_file = Path("script_generated")



modifiedLine = "-- Ready for modifying line"
modifiedLine2 = "-- Waiting for art!"

x = 0 
y = 0 
counter = 0 

size = 32, 32

im = Image.open('Script_Maker/Images/File.png')
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save("Script_Maker/Images/File_resized.png", "PNG")
im.close()
im = Image.open('Script_Maker/Images/File_resized.png')

rgb_im = im.convert('RGB') 

open('Script_Maker/Sources/sample.txt', 'w').close()

for i in range(1, 1024): 
    r, g, b = rgb_im.getpixel((x,y)) 
    x += 1 
    counter += 1
    if x == 32: 
        y += 1
        x = 0
    Full_Data = {'R = ' f'{r}, G = ' f'{g}, B = ' f'{b}'}
    Full_Data2 = f"{{R = {r}, G = {g}, B = {b}}}"

    f = open("Script_Maker/Sources/sample.txt", "a")
    f.write(f"{Full_Data2}, ")
    f.close()


f = open('Script_Maker/Sources/sample.txt', 'r')
rgb_codes = f.read()
f.close()



f = open('Script_Maker/Sources/TheFunny.txt', 'r')
file_contents1 = f.read()
f.close()

f = open('Script_Maker/Sources/TheFunny2.txt', 'r')
file_contents2 = f.read()
f.close()

name = input(f"{Fore.MAGENTA} > {Fore.RESET}Script Generated! What would you like to call it? ")


weird_line = f"""ArtMakerSection:NewDropdown(\"Art\", \"Select art and it will Make It\", {{
    "{name}",
{modifiedLine}
    }},  function(option)"""



def makeScript():
    f = open("script_generated", "a")
    f.write(f"""

    {file_contents1}
    {weird_line}

        local data = {{}}
        data[\"{name}\"]={{{rgb_codes}}}
        {modifiedLine2}

    {file_contents2}


    """)

def add_to_script():
    with open('script_generated', 'r') as file :
        filedata = file.read()

    filedata = filedata.replace(modifiedLine, f"""    "{name}",
{modifiedLine}""")

    with open('script_generated', 'w') as file:
        file.write(filedata)


    with open('script_generated', 'r') as file :
        filedata = file.read()

    filedata = filedata.replace(modifiedLine2, f"""data[\"{name}\"]={{{rgb_codes}}}
        {modifiedLine2}""")

    with open('script_generated', 'w') as file:
        file.write(filedata)

    
if my_file.is_file():
    add_to_script()

else:
    makeScript()

with open('script_generated') as file:
    clipboard = file.read()
    
pyperclip.copy(clipboard)
print(f"{Fore.MAGENTA} > {Fore.RESET} Successfully created! Script copied to clipboard.")
