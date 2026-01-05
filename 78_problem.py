from pathlib import Path


FOLDER = Path("/Users/mezo/Documents/Software Engineer/problems")


def handle_files(*, path: Path) -> None:
    counter = 0

    for file in FOLDER.iterdir():
        if file.is_file():
            print(file.rename(f"{counter}_problem.py"))
            counter+= 1
    return True


handle_files(path=FOLDER)
