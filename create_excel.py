import openpyxl
from openpyxl import load_workbook
import os
import fonctions


def parcour_num_cam_excel (num_cam, sheet):
    # Parcourir la colonne B (index 2) à partir de la ligne 2 (en supposant que les en-têtes sont à la ligne 4)
    for cell in sheet.iter_rows(min_row=5, min_col=2, max_col=2):
        # Accéder à la valeur de la cellule actuelle
        valeur_cellule = cell[0].value  # Fonctionne si la cellule n'est pas vide
        print(valeur_cellule)

def colonne_passage_excel(type_passage):
    match type_passage:
        case "DM" :
            return 'C'
        case "DC":
            return 'E'
        case "DR":
            return 'G'
        case "MM":
            return 'I'
        case "MC":
            return 'K'
        case "MR" :
            return 'M'
        case "FM" :
            return 'P'
        case "FC" :
            return 'Q'
        case "FR" :
            return 'S'
        case _:
            print(f"le type de passage rejeté {type_passage}")
            return False
        
def recuperer_heure_passage(nom_clip):
    pass

# Chemin du fichier Excel final
new_excel_file = "./excel/final/Essaies_Zones.xlsx"

# Charger le classeur Excel existant
workbook = load_workbook("./excel/model/model.xlsx")

# Sélectionnez la feuille active
sheet = workbook.active

# Vérifier si le fichier final existe, si oui, renommer en conséquence
i = 0
while True:
    i += 1
    if not os.path.isfile(new_excel_file):
        break
    else:
        new_excel_file = f"./excel/final/Essaies_Zones({i}).xlsx"

path_to_folder = "C:/Users/pierry.benoit/Documents/dossiers_camera"

# Obtenir le nombre de caméras
nb_camera = fonctions.get_nb_camera(path_to_folder)

# Insérer les données dans la feuille de calcul
for i in range(1, nb_camera + 1):
    sheet[f'B{i + 4}'] = i

#recupere tous les clips videos dans un tableau [[clip_ramper_1, clip_ramper_2, clip_ramper_3], [clip_marcher_1, clip_marcher_2, clip_marcher_3]...]
clips = fonctions.get_videos_clips(path_to_folder)


#On parcourt tout les clips
for clip in clips :
    try :
        for i in range (3):         #Chaque clip est dans une liste de 3
            nom_clip = clip[i]
            index_numero_cam = nom_clip.find("TH")                              #Index ou se situe TH (récuperer l'index de T)
            numero_cam = nom_clip[index_numero_cam+2:index_numero_cam+4]        #On recupere l'indice ou se situe TH et on récupere les 2 chiffres apres TH
            ligne_excel = int(numero_cam) + 4
            type_de_passage = nom_clip[-6:-4]
            colonne_excel = colonne_passage_excel(type_de_passage)
            sheet[f"{colonne_excel}{ligne_excel}"] = nom_clip

    except Exception :
        print(Exception)






# Enregistrer le classeur Excel
workbook.save(new_excel_file)
