def draw_square(n: int, char: str = "#", hollow: bool = True) -> None:
    """Print a square of size n using the given char.

    - If hollow is True, prints only the border; otherwise filled.
    """
    if n <= 0:
        return

    for i in range(n):
        line = []
        for j in range(n):
            if hollow and 0 < i < n - 1 and 0 < j < n - 1:
                line.append(" ")
            else:
                line.append(char)
        print("".join(line))


if __name__ == "__main__":
    try:
        # Read size from input; default to 5 if empty
        raw = input().strip()
        size = int(raw) if raw else 5
    except Exception:
        size = 5

    draw_square(size)
