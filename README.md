# Lyrics
A app built on python that takes two inputs and merges them to give proper Lyrics

## How to install the modules used in building this app are:
1. Kivy => pip install kivi
2. Pyperclip => pip install pyperclip
3. Pyinstaller => pip install pyinstaller

## Python script to .exe
Use **pyinstaller**, *nuitka doesn't do well* with kivy gui, and make sure while converting you **do not make a standalone**, that's complex in nature, in this I kept it simple, the 2 following commands are to be run.
> pyinstaller "main.py" -w --icon=logo.png
- Now after this go to the "main.py"'s .spec file and paste the following in the first line
- "from kivy_deps import sdl2,glew"
- and after this in coll=COLLECT paste: 
- **after** a.datas,
  \*[Tree(p) for p in (sdl2.dep_bins+glew.dep_bins)],

Then update the .exe by running the following command
> pyinstaller main.spec -y
