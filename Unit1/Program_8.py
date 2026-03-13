text = input("Enter a string: ")

vowels = sum(1 for ch in text if ch.lower() in "aeiou")
print("Number of vowels:", vowels)

length = 0
for _ in text:
    length += 1
print("Length of string:", length)

rev = text[::-1]
print("Reversed string:", rev)

find_str = input("Enter substring to find: ")
replace_str = input("Enter substring to replace with: ")
print("After replace:", text.replace(find_str, replace_str))

if text == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
