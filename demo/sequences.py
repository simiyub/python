#Sequence types
#Python offers three sequence types: list, tuple and range.
# There are also other sequence types tailored to process binary and text strings.
print("python sequences: list, tuple, range\n")
print("sequence operations")
print("___________________")

int_list = [1,2,3,4,5]
int_tuple = (1,2,3,4,5)
print(type(int_list), int_list)
print(type(int_tuple),int_tuple)

print('3 in int_list:')
print(3 in int_list)

print('\n--6 not in int_tuple--')
print(6 not in int_tuple)

alpha_sequence = ['a','b','c','d','e']
print(type(alpha_sequence),alpha_sequence)
print(type(int_tuple),int_tuple)
print("\nconcatenate")
print(type(int_list), int_list)
concatenated = int_list + alpha_sequence
print(concatenated)
print("\nsequence*n : add the sequence to itself n times")
print(int_tuple*3)

print("2nd item of s, origin 0")
int_list = [1,2,3,4,5]
print(int_list)
print(int_list[1])

print("slice of s from i to j")
int_list = [1,2,3,4,5,6,7,8,9,10]
print("slice of int_list from 3 to 8 inclusive")
print(int_list[2:8])

print("slice of s from i to j with step k")
int_list = [1,2,3,4,5,6,7,8,9,10]
print(int_list)
print(int_list[1::2])

print("length of s")
print(len(int_list))

print("smallest item of s")
print(min(int_list))

print("largest item of s")
print(max(int_list))

int_list = [1,2,1,4,3,6,7,8,3,10]

print("index of the first occurrence of 3 in the list (at or after index i and before index j)")
print(int_list.index(3))

print("number of occurrences of 1 in list")
print(int_list.count(1))