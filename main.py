# Dette har jeg gjort for at kunne få en realistisk nedtælling
from time import sleep 

def main():
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

if __name__ == "__main__":
    main()
