"""
Person Registration System
A simple application for registering and managing person data with persistent storage.
"""

import json  # For saving and loading data in JSON format
import os    # For cross-platform terminal clearing
from time import sleep  # For realistic countdown functionality
from pathlib import Path  # For better file path handling

# Constants
MAX_ATTEMPTS = 3
DATA_FILE = "personer.json"


def gem_til_json(personer):
    """
    Save person data to a JSON file.
    
    Args:
        personer (list): List of person dictionaries to save
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(personer, f, ensure_ascii=False, indent=4)
        print("\n ✅ Data er gemt i 'personer.json'")
    except Exception as e:
        print(f"❌ Kunne ikke gemme data: {e}")


def hent_fra_json():
    """
    Load person data from a JSON file.
    
    Returns:
        list: List of person dictionaries, or empty list if file doesn't exist
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            personer = json.load(f)
        print("\n ✅ Data er hentet fra 'personer.json'")
        return personer
    except FileNotFoundError:
        print("❌ Filen 'personer.json' blev ikke fundet.")
        return []  # Return empty list so program can continue without crashing
    except Exception as e:
        print(f"❌ Kunne ikke hente data: {e}")
        return []  # Return empty list for error resilience


def clear_screen():
    """
    Clear the terminal screen in a cross-platform way.
    Works on both Windows (cls) and Unix-based systems (clear).
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def vis_alle_personer(personer):
    """
    Display all registered persons.
    
    Args:
        personer (list): List of person dictionaries to display
    """
    if not personer:
        print("\n📭 Ingen personer registreret endnu.")
    else:
        print("\n--- 👥 ALLE REGISTREREDE PERSONER ---")
        for p in personer:
            print(f"- {p['navn']}: {p['alder']} år")


def soeg_person(personer):
    """
    Search for a person by name (case-insensitive).
    
    Args:
        personer (list): List of person dictionaries to search in
    """
    if not personer:
        print("📭 Ingen data at søge i.")
        return
    
    navn_soeg = input("\nHvem leder du efter? ").strip().lower()
    
    # Validate input
    if not navn_soeg:
        print("⚠️ Du skal indtaste et navn.")
        return
    
    fundet = False
    for p in personer:
        if p["navn"].lower() == navn_soeg:
            print(f"🔍 Fundet: {p['navn']} er {p['alder']} år gammel.")
            fundet = True
            break
    
    if not fundet:
        print(f"❌ Kunne ikke finde '{navn_soeg}' i databasen.")


def slet_person(personer):
    """
    Delete a person by name (case-insensitive) and save changes.
    
    Args:
        personer (list): List of person dictionaries to modify
    """
    if not personer:
        print("📭 Ingen data at slette.")
        return
    
    navn_slet = input("\nHvem skal slettes? ").strip().lower()
    
    # Validate input
    if not navn_slet:
        print("⚠️ Du skal indtaste et navn.")
        return
    
    oprindeligt_antal = len(personer)
    
    # Create a new list containing only persons whose names don't match
    personer[:] = [p for p in personer if p["navn"].lower() != navn_slet]
    
    if len(personer) < oprindeligt_antal:
        print(f"🗑️ {navn_slet.capitalize()} er nu slettet.")
        gem_til_json(personer)  # Remember to save the changes!
    else:
        print(f"❓ Kunne ikke finde nogen ved navn '{navn_slet}'.")


def hilsen(navn):
    """
    Display a personalized greeting based on the person's name.
    
    Args:
        navn (str): The person's name
    """
    navn_lower = navn.lower()  # Convert to lowercase for consistent comparison

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
    """
    Verify and store the user's age with retry logic and countdown.
    
    Returns:
        int: The validated age, or None if all attempts fail
    """
    forsoeg = MAX_ATTEMPTS
    alder = None

    # Keep asking while we have attempts remaining and no valid age
    while forsoeg > 0:
        alder_input = input(f"Hvor gammel er du? (Forsøg tilbage: {forsoeg}): ").strip()
        
        try:
            alder = int(alder_input)
            break  # Success! Exit the while loop
        except ValueError:
            forsoeg -= 1
            if forsoeg > 0:
                print("FEJL: Du skal indtaste et gyldigt heltal.")
            else:
                print("Du har brugt alle dine forsøg.")
                return None

    # Determine adult/child status
    status = "Voksen" if alder >= 18 else "Barn"
    print(f"Du er {alder} år gammel, hvilket vil sige at du er {status}.")

    # Countdown from 3 to 1 with 1 second delay between each
    for i in range(3):
        print(f"Tæller ned: {3 - i}...")
        sleep(1)
    
    return alder


def register_personer(personer):
    """
    Register new persons and add them to the existing list.
    Handles retry logic for input validation.
    
    Args:
        personer (list): Existing list of person dictionaries to append to
    """
    # Display existing data count
    if personer:
        print(f"\n📂 Eksisterende data fundet og indlæst.\nVelkommen tilbage! Jeg kender allerede {len(personer)} personer.")
    
    tryings = MAX_ATTEMPTS

    # Validate number of persons to register
    while tryings > 0:
        try:
            antal_personer_input = input("Hvor mange personer vil du registrere? ").strip()
            
            if not antal_personer_input:
                print("⚠️ Du skal indtaste et tal.")
                tryings -= 1
                continue
            
            antal_personer = int(antal_personer_input)
            
            if antal_personer <= 0:
                print("⚠️ Antal skal være større end 0.")
                tryings -= 1
                continue
            
            break
        except ValueError:
            tryings -= 1
            if tryings > 0:
                print("Indtast venligst kun tal.")
            else:
                print("Du har brugt alle dine forsøg.")
                return

    # Register each person
    for i in range(antal_personer):
        navn = input(f"\nNavn på person {i+1}: ").strip()
        
        # Validate name input
        if not navn:
            print("⚠️ Navn kan ikke være tomt.")
            i -= 1  # Retry this person
            continue
        
        hilsen(navn)

        # Reuse smart age validation with retry logic
        while True:
            try:
                alder_input = input(f"Hvor gammel er {navn}? ").strip()
                
                if not alder_input:
                    print("⚠️ Du skal indtaste et tal.")
                    continue
                
                alder = int(alder_input)
                
                if alder < 0:
                    print("⚠️ Alder kan ikke være negativ.")
                    continue
                
                break
            except ValueError:
                print("Indtast venligst et tal.")
        
        # Add person dictionary to the list
        personer.append({"navn": navn, "alder": alder})

    # Find the oldest person (Python magic!)
    aeldste_person = max(personer, key=lambda x: x["alder"])
    
    print(f"\nDen ældste person er {aeldste_person['navn']} på {aeldste_person['alder']} år.")

    # Display all registered persons
    print("\nAlle registrerede personer:")
    for p in personer:
        print(f"- {p['navn']}: {p['alder']} år")

    gem_til_json(personer)  # Save data in JSON format


def display_menu():
    """
    Display the main menu options.
    """
    print("\n--- HOVEDMENU ---")
    print("1. Se alle personer")
    print("2. Registrer nye personer")
    print("3. Søg efter en person")
    print("4. Slet en person")
    print("5. Afslut")


def main():
    """
    Main program loop handling user menu selection and program flow.
    """
    personer = hent_fra_json()
    
    while True:
        # Clear screen for clean display
        clear_screen()
        
        display_menu()
        
        valg = input("\nVælg (1-5): ").strip()  # .strip() removes unnecessary whitespace
        
        # Validate input
        if not valg:
            print("⚠️ Du skal indtaste et valg.")
            input("\nTryk på Enter for at fortsætte...")
            continue

        # Handle menu selection
        if valg == "1":
            vis_alle_personer(personer)
        elif valg == "2":
            register_personer(personer)
        elif valg == "3":
            soeg_person(personer)
        elif valg == "4":
            slet_person(personer)
        elif valg == "5":
            print("🚀 Tak for i dag! Programmet lukker...")
            break
        else:
            print(f"❌ '{valg}' er ikke en mulighed. Vælg venligst et tal mellem 1 og 5.")
        
        input("\nTryk på Enter for at fortsætte...")  # Hold the terminal open so user can see the result


if __name__ == "__main__":
    main()
