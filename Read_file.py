def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False
    try:
        with open('acrony123Ams.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except:
        print("The reference fille can not be found!")
        return # the try-except loop stops here
    
    if not found:
        print('The acronym does not exist')

def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')
    with open('acronyms.txt', 'a') as file:
        file.write('\n' + acronym + ' - ' + definition)

def main():
    # Ask the user whether they want to find or add an acronym
    choice = input('Do you want to find(F) or add(A) an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()