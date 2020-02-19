

def castle_placer(terrain):
    if terrain.__len__() == 1 or terrain.count(terrain[0]):
        return 1
    else:
        n_of_castles = 0
        landform = []
        for i in range(0, terrain.__len__() - 1):
            if terrain[i] != terrain[i + 1]:
                landform.append(1 if terrain[i + 1] - terrain[i] > 0 else -1)
        landform.insert(0, landform[0] * (-1))
        landform.append(landform[-1] * (-1))
        for i in range(0, landform.__len__() - 1):
            if landform[i] != landform[i + 1]:
                n_of_castles += 1
        return n_of_castles




if __name__ == "__main__":
    T = int(input("Number of testcases: "))
    N = []
    for i in range(0, T):
        N.append([int(t) for t in input().strip().split(' ')])

    for i in range(0, T):
        print(N[i])
        print(castle_placer(N[i]))