txt = "Hello, I'm Converting From C to Python"

print(f"captialize :: {txt.capitalize()}")

print(f"count of e :: {txt.count('e')}")

print(f"casefold :: {txt.casefold()}")

print(f"center :: {txt.center(100)}")

print(f'encode :: {txt.encode(encoding="ascii",errors="ignore")}')

print(f"endwith :: {txt.endswith('n')}")

print(f"expandtaps :: {txt.expandtabs(10)}")

print(f"find :: {txt.find('h')}")

print(f"title :: {txt.title()}")

print(f"strip :: {txt.strip()}")

print(f"replace :: {txt.replace('o', 'x')}")

print(f"partition :: {txt.partition('Converting')}")