import re

def mul(s):
    n1, n2 = [int(x) for x in re.findall("\d{1,3}", s)]
    # print(n1, n2)
    return n1 * n2

def sol():
    with open("input.txt", "r") as file:
        inputStr = file.read()
        
        lst = re.findall("mul\(\d{1,3},\d{1,3}\)", inputStr)
        ans = 0
        for l in lst:
            ans += mul(l)
        print(f"Part 1 ans: {ans}")

        processStr = inputStr.split("do")
        do = True
        ans2 = 0
        for s in processStr:
            if s[:3] == "n't":
                # print("don't")
                # print(s)
                do = False 
            else:
                # print("do")
                # print(s)
                do = True
            
            if do:
                lst = re.findall("mul\(\d{1,3},\d{1,3}\)", s)
                for l in lst:
                    ans2 += mul(l)
        print(f"Part 2 ans: {ans2}")


if __name__ == "__main__":
    sol()
