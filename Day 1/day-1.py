import os


def main():
    print("Hello world!")

    noOfIncrements = 0
    lineBefore = 999999
    os.chdir(r'C:\Users\Admin\Documents\Advent of code\Day 1')
    with open("input.txt", 'r') as f:
        for line in f.readlines():
            
            line = int(line)
            if line > lineBefore:
                noOfIncrements +=1
            lineBefore = line
    print(noOfIncrements)


if __name__ == "__main__":
    main()