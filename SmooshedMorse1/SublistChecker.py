# Checks if a given list is a sublist of another list
# Order must be preserved

sample_list1 = ".....-"
sample_list2 = "..."
sample_list3 = [2, 4, 3]
sample_list4 = [9, 0, 11]

def is_sublist(sublist, superlist):
    i = 0
    for index, sp in enumerate(superlist):
        if sublist[i] == sp:
            if i == len(sublist) - 1:
                return True
            i += 1
        else:
            i = 0
        if i == 0 and len(superlist) - index - 1 < len(sublist):
            return False

print(str(len(sample_list1)))
print(is_sublist(sample_list2, sample_list1))
print(is_sublist(sample_list3, sample_list1))
print(is_sublist(sample_list4, sample_list1))