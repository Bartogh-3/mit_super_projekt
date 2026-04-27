author1 = "John"
author2 = "Bart"
                
def main():
    brugernavn = input("Hvad hedder du? ")

    print(f"Hej {brugernavn}, velkommen til mit_super_projekt!")
    print(f"{author1} siger: Hejsa {brugernavn}, god kodning!\n{author2} ønsker dig en god kodnings oplevelse, {brugernavn}!")
    print(f"Dette projekt er lavet af: {author1} og {author2}.")
    print("Vi håber, at du vil nyde at bruge dette projekt!")
    print("Tak fordi du bruger mit_super_projekt!")

if __name__ == "__main__":
    main()
