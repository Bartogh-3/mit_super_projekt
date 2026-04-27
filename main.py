# Dette har jeg gjort for at kunne få en realistisk nedtælling
from time import sleep 

def main():
    # Vi spørger først om brugerens alder
    alder_input = input("Hvor gammel er du? ") 
    # Vi prøver at konvertere inputtet til et heltal, og hvis det ikke er muligt, vil det kaste en fejl
    try:
        alder = int(alder_input)
    # Hvis vi har en fejl, fordi inputtet ikke kunne konverteres
    except ValueError:
        print("FEJL: Du skal indtaste et gyldigt tal. Prøv igen.")
        # Giv bruger 2 forsøg mere
        for _ in range(2):
            alder_input = input("Prøv igen: ")
            try:
                alder = int(alder_input)
                break
            except ValueError:
                # Hvis det stadig ikke lykkedes, så print en fejlmeddelelse
                print("FEJL: Du skal indtaste et gyldigt tal. Prøv igen.")
        else:
            # Hvis vi har prøvet 3 gange og stadig ikke har fået et gyldigt tal, så afslutter vi programmet
            print("Du har prøvet 3 gange, men det lykkedes ikke at indtaste et gyldigt tal.")
            return

    # Her tjekker vi om brugeren er Vokse eller et barn
    if alder >= 18:
        status = "Voksen"
    else:
        status = "barn"

    # Her printer vi resultatet ud til brugeren
    print(f"Du er {alder} år gammel, hvilket vil sige at du er {status}.")

    # Her er der lavet en lille nedttælling fra 3 til 1 uden en pause imellem hver udskrift
    for i in range(3):
        print(f"Tæller ned: {3 - i}...")
        # Her laver jeg en pause på 1 sekund mellem hver udskrift
        sleep(1)  

if __name__ == "__main__":
    main()
