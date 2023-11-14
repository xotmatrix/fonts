#!/usr/bin/env python3

height = 7
all_chars = list(map(chr, range(0x20, 0x80)))

data = {}
min_index = ord(all_chars[0])
max_index = ord(all_chars[-1]) + 1
with open("font-master.txt", "r") as f:
    for c in all_chars:
        data[c] = {}
        data[c]["description"] = f.readline().strip()[1:]
        data[c]["rawbits"] = []
        for row in range(height):
            data[c]["rawbits"].append(f.readline().strip())

print("; Mono Number 7 pixel font")
print("; (c) 2023 by 4am")
print("; license:Open Font License 1.1, see OFL.txt")
print("; This file is automatically generated")
print()
for row in range(height):
    print(f"FontDataRow{row}")
    for c in map(chr, range(min_index, max_index)):
        description = data[c]['description']
        bits = "1" + data[c]["rawbits"][row][::-1]
        print(f"         !byte %{bits} ; {description}")