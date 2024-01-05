def del_passage_type_txt(fichier_path, ligne_a_supprimer):
    with open(fichier_path, 'r') as fichier:
        lignes = fichier.readlines()

    # Supprime la ligne spécifique
    lignes = [ligne for ligne in lignes if ligne.strip() != ligne_a_supprimer]

    with open(fichier_path, 'w') as fichier:
        fichier.writelines(lignes)
        
        
#chemin_fichier = "C:\Users\pierry.benoit\Documents\dossiers_camera\CAM_14"
ligne_a_supprimer = "FC"
path = "C:\\Users\\pierry.benoit\\Documents\dossiers_camera\\CAM_14\\incomplet.txt"

# Lecture du contenu du fichier
with open(path, 'r') as fichier:
    lignes = fichier.readlines()

# Suppression de la ligne contenant "FR"
nouvelles_lignes = [ligne for ligne in lignes if ligne_a_supprimer not in ligne]

# Écriture du nouveau contenu dans le fichier
with open(path, 'w') as fichier:
    fichier.writelines(nouvelles_lignes)

print(f"La ligne contenant {ligne_a_supprimer} a été supprimée.")