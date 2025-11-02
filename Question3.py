from collections import Counter

string = str(input("Enter text: "))
string = string.lower()

print(f"Total characters (with spaces): {len(string)}")

without_spaces = string.replace(" ", "")
print(f"Total characters (without spaces): {len(without_spaces)}")

words = string.split(" ")
print(f"Total Words: {len(words)}")

freq = {}
for char in without_spaces:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(f"Character frequency: {freq}")

common = []
for char in without_spaces:
    if freq[char] > 1 and char not in common:
        common.append(char)
print(f"Most common character: {common}")

print(f"Is palindrome: {string == string[::-1]}")

print(f"Reversed: {string[::-1]}")