#!/usr/bin/env python3

height = 5
all_chars = []
data = {}
aliases = {}
with open("font-master.txt", "r") as f:
    while True:
        line = f.readline()
        if not line: break
        if not line.startswith(';'): continue
        description = line.strip()[1:]
        char_index = int(description[2:4], 16)
        if description[4:9] == ' -> $':
            alias_index = int(description[9:11], 16)
            aliases[char_index] = alias_index
        else:
            c = chr(char_index)
            all_chars.append(c)
            data[c] = {}
            data[c]["description"] = description
            data[c]["rawbits"] = []
            for row in range(height):
                data[c]["rawbits"].append(f.readline().strip())

print("; Mono Number 5 pixel font")
print("; (c) 2023 by 4am")
print("; license:Open Font License 1.1, see OFL.txt")
print("; This file is automatically generated")
print()
print("FontDataLookup")
for i in range(0x80):
    try:
        char_index = all_chars.index(chr(i))
    except ValueError:
        try:
            char_index = all_chars.index(chr(aliases[i]))
        except:
            char_index = 255
    print(f"         !byte {char_index}")
print()
for row in range(height):
    print(f"FontDataRow{row}")
    for c in all_chars:
        description = data[c]['description']
        bits = "1" + data[c]["rawbits"][row][::-1]
        print(f"         !byte %{bits} ; {description}")
