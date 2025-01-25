def main():
    f = open("ScoreData.txt", " w+")

    score = 0
    for i in range(300):
        if i % 10 == 0:
            score += 1
        if i % 5 == 0 and i != 0:
            score += 1
        if i % 15 == 0 and i != 0:
            score += 1
            score += 1
        if i % 50 == 0 and i != 0:
            score += 1
        if i % 100 == 0 and i != 0:
            score += 1
        f.write(str(score) + "\n")


main()
