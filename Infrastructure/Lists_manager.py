

class Lists_manager(object):
    def __init__(self):
        pass

    def isEmpty(self, _list):
        print("Checking if the list is empty\n")
        if len(_list) == 0:
            print("The list is empty\n")
            return True
        else:
            print("The list is not empty\n")
            return False

    def isMixed(self):
        pass

    def isNested(self):
        pass

    def printList(self, _list):
        print(f"The list content: {_list}")

    def appendList(self, _list1, _list2):
        print("Appending a list to another")
        _list1.append(_list2)

    def insertInList(self, _list, _index):
        pass

    def removeFromList(self):
        pass

    def indexOfItem(self):
        pass

    def lengthOfList(self):
        pass

    def countItemInList(self):
        pass

    def reverseList(self):
        pass

    def popList(self):
        pass
