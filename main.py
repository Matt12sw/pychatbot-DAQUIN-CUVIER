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
