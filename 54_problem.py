from pathlib import Path


FOLDER = Path("/Users/mezo/Documents/Software Engineer/problems")
counter = 0

for file in FOLDER.iterdir():
    if file.is_file():
        print(file.rename(f"{counter}_problem.py"))
        counter+= 1