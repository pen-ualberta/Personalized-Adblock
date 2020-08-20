def readFile():
    fileName= 'domainNames.txt'
    f = open(fileName, 'r')
    file = f.read().splitlines()
    newList= []
    for line in file:
        line = '"*://*.'+line[10:] + '/*"'
        newList.append(line)
    
    f.close()
    return newList
        
    
def main():
    aList = readFile()
    f = open('formatedFile.txt', 'w+')
    for line in aList:
        f.write(line + '\n')
    
    f.close()
main()
        