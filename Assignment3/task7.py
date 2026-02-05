def acronym(phrase):
    words = phrase.split()
    result = ""
    
    for w in words:
        result += w[0].upper()
    
    return result
text = input("Enter a phrase:")
print(acronym(text))