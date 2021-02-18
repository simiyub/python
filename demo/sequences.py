#Sequence types
#Python offers three sequence types: list, tuple and range.
# There are also other sequence types tailored to process binary and text strings.
print("python sequences: list, tuple, range\n")
print("sequence operations")
print("___________________")

int_list = [1,2,3,4,5]
int_tuple = (1,2,3,4,5)
print('int_list :')
print(int_list)
print("\n")
print('int_tuple :')
print(int_tuple)

print('3 in int_list:')
print(3 in int_list)

print('\n 6 not in int_tuple')
print(6 not in int_tuple)

alpha_sequence = ['a','b','c','d','e']
print("concatenated : int_list and alpha_list")
concatenated = int_list + alpha_sequence
print(concatenated)