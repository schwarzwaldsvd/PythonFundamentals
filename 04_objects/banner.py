def banner(message, border='-'):
    line = border * int(len(message)/len(border))
    print(line)
    print(message)
    print(line)

banner("Norwegian Blue")
banner("Sun, Moon and Stars", "*")
banner("Sun, Moon and Stars", border="*")
banner(border=".", message="Hello from Earth")
