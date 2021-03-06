"""
rubot-arm v0.0.1
simple script to run commands
from anywhere in project directories

just pass in the command with arguments and it'll run it appropriately

Enter project root directory or better stil save it as an environmental variable
"""
import time
import os

PROJECT_ROOT = os.environ.get("PROJECT_ROOT")

exe_cmd = "manage.py"
args = input("enter manage.py command(s): ")

common_args = {
    'makemigrations': 'making migrations...',
    'migrate': 'migrating tables...',
    'runserver': 'running server...',
}

if args in common_args.keys():
    print(f"{common_args[args]}")
else:
    print(f"okay are you sure {args} is a {exe_cmd} command lets see...")

def arm(exe=exe_cmd, args=args):
    if exe not in os.listdir():
        try:
            os.chdir(PROJECT_ROOT)
            os.system(f"python {exe} {args}")
        except SystemError:
            return SystemError
    else:
        try:
            os.system(f"python {exe} {args}")
        except SystemError:
            return SystemError

arm()
