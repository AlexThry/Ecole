from src.Class_Tree import Tree
import struct

class Compressor:
    def __init__(self, file):
        self.file = file
        self.tree = Tree(file)
        self.open_text(file)
        self.create_dict()

    def open_text(self, file):
        f = open(file, "r")
        self.text = f.read()
        f.close()

    def create_dict(self):
        dic = {}
        for char in self.text:
            if char not in dic.keys():
                dic[char] = int(self.tree.parcours_profondeur(char))
        self.dic = dict(sorted(dic.items(), key=lambda x: x[1]))

    def codage_huffman(self):
        with open(f"{self.file}_compressed.bin", "wb") as new_file:
            int_char = []
            for char in self.text:
                int_char.append(self.dic[char])
            print(int_char)
            binary_char = ""
            for i in int_char:
                new_file.write(i.to_bytes((i.bit_length() + 7) // 8, "big"))


