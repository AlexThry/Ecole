import shutil


class File:
    def __init__(self, file):
        """
        Objet permettant de manipuler des fichiers
        :param file: Chemin du fichier
        """
        self.text = None
        self.file = file
        self.read()
        self.frequence = self.frequence_appartition()

    def read(self):
        """
        Méthode pour lire un fichier
        :return: None
        """
        with open(self.file, "r") as f:
            text = f.read()
        self.text = text

    def write(self, content):
        """
        Méthode pour écrire du contenu dans un fichier
        :param content: Contenu à écrire
        :return: None
        """
        with open(self.file, "w") as f:
            f.write(content)

    def frequence_appartition(self):
        """
        Méthode qui compte le nombre d'apparition de chaque caractère du fichier
        :return: dict: dictionnaire de type {caractère: fréquence}
        """
        frequence = {}
        for i in self.text:
            if i not in frequence.keys():
                frequence[i] = 1
            else:
                frequence[i] += 1
        frequence = dict(sorted(frequence.items(), key=lambda t: t[0]))
        return sorted(frequence.items(), key=lambda t: t[1])

    def write_frequence(self, path=None):
        """
        Ecris un fichier avec les fréquences pour chaque caractère
        :param path: chemin du fichier
        :return: None
        """
        if not path:
            with open(self.file[:-4] + "_freq.txt", "w") as f:
                f.write(str(len(self.frequence)) + "\n")
                for item in self.frequence:
                    char = item[0]
                    freq = str(item[1])
                    f.write(f"{char} {freq} \n")
        else:
            with open(path, "w") as f:
                f.write(str(len(self.frequence)) + "\n")
                for item in self.frequence:
                    char = item[0]
                    freq = str(item[1])
                    f.write(f"{char} {freq} \n")
