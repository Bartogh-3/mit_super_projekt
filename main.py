# Dette har jeg gjort for at kunne få en realistisk nedtælling
from time import sleep 

def main():
    print("Velkommen til alderstjekket!")
    alder()
    
    print("\nNu skal vi registrere oplysninger for nogle personer.")
    register_personer()

def hilsen(navn):
    navn_lower = navn.lower() # Dette konverterer navnet til små bogstaver, så det er nemmere at sammenligne

    if navn_lower == "john":
        print("🤖 System-besked: Hejsa makker! Bash-eksperten er stolt af din fremgang.")
    elif navn_lower == "bart" or navn_lower == "kim":
        print(f"👋 Velkommen tilbage {navn}, skaberen af dette program!")
    elif navn_lower == "kirsten":
        print(f"👋 Velkommen {navn}, du er da konen til skaberen af dette program!")
    elif navn_lower == "silke":
        print(f"👋 Velkommen {navn}, du er da skaberen af dette program's prinsesse!")
    else:
        print(f"Hej {navn}, hyggeligt at du kigger forbi.")

def alder():
    forsoeg = 3
    alder = None

    # Vi bliver ved med at spørge, så længe vi har forsøg tilbage og ingen alder har
    while forsoeg > 0:
        alder_input = input(f"Hvor gammel er du? (Forsøg tilbage: {forsoeg}): ")
        
        try:
            alder = int(alder_input)
            break  # Succes! Hop ud af while-løkken
        except ValueError:
            forsoeg -= 1
            if forsoeg > 0:
                print("FEJL: Du skal indtaste et gyldigt heltal.")
            else:
                print("Du har brugt alle dine forsøg.")
                return # Afslut programmet

    # Her kører vi med den meget enklere udgave af logikken.
    status = "Voksen" if alder >= 18 else "barn"
    print(f"Du er {alder} år gammel, hvilket vil sige at du er {status}.")

    # Her er der lavet en lille nedttælling fra 3 til 1 uden en pause imellem hver udskrift
    for i in range(3):
        print(f"Tæller ned: {3 - i}...")
        # Her laver jeg en pause på 1 sekund mellem hver udskrift
        sleep(1)  

def register_personer():
    personer = []  # Vores liste til at gemme data
    tryings = 3

    # print("Indtast oplysninger for 3 personer:")
    antal_personer = int(input("Hvor mange personer vil du registrere? "))
    while tryings > 0:
        try:
            antal_personer = int(antal_personer)
            break
        except ValueError:
            tryings -= 1
            if tryings > 0:
                print("Indtast venligst kun tal.")
            else:
                print("Du har brugt alle dine forsøg.")
                return

    for i in range(antal_personer):
        navn = input(f"\nNavn på person {i+1}: ")
        hilsen(navn)

        # Her genbruger vi din smarte fejlhåndtering til alderen
        while True:
            try:
                alder = int(input(f"Hvor gammel er {navn}? "))
                break
            except ValueError:
                print("Indtast venligst et tal.")
        
        # Vi tilføjer en 'dictionary' til vores liste
        personer.append({"navn": navn, "alder": alder})

    # Nu finder vi den ældste (Python magi!)
    aeldste_person = max(personer, key=lambda x: x["alder"])
    
    print(f"\nDen ældste person er {aeldste_person['navn']} på {aeldste_person['alder']} år.")

    # Vi kan også udskrive alle personerne for at se, at det virker
    print("\nAlle registrerede personer:")
    for p in personer:
        print(f"- {p['navn']}: {p['alder']} år")

if __name__ == "__main__":
    main()
