import requests

def sol():
    with open("input.txt", "r") as file:
        lines = [x.strip() for x in file.readlines()] 
        left = []
        right = []
        for line in lines:
            l, r = [int(x) for x in line.split()]
            left.append(l)
            right.append(r)
        
        left.sort()
        right.sort()

        ########################### Part 1 ####################
        totalDistance = 0
        for l, r in zip(left, right):
            totalDistance += abs(l - r)
    

        print(f"total distance = {totalDistance}")
        ########################################################

        similarityScore = 0
        for l in left:
            count = 0
            for r in right:
                if l == r:
                    count += 1
            similarityScore += l * count

        print(f"similarity score = {similarityScore}")
        

if __name__ == "__main__":
    sol()
