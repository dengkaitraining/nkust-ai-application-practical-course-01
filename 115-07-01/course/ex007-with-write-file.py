"""
Solution 2: Make the File Path Dynamic (Best for Sharing Code)
Instead of relying on VS Code settings, update your Python code to find demofile.txt relative to the script itself.
Use the built-in pathlib module to build an absolute path automatically:

reference :
1. Google Search AI
   url : https://www.google.com/search?q=vs+code+FileNotFoundError%3A+%5BErrno+2%5D+No+such+file+or+directory%3A+%27demofile.txt%27&oq=vs+code+FileNotFoundError%3A+%5BErrno+2%5D+No+such+file+or+directory%3A+%27demofile.txt%27&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDU3OTJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
2. W3Schol - Python File Open
   url : https://www.w3schools.com/python/python_file_handling.asp
"""
from pathlib import Path

# Finds the folder where your script is saved
script_dir = Path(__file__).parent

# Combines the folder path with your file name
file_path = script_dir / "writefile.txt"

with open(file_path, "w") as f:
  f.write("Now the file has more content!\n")
  f.write("Second\n")

# open and read the file after the writing:
print("[Ex1. open and read the file after the writing:]")
with open(file_path) as f:
  print(f.read())

with open(file_path, "a") as f:
  f.write("3!\n")
  f.write("4\n")

# open and read the file after the appending:
print("[Ex2. open and read the file after the appending:]")
with open(file_path) as f:
  print(f.read())