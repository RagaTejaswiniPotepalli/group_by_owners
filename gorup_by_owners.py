def group_by_owners():
    fileOwnerDict = {}
    n = int(input("Enter number of values"))
    i = 0
    while i < n:
        fileName = input("Please enter file name")
        ownerName = input("Please enter Owner Name")
        fileOwnerDict[fileName] = ownerName
        i += 1
    UniqueOwners = []
    UniqueOwners = sorted(sorted(fileOwnerDict.values()))
    UniqueOwners = list(dict.fromkeys(UniqueOwners))

    finalDict = {}
    for x in UniqueOwners:
        listFileName = []
        for y in fileOwnerDict:
            if fileOwnerDict[y] == x:
                listFileName.append(y)
        finalDict[x] = listFileName
    print(finalDict)

group_by_owners()




