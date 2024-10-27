######################################
# Task 1
#####################################

squares = {num**2 for num in range(1, 11)}
print(squares)

######################################
# Task 2
####################################

user_input = input("Enter a string: ")

char_set = set(user_input)

print(char_set)

######################################
# Task 3
####################################

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 6, 7, 8, 9)

merged_tuple = tuple1 + tuple2

unique_tuple = tuple(set(merged_tuple))

duplicated_values = []

seen = set()
for item in merged_tuple:
    if item in seen:
        if item not in duplicated_values:
            duplicated_values.append(item)
    else:
        seen.add(item)

print("Merged tuple without duplicates:", unique_tuple)
print("List of duplicated values:", duplicated_values)

###################################
# Task 4
####################################

original_tuple = (1, 2, 3, 4)

swapped_tuple = (original_tuple[-1],) + original_tuple[1:-1] + (original_tuple[0],)

print("Original tuple:", original_tuple)
print("Tuple after swapping first and last elements:", swapped_tuple)

###################################
# Task 5
####################################

nested_tuple = (1, (2, 3), (4, (5, 6)))

flat_tuple = (nested_tuple[0],) + nested_tuple[1] + (nested_tuple[2][0],) + (nested_tuple[2][1][0],) + (nested_tuple[2][1][1],)

print("Flattened tuple:", flat_tuple)

###################################
# Task 6
####################################


set1 = {1, 2}
set2 = {'a', 'b'}

result_set = set()

for x in set1:
    for y in set2:
        result_set.add((x, y))

print(result_set)


