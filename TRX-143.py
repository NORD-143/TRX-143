import os, sys
os.system("git pull")
try:
    __import__("TRX").menu()
except Exception as e:
    exit(str(e))
