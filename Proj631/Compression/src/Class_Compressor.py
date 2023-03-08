from src.Class_Tree import Tree
from src.Class_File import File
import bitarray
import os
import struct

class Compressor:
    def __init__(self, file):
        self.file = file
        self.fileObj = File(file)
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
                dic[char] = self.tree.parcours_profondeur(char)
        self.dic = dic

    def compresstion_rate(self):
        old_file_size = os.path.getsize(self.file)
        new_file_size = os.path.getsize(f"{self.file[:-4]}_compressed.bin")
        return 1 - new_file_size/old_file_size

    def average_size(self, _list):
        total = 0
        for i in _list:
            total += len(i)
        return total/len(_list)


    def codage_huffman(self):
        self.fileObj.write_frequence()
        int_char = []
        for char in self.text:
            int_char.append(self.dic[char])
        avg_size = self.average_size(int_char)
        bit_char = []
        for char in int_char:
            for bit in char:
                bit_char.append(int(bit))
        bits = bitarray.bitarray(bit_char)
        with open(f"{self.file[:-4]}_compressed.bin", "wb") as new_file:
            bits.tofile(new_file)
        print("Done")
        print("Compression rate : ", self.compresstion_rate())
        print("Average character size (in bit) : ", avg_size)
        print("file location : ", os.path.join(os.getcwd(), f"{self.file}_compressed.bin"))
