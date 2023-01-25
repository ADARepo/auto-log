Can run the script as is after inputting credentials in the .ini for logging into SWTOR. I also made it an executable on my own machine.
Will modify in the future to work with other applications instead of just SWTOR, the problem  has been UAC.

used pyinstaller for making an executable out of this
also used:
pywin32
pillow
opencv_python for confidence factor on the screenshot recognition


TODO:
- Change from being time based to work around UAC prompt and instead just rely on images
- Instead of positioning for mouse clicks, instead rely fully on image processing since the launcher UI could be moved or the screen could be modified
    - This usually isn't a problem since the launcher opens in the same spot every time
    - Having the pictures be more precise for the clicks by including pictures of the text boxes and buttons should help reduce missed clicks