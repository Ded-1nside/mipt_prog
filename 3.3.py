import zipfile
import os


def write_array(array, file_name):
    file_name.write('\n'.join(array))


with zipfile.ZipFile('main.zip', 'r') as zip_ref:
    zip_ref.extractall('.')


ans = []
for cur_dir, dirs, files in os.walk('main'):
    for i in range(len(files)):
        if '.py' in files[i]:
            ans.append(cur_dir)

with open("text3.txt", "w") as txt:
    write_array(ans, txt)
