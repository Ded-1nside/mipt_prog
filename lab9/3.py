import os
import string as st


class TextLoader:
    def __init__(self, path):
        if os.path.isdir(path):
            self.path = path
            self.file_paths = []

            for cur_file in os.listdir(self.path):
                file_path = os.path.join(self.path, cur_file)
                if os.path.isfile(file_path):
                    self.file_paths.append(file_path)
        else:
            print(path, 'is not a directory')
            raise ValueError
    
    def __len__(self):
        return len(self.file_paths)
    
    def __gettext__(self, path):
        with open(path, "r", encoding="utf-8") as file:
            return file.read().lower().translate(str.maketrans('', '', st.punctuation))

    def __getitem__(self, id):
        return self.__gettext__(self.file_paths[id])
    
    def __iter__(self):
        for path in self.file_paths:
            yield self.__gettext__(path)
