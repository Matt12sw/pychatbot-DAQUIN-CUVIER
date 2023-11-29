import os

def extraire_et_renommer_president(nom_fichier):
    # Liste des noms de présidents
    presidents = ["Chirac", "Giscard d'Estaing", "Mitterrand", "Macron", "Sarkozy"]

    # Extraire le nom du président à partir du nom du fichier
    nom_president = nom_fichier.split("_")[1]

    # Vérifier si le nom du président extrait est dans la liste des noms de présidents
    if nom_president in presidents:
        # Construire le nouveau nom du fichier en remplaçant le numéro optionnel par le nom du président
        nouveau_nom = f"{nom_fichier.split('_')[0]}_{nom_president}{nom_fichier.split('_')[2]}"

        # Construire le chemin complet du fichier actuel et du nouveau fichier
        chemin_actuel = os.path.join("speeches", nom_fichier)
        chemin_nouveau = os.path.join("speeches", nouveau_nom)

        # Renommer le fichier
        os.rename(chemin_actuel, chemin_nouveau)

        print(f"Le fichier {nom_fichier} a été renommé en {nouveau_nom}")


# Se déplacer dans le répertoire "speeches"
os.chdir("speeches")

# Parcourir tous les fichiers dans le répertoire
for nom_fichier in os.listdir("."):
    extraire_et_renommer_president(nom_fichier)

# Afficher le nouveau nom de chaque fichier à la fin
print("\nNouveaux noms des fichiers :")
for nom_fichier in os.listdir("."):
    print(nom_fichier)