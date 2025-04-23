try:
    subor = open("subor.txt", "r")

    while True:
        riadok = subor.readline()
        if riadok == "":
            break
        print(riadok.strip())# strip odstráni nečitateľné znaky napr. \n, \t (enter)

    subor.close()# zatvorí súbor
except:
    print("súbor sa nenašiel")