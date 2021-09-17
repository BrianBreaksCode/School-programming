def inlezen_beginstation(stations):
    correct_antwoord = False
    while not correct_antwoord:
        begin_station = input("Wat is uw beginstation: ")
        if begin_station in stations:
            correct_antwoord = True
            return begin_station
        else:
            print("Incorrect")
            continue


def inlezen_eindstation(stations, beginstation):
    correct_antwoord = False
    while not correct_antwoord:
        eind_station = input("Wat is uw eindstation: ")
        if eind_station in stations and stations.index(eind_station) > stations.index(beginstation):
            correct_antwoord = True
            print("")
            return eind_station
        elif eind_station not in stations:
            print("Station incorrect")
            continue
        else:
            print(f"Deze trein komt niet in {eind_station}")


def omroepen_reis(stations, beginstation, eindstation):
    begin_station_index = stations.index(beginstation)
    eind_station_index = stations.index(eindstation)
    afstand_stations = eind_station_index - begin_station_index
    kosten_afstand = afstand_stations * 5
    print(
        f"Het beginstation {beginstation} is het {begin_station_index + 1}e station in het traject")
    print(
        f"Het eindstation {eindstation} is het {eind_station_index + 1}e station in het traject")
    print(f"De afstand bedraagt {afstand_stations} station(s)")
    print(f"De prijs van het kaartje is {kosten_afstand} euro\n")
    print(f"Jij stapt in de trein in: {beginstation}")
    for tussen_stations in range(begin_station_index + 1, eind_station_index):
        print(f"  - {stations[tussen_stations]}")
    print(f"Jij stapt uit in: {eindstation}")


stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam",
            "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal",
            "’S-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
