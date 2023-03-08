import shutil
class File:
    def __init__(self, file):
        self.file = file
        self.read()
        self.frequence = self.frequence_appartition()

    def read(self):
        with open(self.file, "r") as f:
            text = f.read()
        self.text = text
    def write(self, content):
        with open(self.file, "w") as f:
            f.write(content)

    def frequence_appartition(self):
        frequence = {}
        for i in self.text:
            if i not in frequence.keys():
                frequence[i] = 1
            else:
                frequence[i] += 1
        frequence = dict(sorted(frequence.items(), key=lambda t: t[0]))
        return sorted(frequence.items(), key=lambda t: t[1])

    def write_frequence(self):
        with open(self.file[:-4] + "_freq.txt", "w") as f:
            f.write(str(len(self.frequence)) + "\n")
            for item in self.frequence:
                char = item[0]
                freq = str(item[1])
                f.write(f"{char} {freq} \n")


