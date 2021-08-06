while True:
    file = input("Enter the filename\n")
    print("\nOpening " + file + '...\n')
    try:
        f = open(file, "r", encoding='utf-8')
        break
    except IOError:
        input("Error in file opening, please type correct filename")


    print(f)