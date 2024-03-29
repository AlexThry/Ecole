import sqlite3
import os

class DBAgent:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(os.getcwd(), "DB", "database.db"))
        self.curs = self.conn.cursor()
        self.curs.execute("CREATE TABLE IF NOT EXISTS Profs (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50))")
        self.curs.execute("CREATE TABLE IF NOT EXISTS Modules (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50))")
        self.curs.execute("CREATE TABLE IF NOT EXISTS anime (idModule REFERENCES Modules(id), idProf REFERENCES Profs(id), PRIMARY KEY (idModule, idProf))")
        self.curs.execute("CREATE TABLE IF NOT EXISTS aEcrit (lien VARCHAR(256), idProf INTEGER REFERENCES Profs(id), PRIMARY KEY (lien, idProf))")
        self.conn.commit()
        
    def addProf(self, name:str):
        response = self.curs.execute(f"SELECT name FROM Profs WHERE name = ?", (name,)).fetchall()
        if len(response) == 0:
            self.curs.execute("INSERT INTO Profs (name) VALUES (?)", (name,))
            self.conn.commit()
            
    def addModule(self, name:str):
        response = self.curs.execute(f"SELECT name FROM Modules WHERE name = ?", (name,)).fetchall()
        if len(response) == 0:
            self.curs.execute("INSERT INTO Modules (name) VALUES (?)", (name,))
            self.conn.commit()
            
    def addParticipation(self, moduleName:str, profsNames:list):
        idModule = self.curs.execute(f"SELECT id FROM Modules WHERE name = ?", (moduleName,)).fetchall()
        for prof in profsNames:
            idProf = self.curs.execute(f"SELECT id FROM Profs WHERE name = ?", (prof.upper().strip(),)).fetchall()
            if idProf and idModule:
                try:
                    self.curs.execute("INSERT INTO anime (idModule, idProf) VALUES (?, ?)", (idModule[0][0], idProf[0][0]))
                    self.conn.commit()
                except sqlite3.IntegrityError:
                    pass

    def addArticle(self, prof:str, link:str):
        pass


    # def addLien(self, lien):
    #     self.curs.execute("INSERT INTO Liens (lien) VALUES (?)", (lien,))

    def addAEcrit(self, lien, idProf):
        try:
            if not self.curs.execute("SELECT idProf FROM aEcrit WHERE lien = ?", (lien,)).fetchall():
                self.curs.execute("INSERT INTO aEcrit (lien, idProf) VALUES (?, ?)", (lien, idProf))
                self.conn.commit()
        except:
            pass
    def getAllProfs(self):
        profs = []
        _profs = self.curs.execute("SELECT name FROM Profs").fetchall()
        for prof in _profs:
            profs.append(prof[0])
        return profs

    def getProfId(self, prof):
        return self.curs.execute("SELECT id FROM Profs WHERE name = ?", (prof,)).fetchall()[0][0]

