# Quang Lam

import datetime
import random
import time

def main():

    # Write an XML file with the results
    file = open("StringCompareTiming.xml","w")

    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')

    file.write('<Plot title="String Comparison Time (Worst Scenario)">\n')

    # Test strings of size 1000 to 100000.
    xmin = 1000
    xmax = 100000

    # Record the string sizes in xList
    #  and the average access time to compare the strings in yList
    xList = []
    yList = []

    for x in range(xmin, xmax+1, 1000):
        print(x)

        xList.append(x)

        prod = 0

        # Creates 2 strings of size x
        # Creates worst scenario (explained below)
        str1= ''.join('a' for _ in range(x - 1))
        str2= ''.join('a' for _ in range(x - 1))

        str1 = str1 + 'b'
        str2 = str2 + 'c'


        # let any garbage collection/memory allocation complete or at least
        # settle down
        time.sleep(1)

        # Time before the 1000 test retrievals
        starttime = datetime.datetime.now()

        isEqual = True
        for i in range(x):
            if (str1[i] != str2[i]):
                isEqual = False
                break

        # Best scenario: The first characters of 2 strings are different, it only takes one operation.
        # Worst scenario: Only the last character of each string is different from each other, it takes x operation.
        # => O(N)

        # Python native implementation
        # mockCompare = str1 == str2
        # O(1)

        # Time after the 1000 test retrievals
        endtime = datetime.datetime.now()

        # The difference in time between start and end.
        deltaT = endtime - starttime

        # Divide by 1000 for the average access time
        # But also multiply by 1000000 for microseconds.
        accessTime = deltaT.total_seconds() * 1000

        print(accessTime)

        yList.append(accessTime)

    file.write('  <Axes>\n')
    file.write('    <XAxis min="'+str(xmin)+'" max="'+str(xmax)+'">String Size</XAxis>\n')
    file.write('    <YAxis min="'+str(min(yList))+'" max="'+str(max(yList))+'">Microseconds</YAxis>\n')
    file.write('  </Axes>\n')

    file.write('  <Sequence title="Comparison Time (Worst Scenario) vs String Size" color="red">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')

    file.write('  </Sequence>\n')

    # Divider
    # Record the string sizes in xList
    #  and the average access time to compare the strings in yList
    xList = []
    yList = []

    for x in range(xmin, xmax+1, 1000):
        print(x)

        xList.append(x)

        prod = 0

        # Creates 2 strings of size x
        # Creates worst scenario (explained below)
        str1= ''.join('a' for _ in range(x - 1))
        str2= ''.join('a' for _ in range(x - 1))

        str1 = 'b' + str1
        str2 = 'c' + str2


        # let any garbage collection/memory allocation complete or at least
        # settle down
        time.sleep(1)

        # Time before the 1000 test retrievals
        starttime = datetime.datetime.now()

        isEqual = True
        for i in range(x):
            if (str1[i] != str2[i]):
                isEqual = False
                break

        # Best scenario: The first characters of 2 strings are different, it only takes one operation.
        # Worst scenario: Only the last character of each string is different from each other, it takes x operation.
        # => O(N)

        # Python native implementation
        # mockCompare = str1 == str2
        # O(1)

        # Time after the 1000 test retrievals
        endtime = datetime.datetime.now()

        # The difference in time between start and end.
        deltaT = endtime - starttime

        # Divide by 1000 for the average access time
        # But also multiply by 1000000 for microseconds.
        accessTime = deltaT.total_seconds() * 1000

        print(accessTime)

        yList.append(accessTime)

    file.write('  <Sequence title="Comparison Time (Best Scenario) vs String Size" color="green">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')

    file.write('  </Sequence>\n')
    
    # Divider
    # Record the string sizes in xList
    #  and the average access time to compare the strings in yList
    xList = []
    yList = []

    for x in range(xmin, xmax+1, 1000):
        print(x)

        xList.append(x)

        prod = 0

        # Creates 2 strings of size x
        # Creates worst scenario (explained below)
        str1= ''.join(random.choice('abcde') for _ in range(x))
        str2= ''.join(random.choice('abcde') for _ in range(x))

        # let any garbage collection/memory allocation complete or at least
        # settle down
        time.sleep(1)

        # Time before the 1000 test retrievals
        starttime = datetime.datetime.now()

        isEqual = True
        for i in range(x):
            if (str1[i] != str2[i]):
                isEqual = False
                break

        # Best scenario: The first characters of 2 strings are different, it only takes one operation.
        # Worst scenario: Only the last character of each string is different from each other, it takes x operation.
        # => O(N)

        # Python native implementation
        # mockCompare = str1 == str2
        # O(1)

        # Time after the 1000 test retrievals
        endtime = datetime.datetime.now()

        # The difference in time between start and end.
        deltaT = endtime - starttime

        # Divide by 1000 for the average access time
        # But also multiply by 1000000 for microseconds.
        accessTime = deltaT.total_seconds() * 1000

        print(accessTime)

        yList.append(accessTime)

    file.write('  <Sequence title="Comparison Time (Random Scenario) vs String Size" color="blue">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')

    file.write('  </Sequence>\n')    

    file.write('</Plot>\n')
    file.close()

if __name__ == "__main__":
    main()
