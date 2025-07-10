

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
    
    def insertion(unsorted):
        length = len(unsorted)
        for i in range(1, length):
            key = unsorted[i]
            j = i -1
            while j >= 0 and unsorted[j] > key:
                unsorted[j + 1] = unsorted[j]
                j -= 1
            unsorted[j + 1] = key
        sorted = unsorted
        return sorted
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = Sorting.merge_sort(arr[:mid])
        right = Sorting.merge_sort(arr[mid:])

        return Sorting.merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return Sorting.quick_sort(left) + middle + Sorting.quick_sort(right)



numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(f"Values unsorted: {numbers} \n\n")
sorted = Sorting.quick_sort(numbers)
print(f"Values sorted:   {sorted}\n")