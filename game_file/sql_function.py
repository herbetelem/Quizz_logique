# coding : utf-8

# import de la librairie
import sqlite3

# * Fonction pour recuperer depuis la bdd

class SQL_request:
    
    def __init__(self):
        # # * connection a la bdd
        # self.connection = sqlite3.connect("quizz.db")
        # # * instance du curseur
        # self.cursor = self.connection.cursor()
        # Vérifier que le joueur et déjà dans la base de donnée ou non
        self.user = False

    def read_question(self, id_question):
        self.connection = sqlite3.connect("quizz.db")
        self.cursor = self.connection.cursor()
        # * je definit quelle id de question je vais chercher
        id_question = (id_question,)
        # * je créer la requete
        self.cursor.execute('SELECT * FROM hh_quizz WHERE id = ?', id_question)
        # * je formate en tuple ma reponse
        self.question_tmp = self.cursor.fetchone()
        self.connection.close()

    def read_answer(self, id_question):
        self.connection = sqlite3.connect("quizz.db")
        self.cursor = self.connection.cursor()
        # * je definit quelle id de question je vais chercher
        id_question = (id_question,)
        # * je créer la requete
        self.cursor.execute('SELECT * FROM hh_answer WHERE id_question = ?', id_question)
        # * je formate en tuple mes reponses
        self.anwser_tmp = self.cursor.fetchall()
        self.connection.close()

    def read_score(self):
        self.connection = sqlite3.connect("quizz.db")
        self.cursor = self.connection.cursor()
        # * je créer la requete
        self.cursor.execute('SELECT * FROM hh_score ORDER BY score DESC')
        # * je formate en tuple mes reponses
        self.score_tmp = self.cursor.fetchall()
        self.connection.close()

    def create_score(self, name, score):
        connection = sqlite3.connect("quizz.db")
        cursor = connection.cursor()
        # creer la sauvegarde d'un nouveau scores
        new_user = (cursor.lastrowid, name, score)
        # On creer une requete pour un nouveau utilisateur
        cursor.execute('INSERT INTO hh_score VALUES(?,?,?)', new_user)
        # envoi du nouveau joueur
        connection.commit()
        connection.close()

    def verification_user(self, name_user):
        self.connection = sqlite3.connect("quizz.db")
        self.cursor = self.connection.cursor()
        # Vérifier si le joueur est déjà dans la liste
        self.cursor.execute('SELECT * FROM hh_score WHERE name = ?', name_user)
        result = self.cursor.fetchone()
        if result == None :
            self.user = False
        else : 
            self.user = True
            self.connection.close()

    def update_user(self, name, score):
        connection = sqlite3.connect("quizz.db")
        cursor = connection.cursor()
        # Mettre a jour les score d'un joueur
        update_user = (score, name)
        cursor.execute('UPDATE hh_score SET score = ? WHERE name = ?', update_user)
        connection.commit()
        connection.close()
