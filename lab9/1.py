test_list = [0, 1, 2, 3, 4]

for i in test_list:
    test_list.append(i)
    if i == 4:
        break

print(test_list)