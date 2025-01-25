piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("a", "b", "c", "d", "e", "f", "g")

print(f"1: {piano_keys}")

print(f"2: {piano_keys[2:5]}")
print(f"3: {piano_keys[2:]}")
print(f"4: {piano_keys[:5]}")

print(f"5: {piano_keys[2:5:2]}")
print(f"6: {piano_keys[::2]}")

print(f"7: {piano_keys[::-1]}")
print(f"8: {piano_keys[::-3]}")

print(f"9: {piano_tuple[2:5]}")
