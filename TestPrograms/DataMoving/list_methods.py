testList = [1, 2, 3]  # init List
testList.extend(testList)  # add list to end of annother list
print(testList)
testList.append(6)  # add single item of type consistant with type
testList.insert(1, 4)  # add item @ index
testList.remove(1)  # remove first item with value
del testList[0]
print(testList.pop(1))  # remove item @ index and return
testList.reverse()
print(testList.count(1))  # number of Something in an array
print(len(testList))  # get length of list or bytearray
print(testList)
testList.clear()
