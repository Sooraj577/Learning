import copy


# using = operator
print("\n****Using = Operator****")
original1 = [[1,2], [3,4]]
new = original1
print(f"original => {original1}, id => {id(original1)}")
print(f"new => {new}, id => {id(new)}")
print("Updating the original list")
original1.append([5,6])
print(f"updated original => {original1}, id => {id(original1)}")
print(f"new after updating original => {new}, id => {id(new)}")

# shallow copy
print("\n****Shallow Copy****")
original = [[1,2],[3,4]]
shallow_copied = copy.copy(original)
print(f"original => {original}, id => {id(original)}")
print(f"shallow copied => {shallow_copied}, id => {id(shallow_copied)}")
print("Updating the original list")
original.append([5,6])
print(f"updated original => {original}, id => {id(original)}")
print(f"shallow copied after updating original => {shallow_copied}, id => {id(shallow_copied)}")
original[1][1] = 'AA'
print(f"updated original => {original}, id => {id(original)}")
print(f"shallow copied after updating original => {shallow_copied}, id => {id(shallow_copied)}")


# deep copy
print("\n****Deep Copy****")
original2 = [[1,2],[3,4]]
deep_copied = copy.deepcopy(original2)
print(f"original => {original2}, id => {id(original2)}")
print(f"deep copied => {deep_copied}, id => {id(deep_copied)}")
print("Updating the original list by appending [5,6]")
original2.append([5,6])
print(f"updated original => {original2}, id => {id(original2)}")
print(f"deep copied after updating original => {deep_copied}, id => {id(deep_copied)}")
print("Updating the original list")
original2[1][1] = 'AA'
print(f"updated original => {original2}, id => {id(original2)}")
print(f"deep copied after updating original => {deep_copied}, id => {id(deep_copied)}")


# Ref:
# https://www.programiz.com/python-programming/shallow-deep-copy
# https://www.educative.io/answers/what-is-difference-between-shallow-copy-and-deep-copy-in-python