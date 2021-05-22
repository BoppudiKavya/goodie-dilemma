import math

num = 0
goodies = {}
def readinput(filename):
    global num, goodies
    with open(filename, "r") as filereader:
        count = 0
        for line in filereader:
            if("Number of employees" in line):
                num = int(line.split(":")[1].strip())
            if(count == 1 and ":" in line):
                cost = int(line.split(":")[1].strip())
                name = line.split(":")[0].strip()
                goodies[cost] = name
            if("Goodies and Prices" in line):
                count = 1

def writeoutput(filename, answer):
    global goodies
    with open(filename, "w") as filewriter:
        filewriter.write("The goodies selected for distribution are:\n\n")
        for elem in answer:
            filewriter.write("{0}: {1}\n".format(goodies[elem], elem))
        filewriter.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is {0}". format(answer[-1] - answer[0]))

print("Enter input filename: ")
filename = input()
readinput(filename)
prices = sorted(goodies.keys())
diff = math.inf
index = 0
for i in range(len(prices) - num + 1):
    tempdiff = prices[i:i+num][-1] - prices[i:i+num][0]
    if(tempdiff < diff):
        diff = tempdiff
        index = i

writeoutput("sample_output2.txt", prices[index: index+num])
print("Saved output in sample_output1.txt!\n")