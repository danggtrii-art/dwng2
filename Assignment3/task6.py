def middle_character(s):
    length = len(s)
    mid = length // 2
    
    if length % 2 == 0:
        return s[mid - 1] + s[mid]
    else:
        return s[mid]
def middle_character(s):
    length = len(s)
    mid = length // 2
    
    if length % 2 == 0:
        return s[mid - 1] + s[mid]
    else:
        return s[mid]
text = input("Enter a string: ")
result = middle_character(text)
print(result)
