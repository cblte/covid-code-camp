# -*- encoding: utf-8 -*-

shelf = ["Zaubersaege", "leer", "Wunderkekse", "Trickkarten", "leer"]

def add_shelf(artikel):
    print("Versuche Artikel >"+ artikel +"< auf das Regal zu legen")
    
    gefunden = "false"
    freierPlatz = 0
    for i in shelf:
        if i == "leer":
            gefunden = "true"
            break
        else:
            freierPlatz = freierPlatz + 1
            continue

    # ersetze
    if gefunden == "true":
        shelf[freierPlatz] = artikel
    else:
        shelf.append(artikel)


add_shelf("Rubik Cube")
print(shelf)
add_shelf("Liebestrank")
print(shelf)
add_shelf("Zauberstab")
print(shelf)


