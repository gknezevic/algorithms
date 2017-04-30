# sample input -1 2 4 -3 5 2 -5 2

maxSubArray = 0
first = 0
last = 0

def algorithm1(array):
    global maxSubArray
    #for x in range(len(array)-1):
    for x in range(len(array)-1):
        #print(x)
        sum = int(array[int(x)])
        for y in array[int(x)+1:]:
            #print(str(x) + ' ' + y)
            sum += int(y)
            if maxSubArray < sum:
                maxSubArray = sum
                global first
                global last
                first = int(x)
                last = int(y)

def algorithm2(array):
    p = s = 0
    for k in range(len(array)):
        s = max(int(array[k]), s + int(array[k]))
        p = max(p, s)
    print("max sum is: ", p)


def readLine():
    return input().split(" ")

def printArray(array):
    for num in array:
        print(num, sep=" ")

array = readLine()
algorithm1(array)
#printArray(array)
print('max=%d, first=%d, last=%d', maxSubArray, first, last)
algorithm2(array)