new_file = open('new_file.txt', 'x')
new_file.close()
import os
print("checking if file exists")
if os.path.exists("my file .txt"):
    os.remove
else:
    print("file dose not exist")