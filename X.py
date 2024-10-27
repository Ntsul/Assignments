#########################################
# task 1
#########################################

def mint(listA, listB):
    return list(zip(listA, listB))


list1 = [1, 2, 3]
list2 = ['x', 'y', 'z']

result = mint(list1, list2)
print(result)

#########################################
# task 2
#########################################

get_even = lambda numbers: [n for n in numbers if n % 2 == 0]


input_list = [1, 2, 3, 4, 5, 6, 7]

result = get_even(input_list)
print(result)

#########################################
# task 3
#########################################


get_positive = lambda lst: list(filter(lambda x: x > 0, lst))


input_data = [8, -2, 0, 4, -1, 10, -5]

result_2 = get_positive(input_data)
print(result_2)

#########################################
# task 4
#########################################


palindrome_filter = lambda items: list(filter(lambda item: item == item[::-1], items))


string_list = ["civic", "deified", "python", "level", "hello"]

result = palindrome_filter(string_list)
print(result)

#########################################
# task 5
#########################################

from functools import reduce


def product_of_list(num_list):
    return reduce(lambda a, b: a * b, num_list)


numbers = [2, 4, 6, 8]
result = product_of_list(numbers)
print(result)

#########################################
# task 6
#########################################


def filter_ending_words(word_list, suffix):
    try:

        return list(filter(lambda word: isinstance(word, str) and word.endswith(suffix), word_list))
    except TypeError:
        return "Invalid input! Make sure the first parameter is a list of strings and the second is a string."


words = ['hello', 'world', 'coding', 'nod']
ending = 'ing'

result = filter_ending_words(words, ending)
print(result)
