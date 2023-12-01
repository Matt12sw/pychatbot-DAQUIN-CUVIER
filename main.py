#madeleines
import os
def extraire_nom_president(nom_fichier):
    # Supprimer le préfixe "Nomination_" et l'extension ".txt" du nom du fichier
    nom_president = nom_fichier.replace("Nomination_", "").replace(".txt", "")
    return nom_president

# Chemin du dossier contenant les fichiers
dossier = "speeches"

# Parcourir tous les fichiers dans le dossier
for nom_fichier in os.listdir(dossier):
    chemin_fichier = os.path.join(dossier, nom_fichier)

    # Vérifier si le chemin correspond à un fichier (et non à un sous-dossier)
    if os.path.isfile(chemin_fichier):
        # Extraire le nom du président à partir du nom du fichier
        nom_president = extraire_nom_president(nom_fichier)

        # Afficher le nom du président associé à chaque fichier
        print(f"Le fichier {nom_fichier} correspond au président {nom_president}")


def liste_noms_presidents(dossier):
    # Initialiser une liste pour stocker les noms des présidents
    noms_presidents = []

    # Parcourir tous les fichiers dans le dossier
    for nom_fichier in os.listdir(dossier):
        chemin_fichier = os.path.join(dossier, nom_fichier)

        # Vérifier si le chemin correspond à un fichier (et non à un sous-dossier)
        if os.path.isfile(chemin_fichier):
            # Extraire le nom du président à partir du nom du fichier
            nom_president = extraire_nom_president(nom_fichier)

            # Ajouter le nom du président à la liste s'il n'est pas déjà présent
            if nom_president not in noms_presidents:
                noms_presidents.append(nom_president)

    return noms_presidents

# Appeler la fonction pour obtenir la liste des noms des présidents dans le dossier "speeches"
noms_presidents = liste_noms_presidents("speeches")

# Afficher la liste des noms des présidents
print("Noms des présidents dans le dossier 'speeches':", noms_presidents)
