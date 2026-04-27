# Mit Super Projekt 🚀

Dette projekt er en interaktiv Python-applikation til håndtering og registrering af personoplysninger. Programmet gør det muligt at oprette en lokal database (JSON-fil) over personer, søge i dem, slette dem og få personlige hilsner baseret på navne.

## 📋 Funktioner

    Hovedmenu: Naviger nemt mellem programmets forskellige funktioner.

    Robust Registrering: Indtastning af navne og alder med fuld fejlhåndtering og validering.

    Personlige Hilsner: Programmet genkender specifikke navne (f.eks. Bart, Kim, John, Kirsten, Silke) og giver unikke svar.

    Permanent Lagring: Gemmer automatisk data i en personer.json fil, så oplysningerne huskes til næste gang.

    Søgefunktion: Find hurtigt alderen på en specifik person i systemet.

    Slettefunktion: Mulighed for at fjerne personer fra databasen.

    Visuel Feedback: Rydder terminalen for en pænere oplevelse og inkluderer små pauser/nedtællinger.

## 🛠️ Krav

For at køre dette program skal du have:

    Python 3.x installeret på din computer.

    En terminal eller kommandoprompt (Bash, PowerShell, etc.).

## 🚀 Installation & Opstart

    Hent koden:
    Kopier main.py til din lokale projektmappe:
    Bash

    mkdir mit_super_projekt
    cd mit_super_projekt

    Kør programmet:
    Du starter applikationen ved at køre følgende kommando i din terminal:
    Bash

    python3 main.py

## 📖 Sådan bruges det

Når programmet starter, mødes du af en hovedmenu med 5 valgmuligheder:

    Se alle personer: Viser en liste over alle navne og aldre, der er gemt i systemet.

    Registrer nye personer: Her kan du tilføje nye medlemmer. Programmet spørger først, hvor mange du vil tilføje.

    Søg efter en person: Indtast et navn for at se personens alder.

    Slet en person: Fjern en person permanent fra JSON-databasen.

    Afslut: Gemmer og lukker programmet sikkert.

## 📂 Filstruktur

    main.py: Selve programkoden.

    personer.json: Databasen (oprettes automatisk ved første kørsel/gemning).

---

Udviklet af Bart (med hjælp fra John og Kim)