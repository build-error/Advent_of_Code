def safeOrNot(report):
    for i in range(1, len(report)-1):
        d1 = report[i] - report[i-1]
        d2 = report[i+1] - report[i]
        # print(d1, d2)
        cond1 = abs(d1) > 0 and abs(d1) < 4
        cond2 = abs(d2) > 0 and abs(d2) < 4
        cond3 = (d1 * d2) > 0

        # print(cond1, cond2, cond3)
        if not cond1 or not cond2 or not cond3:
            # print("Unsafe")
            return False
    return True

def make_subsets(lst):
    subsets = []
    for i in range(len(lst)):
        subset = lst[:i] + lst[i+1:]
        subsets.append(subset)

    return subsets

def sol():
    with open("input.txt", "r") as file:
        lines = [x.strip() for x in file.readlines()] 
        data = []
        for line in lines:
            data.append([int(x) for x in line.split()])
        
        ans = 0
        ans2 = 0
        for report in data:
            mini_report = make_subsets(report)
            count = 0
            if safeOrNot(report):
                ans+=1
            else:
                print(report)
                print(mini_report)
                count = 0
                for r in mini_report:
                    if safeOrNot(r):
                        ans2+=1
                        break
            
        print(f"Number of safe reorts: {ans}")
        print(f"Number of safe reports after one modification: {ans2}")

        

if __name__ == "__main__":
    sol()
