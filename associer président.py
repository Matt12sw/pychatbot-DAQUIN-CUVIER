import os
def extraire_nom_president(nom_fichier):
    # Supprimer le préfixe "Nomination_" et l'extension ".txt" du nom du fichier
    nom_president = nom_fichier.replace("Nomination_", "").replace(".txt", "").replace("1", "").replace("2", "")
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


def read_speech(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def get_president_first_name(president_name):
    # Ajoutez ici la correspondance entre le nom et le prénom de chaque président
    president_names_mapping = {
        "Chirac": "Jacques",
        "Giscrad_dEstaing": "Valéry",
        "Mitterrand": "François",
        "Macron": "Emmanuel",
        "Sarkozy": "Nicolas"
    }

    return president_names_mapping.get(president_name, "Inconnu")


def main():
    directory = "speeches"
    presidents = ["Chirac", "Giscrad_dEstaing", "Mitterrand", "Macron", "Sarkozy"]

    for president in presidents:
        for file_name in os.listdir(directory):
            if president in file_name:
                file_path = os.path.join(directory, file_name)
                speech_content = read_speech(file_path)

                # Obtenez le prénom du président
                president_first_name = get_president_first_name(president)

                # Vous pouvez faire quelque chose avec le prénom du président et le contenu du discours ici
                # Par exemple, imprimer le prénom, le nom du président et le contenu du discours
                print(f"Président: {president_first_name} {president}")
                print(f"Contenu du discours:\n{speech_content}")
                print("=" * 50)


if __name__ == "__main__":
    main()



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

def convertir_et_enregistrer_en_minuscules(dossier_entree, dossier_sortie):


    # Liste des fichiers dans le dossier d'entrée
    fichiers = os.listdir(dossier_entree)

    for fichier in fichiers:
        chemin_fichier_entree = os.path.join(dossier_entree, fichier)

        # Vérifiez si le chemin est un fichier
        if os.path.isfile(chemin_fichier_entree):
            with open(chemin_fichier_entree, 'r') as file:
                contenu = file.read()

            # Convertir le contenu en minuscules
            contenu_minuscules = contenu.lower()

            # Créer le chemin du fichier de sortie
            chemin_fichier_sortie = os.path.join(dossier_sortie, fichier)

            # Enregistrer le fichier en minuscules dans le dossier de sortie
            with open(chemin_fichier_sortie, 'w') as file:
                file.write(contenu_minuscules)

            print(f'Le fichier {fichier} a été converti et enregistré en minuscules.')

# Utilisation de la fonction
dossier_entree = 'speeches'
dossier_sortie = 'cleaned'

convertir_et_enregistrer_en_minuscules(dossier_entree, dossier_sortie)

import os
import string

def clean_text(text):
    #  On supprime certain caractères de ponctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    # On remplace l'apostrophe et le tiret par du vide
    cleaned_text = cleaned_text.replace("’", " ").replace("-", " ")

    return cleaned_text

def clean_and_save_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
        cleaned_text = clean_text(text)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)

def clean_files(directory):
    if not os.path.exists("cleaned"):
        os.makedirs("cleaned")

    for file_name in os.listdir(directory):
        input_path = os.path.join(directory, file_name)
        output_path = os.path.join("cleaned", file_name)

        clean_and_save_file(input_path, output_path)

def main():
    directory = "speeches"
    clean_files(directory)
    print("Nettoyage terminé.")

if __name__ == "__main__":
    main()
    