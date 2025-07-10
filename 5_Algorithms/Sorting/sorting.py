

class Sorting():

    def bubble(unsorted):
        for i in range(len(unsorted)):
            for j in range(0,len(unsorted)-i-1):
                if unsorted[j] > unsorted[j+1]:
                    #swap the numbers
                    unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
        sorted = unsorted
        return sorted
    
    def selection(unsorted):
        length = len(unsorted)
        for i in range(length):
            min = i
            for j in range(i+1,length):
                if unsorted[j] < unsorted[min]:
                    min = j
            unsorted[i], unsorted[min] = unsorted[min], unsorted[i]

        sorted = unsorted
        return sorted


                


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(f"Values unsorted: {numbers} \n\n")
sorted = Sorting.selection(numbers)
print(f"Values sorted:   {sorted}\n")