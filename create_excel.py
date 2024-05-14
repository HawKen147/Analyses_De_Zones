import openpyxl
from openpyxl import load_workbook
import os
import fonctions

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

#recupere tous les clips videos dans un tableau [[clip_ramper_1, clip_ramper_2, clip_ramper_3], [clip_marcher_1, clip_marcher_2, clip_marcher_3]...]
clips = fonctions.get_videos_clips(path_to_folder)

for clip in clips :
    try :
        for i in range (3):
            print(clip[i])
    except Exception :
        print(Exception)
        print("")

#print(clips)

# Insérer les données dans la feuille de calcul
for i in range(1, nb_camera + 1):
    sheet[f'B{i + 4}'] = i

# Enregistrer le classeur Excel
workbook.save(new_excel_file)
