import os
import math
def extraire_nom_president(nom_fichier):

    nom_president = nom_fichier.replace("Nomination_", "").replace(".txt", "").replace("1", "").replace("2", "")
    return nom_president

dossier = "speeches"

for nom_fichier in os.listdir(dossier):
    chemin_fichier = os.path.join(dossier, nom_fichier)

    if os.path.isfile(chemin_fichier):
        nom_president = extraire_nom_president(nom_fichier)
        print("Le fichier",nom_fichier," correspond au président ",nom_president)

def liste_noms_presidents(dossier):

    noms_presidents = []

    for nom_fichier in os.listdir(dossier):
        chemin_fichier = os.path.join(dossier, nom_fichier)

        if os.path.isfile(chemin_fichier):
            nom_president = extraire_nom_president(nom_fichier)

            if nom_president not in noms_presidents:
                noms_presidents.append(nom_president)

    return noms_presidents

noms_presidents = liste_noms_presidents("speeches")

print("Noms des présidents dans le dossier 'speeches':", noms_presidents)

def convertir_et_enregistrer_en_minuscules(dossier_entree, dossier_sortie):

    fichiers = os.listdir(dossier_entree)

    for fichier in fichiers:
        chemin_fichier_entree = os.path.join(dossier_entree, fichier)

        if os.path.isfile(chemin_fichier_entree):
            with open(chemin_fichier_entree, 'r') as file:
                contenu = file.read()
            contenu_minuscules = contenu.lower()
            chemin_fichier_sortie = os.path.join(dossier_sortie, fichier)

            with open(chemin_fichier_sortie, 'w') as file:
                file.write(contenu_minuscules)
            print("Le fichier",fichier,"a été converti et enregistré en minuscules.")

dossier_entree = 'speeches'
dossier_sortie = 'cleaned'

convertir_et_enregistrer_en_minuscules(dossier_entree, dossier_sortie)

def nettoyer_le_texte(dossier_entree, dossier_sortie):

    fichiers = os.listdir(dossier_entree)

    for fichier in fichiers:
        chemin_fichier_entree = os.path.join(dossier_entree, fichier)

        if os.path.isfile(chemin_fichier_entree):
            with open(chemin_fichier_entree, 'r') as file:
                contenu = file.read()
            contenu_nettoyer = contenu.replace("?", "").replace(",", "").replace("-", "").replace(".", "").replace("!", "").replace("'", "")
            chemin_fichier_sortie = os.path.join(dossier_sortie, fichier)

            with open(chemin_fichier_sortie, 'w') as file:
                file.write(contenu_nettoyer)
            print("Le fichier",fichier," a été nettoyer et enregistré .")

dossier_entree = 'cleaned'
dossier_sortie = 'cleaned'

nettoyer_le_texte(dossier_entree, dossier_sortie)


def IDF(directory):
    os.chdir(directory)
    nb_fichier=0
    texte=""
    nb_mots=0
    IDF_mots=0
    for fichier in os.listdir(directory):
        nb_fichier+=1
        dico={}
        with open(r'/Users/adrien/PycharmProjects/pychatbot-DAQUIN-CUVIER/cleaned/{files}'.format(file=files),"r")as file:
            texte+=file.read()
            file.close()
            for mots in text.split():
                if mots not in dico:
                    for files in os.listdir(directory):
                        with open(r'/Users/adrien/PycharmProjects/pychatbot-DAQUIN-CUVIER/cleaned/{files}'.format(file=files),"r")as file:
                            if mots in file.read():
                                nb_mots+=1

            IDF_mots=math.log((nb_fichier/nb_mots))
            nb_mots=0
            dico.update({mots:IDF_mots})
            return(dico)