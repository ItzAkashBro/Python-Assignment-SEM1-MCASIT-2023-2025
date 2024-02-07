# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20,4:6}
# dic2={3:30, 4:40,5:2}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 36, 4: 40, 5: 52, 6: 60}

dic1={1:10, 2:20,4:6}
dic2={3:30, 4:40,5:2}
dic3={5:50,6:60}
dic4={ }
for i in [dic1, dic2, dic3]:
    for key, value in i.items():
        dic4[key] = dic4.get(key, 0) + value
print("Result:", dic4)
