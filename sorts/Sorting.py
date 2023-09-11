class StaticMethodsMeta(type):
    def __new__(cls, name, bases, dct):
        # Iterate through the class dictionary and make all methods static
        for key, value in dct.items():
            if callable(value):
                dct[key] = staticmethod(value)
        return super(StaticMethodsMeta, cls).__new__(cls, name, bases, dct)

class Sorting:
    def bubble_sort(array):
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j+1], array[j]
        return array
    
    def selection_sort(array):
        length = len(array)
        for i in range(length - 1):
            min_index = i
            for j in range(i+1, length):
                if array[min_index] > array[j]:
                    min_index = j
            if i != min_index:
                array[i], array[min_index] = array[min_index], array[i]
        return array
    
    def insertion_sort(array):
        for i in range(1, len(array)):
            temp = array[i]
            j = i - 1
            while temp < array[j] and j > -1:
                array[j + 1] = array[j]
                array[j] = temp
                j -= 1
        return array



sort = Sorting.insertion_sort([4, 2, 6, 5, 1, 3])
print(sort)