def toon_aantal_kluizen_vrij():
    kluis_file = open("fa_kluizen.txt", "rt")
    gebruikte_kluizen = len(kluis_file.readlines())
    kluis_file.close()
    vrije_kluizen = 12 - gebruikte_kluizen
    print(f"Er zijn {vrije_kluizen} kluizen beschikbaar\n")
    # Get number of lines through readlines and len, which doesnt work well with larger files. Good thing 12 lines isn't large anymore


def nieuwe_kluis():
    alle_vrije_kluizen = [*range(1, 13)]
    kluis_file = open("fa_kluizen.txt", "rt")
    gebruikte_kluizen = kluis_file.readlines()
    kluis_file.close()

    for i in range(len(gebruikte_kluizen)):
        gebruikte_kluis = gebruikte_kluizen[i]
        gebruikte_kluis_nr = gebruikte_kluis[:gebruikte_kluis.find(";")]
        for kluis in alle_vrije_kluizen:
            if kluis == int(gebruikte_kluis_nr):
                alle_vrije_kluizen.remove(kluis)
    # Grabs each line from the file and removes the seperator ; and the password to get the locker number
    if not alle_vrije_kluizen:
        print("Alle kluizen zijn bezet\n")
        return

    print("De volgende kluizen zijn beschikbaar:")
    for kluis in range(len(alle_vrije_kluizen)):
        print(f"Kluis {alle_vrije_kluizen[kluis]}")

    while True:
        keuze_kluis = int(input("Welke kluisnummer kiest u? "))
        if keuze_kluis not in alle_vrije_kluizen:
            print("Kluis niet beschikbaar")
            continue
        else:
            kluis_code = input("Kies uw kluiscode: ")
            kluis_file = open("fa_kluizen.txt", "a")
            kluis_file.write(f"{keuze_kluis};{kluis_code}\n")
            kluis_file.close
            print(f"Kluis {kluis_code} is nu van u.")
            break


def kluis_openen():
    kluis_file = open("fa_kluizen.txt", "rt")
    gebruikte_kluizen = kluis_file.readlines()
    kluis_file.close()
    for line in range(len(gebruikte_kluizen)):
        test = gebruikte_kluizen[line]
        test = test.replace("\n", "")
        kluis_nr = test[:test.find(";")]
        kluis_code = test[test.find(";") + 1:]
        gebruikte_kluizen[line] = [kluis_nr, kluis_code]

    input_kluisnr = input("Kluisnummer: ")
    input_code = input("Code: ")
    onjuist = True
    for check in gebruikte_kluizen:
        if input_kluisnr in check and input_code in check:
            print("Uw kluis nu geopent. \n")
            onjuist = False
    if onjuist:
        print("De ingevulde gegevens kloppen niet. \n")


def kluis_teruggeven():
    kluis_file = open("fa_kluizen.txt", "rt")
    gebruikte_kluizen = kluis_file.readlines()
    kluis_file.close()
    for line in range(len(gebruikte_kluizen)):
        test = gebruikte_kluizen[line]
        test = test.replace("\n", "")
        kluis_nr = test[:test.find(";")]
        kluis_code = test[test.find(";") + 1:]
        gebruikte_kluizen[line] = [kluis_nr, kluis_code]

    input_kluisnr = input("Kluisnummer: ")
    input_code = input("Code: ")
    onjuist = True
    for check in gebruikte_kluizen:
        if input_kluisnr in check and input_code in check:
            print("Uw kluis is nu teruggegeven \n")
            gebruikte_kluizen.remove([input_kluisnr, input_code])
            kluis_file = open("fa_kluizen.txt", "w")
            for line in gebruikte_kluizen:
                test = line[0] + ";" + line[1] + "\n"
                kluis_file.write(test)
            kluis_file.close()
            onjuist = False
    if onjuist:
        print("De ingevulde gegevens kloppen niet.\n")


def stoppen():
    quit()


opties = {
    1: toon_aantal_kluizen_vrij,
    2: nieuwe_kluis,
    3: kluis_openen,
    4: kluis_teruggeven,
    5: stoppen
}
keuze = ["1: Ik wil weten hoeveel kluizen nog vrij zijn", "2: Ik wil een nieuwe kluis",
         "3: Ik wil even iets uit mijn kluis halen", "4: Ik wil mijn kluis teruggeven",
         "5: ik wil stoppen"]

while True:
    try:
        for i in keuze:
            print(i)
        choice = int(input("Kies uw optie: "))
        if choice not in range(1, 6):
            print("Keuze incorrect\n")
            continue
        else:
            opties[choice]()
    except ValueError:
        print("")
        continue
