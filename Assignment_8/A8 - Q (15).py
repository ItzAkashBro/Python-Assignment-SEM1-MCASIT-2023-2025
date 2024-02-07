#  Write a Python program to convert more than one list to a nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004':
# {'Saim Richards': 92}}]

sid = ['S001', 'S002', 'S003', 'S004']
sn = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
ss = [85, 98, 89, 92]
n = [{id: {name: score}} for id, name, score in zip(sid, sn, ss)]
print("Nested Dictionary:", n)