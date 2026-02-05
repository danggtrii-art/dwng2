numbers = []
while True:
    s = input("Enter a number (empty to quit): ")
    if s == "":
        break
    numbers.append(float(s))
if len(numbers) > 0:
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))
else:
    print("No numbers entered")