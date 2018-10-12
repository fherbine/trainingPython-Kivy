str1 = "toto"

if __name__ == "__main__":
    str2 = str1.upper()
    print(str2)
    print(str2.lower())
    print("{0} means {1}, well I'm not sure, because {1} could also mean {0}".format(str1, str2))
    print("{toto} is the {origin} name of {TOTO}".format(toto=str1, TOTO=str2, origin="scandinavian"))
    print(str1 + str2 + "!\n" + "{} just appeared ".format(str1) + str(2) + " times")
    print("let's make the analysis of the " + str1[0] + str1[1:-1] + str1[-1] + "s")
    print("There's only " + str(len(str1)) + " letters in this name:")
    for c in str1:
        print(c)
    print("There's " + str(2) + " main parts in this terrific name {} and {}".format(str1[:2], str2[2:]))
