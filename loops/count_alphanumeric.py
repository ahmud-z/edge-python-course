password = "$1,$23abc%#A"
count = 0

for sym in password:
    if (
        (sym >= "a" and sym <= "z")
        or (sym >= "A" and sym <= "Z")
        or (sym >= "1" and sym <= "9")
    ):
        count = count + 1

print(f"Total alphanumeric counted: {count}")
