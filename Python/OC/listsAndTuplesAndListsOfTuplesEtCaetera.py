if __name__ == "__main__":
    lst1 = list()
    tpl1 = ()
    print("{auth} said one day that small things are better than huge ones...".format(auth="M. Ghandi"))
    print("That's why he decided to make these:")
    print(lst1)
    print(tpl1)
    lst1 = [3, 2, 1, "engines on", ("take", "off")]
    print("In the 60's they often said :")
    for items in lst1[:-1]:
        print(items)
    for sub_items in lst1[-1]:
        print(sub_items)
    lst1.append("And the rocket took off {auth}".format(auth="JFK"))
    print(lst1[-1])
    print(lst1)
    lst1.insert(len(lst1) - 1, "toto")
    print(lst1)
    invasion = ["toto", "toto"]
    print("toto came back !")
    print(lst1 + invasion)
    lst1.extend(invasion)
    print(lst1)
    print("Definetly the terrible toto invades us !")

