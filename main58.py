def oblicz_pole_trojkata(podstawa, wysokosc):
    pole = 0.5 * podstawa * wysokosc
    return pole

podstawa = float(input("Podaj długość podstawy trójkąta: "))
wysokosc = float(input("Podaj wysokość trójkąta: "))

pole = oblicz_pole_trojkata(podstawa, wysokosc)
print("Pole trójkąta wynosi:", pole)
