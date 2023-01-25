import pyautogui as pg
import subprocess, elevate, configparser, os, sys, win32com.shell.shell as shell, time, pyperclip as pc

# Solution for starting script as admin to be able to access launcher as admin.
# Found here: https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script/11746382#11746382
ASADMIN = 'asadmin'
if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

# Using elevate
# elevate.elevate(show_console=False)

# Gather credentials for logging into the Star Wars The Old Republic Launcher
# Setup for a config file found https://docs.python.org/3/library/configparser.html
config = configparser.ConfigParser()
try:
    config.read('info.ini')
    user = config['SWTOR']['username']
    password = config['SWTOR']['password']
except KeyError:
    pg.confirm("Config file 'info.ini' not found.")
    sys.exit()

swLoginScreen = 'swtor.png'
swPlayButt = 'swplaybutt.png'

# Attempt to open star wars launcher. use Popen to be asynchronous and the program will continue to execute.
# If using .run() or .call(), the program will not continue to run until the launcher is closed.
try:
    path = "C:/Program Files (x86)/Electronic Arts/BioWare/Star Wars - The Old Republic/launcher.exe"
    subprocess.Popen(path)
except FileNotFoundError:
    pg.confirm("Game launcher not found.")
    sys.exit()

passes = 0

# Sleep for a bit while the launcher loads before trying to search.
time.sleep(3)

# Username and password  to be looked for until found. 
while True:
    try:
        passes += 1
        swtorCoord = pg.locateCenterOnScreen('swtor.png', grayscale=False, confidence=.5)
    except pg.ImageNotFoundException:
        # Asking if we want the program to continue if we can't find the screen after a bit.
        if passes % 10 == 0:
            response = pg.confirm("10 attempts made to find star wars launcher window. Cancel to stop, OK to continue.")
            if response == "Cancel":
                pg.alert(text="Program exiting...")
                sys.exit()
        continue
    break

# Enters username and password then clicks login.
# Click Username text box, copy and paste username. positioning
pg.moveTo(662, 484)
pg.leftClick()
pc.copy(user)
pg.hotkey('ctrl', 'v')

# Password. positioning.
pg.moveTo(638, 576)
pg.leftClick()
pc.copy(password)
pg.hotkey('ctrl', 'v')

# Click Login. positioning.
pg.leftClick(551, 785)

passes = 1

# Now find the Play button on the next window.
while True:
    try:
        passes += 1
        swPlayCoord = pg.locateCenterOnScreen(swPlayButt, grayscale=False, confidence=.5)
    except pg.ImageNotFoundException:
        # Asking if we want the program to continue if we can't find the PLAY button after a bit.
        if passes % 10 == 0:
            response = pg.confirm("10 attempts made to find the PLAY button. Cancel to stop, OK to continue.")
            if response == "Cancel":
                pg.alert(text="Program exiting...")
                sys.exit()
        continue
    break

# Wait a few seconds for the Play button to be ready.
time.sleep(6)

# Click Play and exit.
pg.leftClick(1340, 778)

# If the PLAY button was clicked before it was ready, wait another couple of seconds to see if the button is still there.
# If it is, try clicking it again one more time.
try:
    swPlayCoord = pg.locateCenterOnScreen(swPlayButt, grayscale=False, confidence=.5)
    time.sleep(1)
    pg.leftClick(1340, 778)
except pg.ImageNotFoundException:
    sys.exit()
finally:
    sys.exit()