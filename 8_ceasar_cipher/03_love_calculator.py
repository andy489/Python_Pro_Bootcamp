def calculate_love_score(name1, name2):
    fir = ["T", "R", "U", "E"]
    sec = ["L", "O", "V", "E"]

    c1 = 0
    c2 = 0

    for char in name1:
        if char.upper() in fir:
            c1 += 1
        if char.upper() in sec:
            c2 += 1
    for char in name2:
        if char.upper() in fir:
            c1 += 1
        if char.upper() in sec:
            c2 += 1

    print(f"{c1}{c2}")


calculate_love_score("Kanye West", "Kim Kardashian")