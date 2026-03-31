import subprocess


def run_command(cmd: list[str], description: str, shell: bool = False) -> None:
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}\n")

    if shell:
        subprocess.run(cmd, shell=shell, check=True, capture_output=True, text=True)
    else:
        subprocess.run(cmd, check=True, capture_output=True, text=True)



def adding_in_staging(file_name: str = None) -> None:
    if file_name:
        run_command(
            cmd=["git", "add", f"{file_name}"],
            description="adding a file in stagin area."
        )
    else:
        run_command(
            cmd=["git", "add", "."],
            description="adding all untracked file in staging area."
        )


adding_in_staging()