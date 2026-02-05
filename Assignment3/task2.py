while True:
    inch = float(input("Enter inches: "))
    
    if inch < 0:
        break
    
    cm = inch * 2.54
    print(cm, "cm")
