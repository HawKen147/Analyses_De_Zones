import os       #accede aux parametre de l'os / dossier
import shutil   #permet la gestion de dossiers / fichiers

#Verifie que tout les fichiers soit bien correctement creer en verifiant si leur chemin existe
#Si les chemin existent, alors return true
def verifie_chemin_dossiers(path):
    if os.path.exists(path):
        if len(check_nb_folder(path)) > 0:
            return True
        else :
            return False

#Fonction qui verifie si il y a des fichiers dans le chemin spécifié
#retourne la liste des fichiers contenu dans le chemin spécifié
def check_nb_folder(path):
    list_fichiers = os.listdir(path)
    return list_fichiers
    
#Fonction qui verifie si le texte entré est un entier ou pas
#return true si le nombre entré est un entier
def verifie_str_is_int(texte):
    try:
        int(texte)
        return True
    except ValueError:
        return False
    
#fonction qui prend un chemin entrer par l'utilisateur
#crée les dossier pour stocker les videos des cameras qui ont été édité
def creer_dossier(nb_camera, path_dossier):
    nb_camera = int(nb_camera)
    i = 0
    for i in range(1, nb_camera + 1):
        j = str(i).zfill(2)  # Ajoute un zéro si i < 10
        cam_path = os.path.join(path_dossier, f"CAM_{j}")
        rampe_cam_path = os.path.join(cam_path, "rampe")
        courir_cam_path = os.path.join(cam_path, "courir")
        marche_cam_path = os.path.join(cam_path, "marche")
        # Créer les dossiers
        os.makedirs(cam_path)
        os.makedirs(rampe_cam_path)
        os.makedirs(courir_cam_path)
        os.makedirs(marche_cam_path)
        #creer le fichier txt pour dire si le fichier est complet ou pas
        txt_file = os.path.join(cam_path, "incomplet.txt")
        with open(txt_file, 'w') as fichier:
            fichier.write(" DM \n DC \n DR \n MM \n MC \n MR \n FM \n FC \n FR \n")
            pass  # Ne rien écrire dans le fichier

        #appel de fonction qui verifie si chaque fichier a bien été créer sinon retourne false 
        if not check_creation_folder(cam_path, rampe_cam_path, courir_cam_path, marche_cam_path, txt_file):
            return False
    return True

#Verifie que tout les fichiers soit bien correctement creer en verifiant si leurs chemins existent
#Si les chemins existent, alors return true sinon return false
def check_creation_folder(cam_path, rampe_cam_path, courir_cam_path, marche_cam_path, txt_file):
    if not(os.path.exists(cam_path) and os.path.exists(rampe_cam_path) and os.path.exists(courir_cam_path) and os.path.exists(marche_cam_path) and os.path.exists(txt_file)):
        return False
    else :
        return True
    

#Fonction qui va permetre de deplacer les videos dans les dossiers creer precedement
def get_video_cam_files(path_video_camera, path_folder_camera):
    list_video_err = []
    list_bad_extensions = []
    list_videos_cam = get_list_videos_cam(path_video_camera) #On recupere le nom de tout les fichiers videos qui sont dans le dossier
    for video_cam in list_videos_cam:
        list_name_video_cam = format_name_video(video_cam)
        if check_extension_folder(video_cam):
            res = move_video_to_folder(path_video_camera, path_folder_camera, video_cam, list_name_video_cam)
            if res == 1 :
                update_incomplet_txt(path_folder_camera, list_name_video_cam)
            else :
                list_video_err.append(video_cam)
        else :
            list_bad_extensions.append(video_cam)

    return list_video_err, list_bad_extensions

    
#Fonction qui déplace les videos dans les bon dossiers
def move_video_to_folder(path_video_camera, path_folder_camera, video_name, list_name_video_cam):
    type_passage, folder_cam = get_passage_cam_number(list_name_video_cam)
    if type_passage == False:
        return list_name_video_cam
    
    path_folder_camera += "\\" + folder_cam + "\\" + type_passage
    path_video_camera += "\\" + video_name
    if not os.path.exists(path_folder_camera):
        return path_folder_camera
    
    shutil.move(path_video_camera, path_folder_camera)
    return 1

    
