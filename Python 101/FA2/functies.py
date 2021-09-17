standaard_prijzen = [0.60, 0.80]
standaard_prijs_range = range(12, 64)


def standaardprijs(afstandKM):
    if afstandKM < 0:
        return 0
    elif afstandKM < 50:
        prijs = afstandKM * standaard_prijzen[0]
        return prijs
    else:
        prijs = 15 + (afstandKM * standaard_prijzen[1])
        return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if weekendrit:
        if leeftijd in standaard_prijs_range:               # weekend + 40% korting
            prijs *= 0.60
        else:                                               # weekend + 35% korting
            prijs *= 0.65
    else:
        if leeftijd in standaard_prijs_range:               # doordeweeks + standaardprijs
            return prijs
        else:                                               # doordeweeks + 30% korting
            prijs *= 0.70
    return prijs