# Google question

# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# The function should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# The function should return 1

# Given an array = [2, 3, 4, 5]
# The function should return None

class FirstReocurringValue:

    def __init__(self):
        self.seen = {}

    def first_reocurring_value(self, array):
        seen = []
        for value in array:
            if value in seen:
                return value
            seen.append(value)
        return None
    
    def long_version(self, array):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] == array[j]:
                    return array[i]
        return None
    
    def dictionary_version(self, array):
        self.seen = {}
        for value in array:
            if value in self.seen:
                print(self.seen)
                return value
            self.seen[value] = True
        return None

frv = FirstReocurringValue()
# print(frv.first_reocurring_value([2, 5, 1, 2, 3, 5, 1, 2, 4])) # 2
# print(frv.first_reocurring_value([2, 1, 1, 2, 3, 5, 1, 2, 4])) # 1
# print(frv.first_reocurring_value([2, 3, 4, 5])) # None

# print(frv.long_version([2, 5, 1, 2, 3, 5, 1, 2, 4])) # 2
# print(frv.long_version([2, 1, 1, 2, 3, 5, 1, 2, 4])) # 1
# print(frv.long_version([2, 3, 4, 5])) # None

print(frv.dictionary_version([2, 5, 1, 2, 3, 5, 1, 2, 4])) # 2
print(frv.dictionary_version([2, 1, 1, 2, 3, 5, 1, 2, 4])) # 1
print(frv.dictionary_version([2, 3, 4, 5])) # None
# print(frv.seen)
        