def get_passage_cam_number(list_name_video_cam):
    try :
        numero_cam = list_name_video_cam[0][2:]
        folder_cam = "CAM_" + numero_cam
        type_passage = list_name_video_cam[-1][1]
        if type_passage == 'R':
            type_passage = "rampe"
            return type_passage , folder_cam
        elif type_passage == 'C':
            type_passage = "courir"
            return type_passage, folder_cam
        elif type_passage == "M":
            type_passage = "marche"
            return type_passage, folder_cam
        else:
            return False
    except :
        return False
    

#Fonction qui prend le nom entier du fichier video
#Met dans une liste le numero de la camera [0]
#Met le numero de la camera, la date, et debut, milieu, fin -> [numero_cam, jour/mois/année heure:min:00, DR.asf]
#Attention, si l'utilisateur n'a pas afficher les extensions de fichier, il y a un risque que cela ne marhce pas
def format_name_video(nom_video):
   try: 
        nom_video = nom_video.split("_")                    #sépare le tableau a chaque '_' dans le nom du fichier de la video
        nom_video_nCam_date = nom_video.pop(1).split("-")   #recupere et supprime la case 1 de la list creer precedement, sépare la chaine de caractere a chaque '-' et en creer un tableau
        numero_cam = nom_video_nCam_date.pop(0)             #recupere et supprime la 1ere case de la list (nom + numero de la camera) 
        date = "/".join(nom_video_nCam_date[::-1])          #Creer la chaine de caractere de la date, [2023,  09, 07] -> 07/09/2023
        heure = nom_video.pop(1)                            #recupere et supprime l'heure contenue dans nom_video
        heure = heure[0:5].replace('h',':')                 #Ne garde que l'heure et les min, remplace 'h' par ':' ; 10h42min44s990ms -> 10:42
        heure += ':00'                                      #ajoute a la fin de la chaine de caractere " :00"
        date += ' ' + heure                                 #concataine la date et l'heure
        type_fichier = nom_video[1]                         #recupere l"extension de video + debut,milieu,fin ...
        nom_video.clear()                                   #Vide nom_video car on a récuperé ce que l'on voulait
        nom_video.append(numero_cam)                        #puis on ajoute chaque variable dans la list nom_video
        nom_video.append(date)
        nom_video.append(type_fichier)
        return nom_video                                    #Retourne la liste creer precedement
   except :
       return nom_video
   
#retourne la liste des fichier contenu dans le chemin spécifié
def get_list_videos_cam(path):
    # Utilise la fonction os.listdir() pour obtenir la liste des fichiers dans le dossier
    fichiers = os.listdir(path)
    return fichiers

#Verfie que l'extension du fichier soit bien un fichier d'extension .asf
def check_extension_folder(video_cam):
    extension = video_cam.split('.')
    if extension[-1] == "asf":
        return True
    else:
        return False


def update_incomplet_txt(path, name_cam_folder):
    type_passage, numero_cam = get_passage_cam_number(name_cam_folder)
    type_passage = name_cam_folder[-1][:2]
    print(type_passage)
    path += "\\" + numero_cam + "\\" + "incomplet.txt"
    del_passage_type_txt(path, type_passage)
    

def del_passage_type_txt(fichier_path, ligne_a_supprimer):
    # Lecture du contenu du fichier
    with open(fichier_path, 'r') as fichier:
        lignes = fichier.readlines()
        print("Contenu avant suppression :")
        for ligne in lignes:
            print(ligne.strip())

    # Suppression de la ligne 
    nouvelle_ligne = [ligne for ligne in lignes if ligne.strip() != ligne_a_supprimer]
    print(f"nouvelle ligne = {nouvelle_ligne}")

    # Écriture du nouveau contenu dans le fichier
    with open(fichier_path, 'w') as fichier:
        fichier.writelines(nouvelle_ligne)

        
def check_folders(path):
    print('ok')

