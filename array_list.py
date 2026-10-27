from abstract_list import AbstractList

class ArrayList(AbstractList):
    def __init__(self):
        self.__array = [None] * 100
        self.__size = 0
    
    def add(self, element): 
        if self.__size >= 100:
            raise OverflowError
    
        for i in range(100):
            if self.__array[i] == None:
                self.__array[i] = element
                self.__size += 1
                break 
    
        
    def remove(self, index): 
        return_index = self.__array[index]
    
        for i in range(99 - index):
            self.__array[index + i] = self.__array[index + i + 1]

        self.__array[99] = None
        self.__size -= 1
        return return_index

    def get(self, index):
        return self.__array[index]

    def set(self, index, element): 
        self.__array[index] = element

    def getIndex(self, element): 
        
        for index in range(100):
            if self.__array[index] == element:
                return index
        return -1

    def size(self):
        return self.__size
