def sol():
    with open("input.txt", "r") as file:
        data = [x.strip() for x in file.readlines()]
        print((len(data[0]), len(data))) # 140, 140

        trackX , trackM, trackA, trackS = [], [], [], []
        for i in range(len(data)):
            for j in range(len(data[i])):
                    if data[i][j] == 'X':
                        trackX.append((i,j))
                    if data[i][j] == 'M':
                        trackM.append((i,j))
                    if data[i][j] == 'A':
                        trackA.append((i,j))
                    if data[i][j] == 'S':
                        trackS.append((i,j))

        print(trackX[:5])
        print(trackM[:5])
        print(trackA[:5])
        print(trackS[:5])

        count = 0
        for x, y in trackX:
            print(x, y)
            if (x+1,y) in trackM and (x+2, y) in trackA and (x+3, y) in trackS:
                print("horizontal forward")
                count += 1

            if (x-1, y) in trackM and (x-2, y) in trackA and (x-3, y) in trackS:
                print("horizontal backwards")
                count += 1

            if (x, y+1) in trackM and (x, y+2) in trackA and (x, y+3) in trackS:
                print("vertical downward")
                count += 1
            
            if (x, y-1) in trackM and (x, y-2) in trackA and (x, y-3) in trackS:
                print("vertical upward")
                count += 1
            
            if (x+1, y+1) in trackM and (x+2, y+2) in trackA and (x+3, y+3) in trackS:
                print("diagonal bottom right")
                count += 1

            if (x-1, y-1) in trackM and (x-2, y-2) in trackA and (x-3, y-3) in trackS:
                print("diagonal top left")
                count += 1

            if (x+1, y-1) in trackM and (x+2, y-2) in trackA and (x+3, y-3) in trackS:
                print("diagonal top right")
                count += 1

            if (x-1, y+1) in trackM and (x-2, y+2) in trackA and (x-3, y+3) in trackS:
                print("diagonal bottom left")
                count += 1


        count2 = 0
        for x, y in trackA:
            print(x, y)
            if (x-1, y-1) in trackM and (x-1, y+1) in trackM and (x+1, y-1) in trackS and (x+1, y+1) in trackS:
                print("up-right X-MAS")
                count2 += 1
            
            if (x-1, y-1) in trackS and (x-1, y+1) in trackS and (x+1, y-1) in trackM and (x+1, y+1) in trackM:
                print("top-down X-MAS")
                count2 += 1

            if (x-1, y-1) in trackM and (x-1, y+1) in trackS and (x+1, y-1) in trackM and (x+1, y+1) in trackS:
                print("lefty X-MAS")
                count2 += 1

            if (x-1, y-1) in trackS and (x-1, y+1) in trackM and (x+1, y-1) in trackS and (x+1, y+1) in trackM:
                print("righty X-MAS")
                count2 += 1

        print(f"Part 1 ans: {count}")
        print(f"Part 2 ans: {count2}")


if __name__ == "__main__":
    sol()
