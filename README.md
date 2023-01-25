- Can run the script as is after inputting credentials in a info.ini for logging into SWTOR. I also made it an executable on my own machine.
    - create an info.ini file setup like this (extra newlines not necessary, just for formatting here. Look inside configparser docs for more info):
 
   [SWTOR]                           
                                       
   username = your_username         
                                       
   password = your_password           
                                       
- 
- Will modify in the future to work with other applications instead of just SWTOR, the problem will just be UAC.
- Used python 3.10.9 in a venv


inside the venv:
- used pyinstaller for making an executable out of this
- also used:
- pywin32
- pillow
    - may need to run python -m pip install --upgrade pip and python -m pip install --upgrade Pillow
- opencv_python for confidence factor on the screenshot recognition


TODO:
- Change from being time based to work around UAC prompt and instead just rely on images
- Instead of positioning for mouse clicks, instead rely fully on image processing since the launcher UI could be moved or the screen could be modified
    - This usually isn't a problem since the launcher opens in the same spot every time
    - Having the pictures be more precise for the clicks by including pictures of the text boxes and buttons should help reduce missed clicks
