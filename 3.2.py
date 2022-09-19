def write_array(array, file_name):
    file_name.write('\n'.join(array))


arr = ["Str1", "Str2", "Obviously necessary string", "Darth Sidious", "AAAAAAA"]
with open("text2.txt", "w") as txt:
    write_array(arr, txt)