import shutil   #permet la gestion de dossiers / fichiers
import os       #accede aux parametre de l'os / dossier


#Verifie que tout les fichiers soient bien correctement créé en verifiant si leurs chemins existent
#Si les chemins existent, alors return true
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
    
#fonction qui prend un chemin entré par l'utilisateur
#crée les dossiers pour stocker les videos des cameras qui ont été édité
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
    list_video_err_double = []
    list_videos_cam = get_list_videos_cam(path_video_camera) #On recupere le nom de tout les fichiers videos qui sont dans le dossier des vidéos exportées
    for video_cam in list_videos_cam:
        list_name_video_cam = format_name_video(video_cam)
        if check_extension_folder(video_cam):
            res = move_video_to_folder(path_video_camera, path_folder_camera, video_cam, list_name_video_cam)
            if res == True :
                update_incomplet_txt(path_folder_camera, list_name_video_cam)
            elif res == 2 :
                list_video_err_double.append(video_cam)
            else :
                list_video_err.append(video_cam)
        else :
            list_bad_extensions.append(video_cam)
    return list_video_err, list_bad_extensions, list_video_err_double

    
#Fonction qui déplace les videos dans les bon dossiers
def move_video_to_folder(path_video_camera, path_folder_camera, video_name, list_name_video_cam):
    if get_passage_cam_number(list_name_video_cam) == False:
        return list_name_video_cam
    else :
        type_passage, folder_cam = get_passage_cam_number(list_name_video_cam)
        path_folder_camera += f"\\{folder_cam}\\{type_passage}"
        path_video_camera += f"\\{video_name}"
        if not os.path.exists(path_folder_camera):
            return path_folder_camera

        if check_file_exists(list_name_video_cam, path_folder_camera) != False:    #Si le fichier n'est pas dans le dossier on déplace le fichier
            shutil.move(path_video_camera, path_folder_camera)
            return True
        else :
            return 2

#Retourne le type de passage selon la lettre dans le nom du fichier
def get_passage_cam_number(list_name_video_cam):
    try :
        numero_cam = list_name_video_cam[0]
        folder_cam = f"CAM_{numero_cam}"
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
#Met le numero de la camera, la date, et debut, milieu, fin -> [numero_cam, DR.asf]
def format_name_video(nom_video):
   try: 
        for i in range(len(nom_video)):
            if nom_video[i:i+2] == "TH" and nom_video[i + 2].isdigit() and nom_video[i + 3].isdigit():      #vérifie que ce soit bien une camera thermique avec les numeros (THXX) peu import les numeros
                numero_cam = nom_video[i+2:i+4]     #Récupere le numéro de camera
        nom_video = nom_video.split("_")                    #sépare le tableau a chaque '_' dans le nom du fichier de la video              
        type_fichier = nom_video[-1]                        #recupere l"extension de video + debut,milieu,fin ...
        nom_video.clear()                                   #Vide nom_video car on a récuperé ce que l'on voulait
        nom_video.append(numero_cam)                        #puis on ajoute chaque variable dans la list nom_video
        nom_video.append(type_fichier)
        return nom_video                                    #Retourne la liste créer precedement
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

#met a jour le fichier incomplet.txt
def update_incomplet_txt(path, name_cam_folder):
    type_passage, numero_cam = get_passage_cam_number(name_cam_folder)
    type_passage = name_cam_folder[-1][:2]
    path += f"/{numero_cam}/incomplet.txt"
    del_passage_type_txt(path, type_passage)

#supprime le passage dans le dossier incomplet.txt
def del_passage_type_txt(fichier_path, ligne_a_supprimer):
    # Lecture du contenu du fichier
    with open(fichier_path, 'r') as fichier:
        lignes = fichier.readlines()
    # Suppression de la ligne 
    nouvelle_ligne = [ligne for ligne in lignes if ligne.strip() != ligne_a_supprimer]
    # Écriture du nouveau contenu dans le fichier
    with open(fichier_path, 'w') as fichier:
        fichier.writelines(nouvelle_ligne)

#Fonction qui permet d'afficher les fichiers manquants en récuperant les lignes du fichiers incomplet.txt  
def check_folders(path):
    if verifie_chemin_dossiers(path):
        check_dictionnary = {}
        txt_file = path + "\\incomplet.txt"
        list_fichiers = os.listdir(path)
        for folder in list_fichiers:
            if folder[0:4] == "CAM_":
                txt_file = f"{path}\\{folder}\\incomplet.txt"
                with open(txt_file, 'r') as fichier:
                    contenu = fichier.read()
                    contenu_sans_espaces = contenu.replace('\n', '')
                    check_dictionnary[folder] = contenu_sans_espaces
        check_dictionnary = check_value_dict(check_dictionnary)
        return check_dictionnary
    else:
        return False

#Si le fichier incompelt.txt est vide, retourne "le dossier est complet" pour la camera xx 
def check_value_dict(dict_check):
    for cle,valeur in dict_check.items():
        if valeur == '':
            dict_check[cle] = "le dossier est complet"
    return dict_check


#Fonction qui vérifie si le fichier a déplacer existe déjà ou pas
def check_file_exists(file_name, path_to_folder):
    files_in_directory = os.listdir(f"{path_to_folder}\\")
    for file in files_in_directory:
        if file_name[-1] in file:
            return False
        

#Fonction qui récupere le nombre de camera
def get_nb_camera(path_to_folders):
    nombre_de_dossiers = 0
    elements = os.listdir(path_to_folders)
    for element in elements:
        # Vérifier si l'élément est un dossier
        if os.path.isdir(os.path.join(path_to_folders, element)):
            nombre_de_dossiers += 1
    return nombre_de_dossiers

#Fonction qui retourne toutes les videos présentes (seulement l'heure de chaque clips)
def get_videos_clips(path_to_folders):
    tab_clips = []
    elements = os.listdir(path_to_folders)
    for cam in elements:
        type_passage = os.listdir(f"{path_to_folders}/{cam}")
        for passage in type_passage :
            if os.path.isdir(f"{path_to_folders}/{cam}/{passage}") and len(os.listdir(f"{path_to_folders}/{cam}/{passage}")) > 0 :
                clips = os.listdir(f"{path_to_folders}/{cam}/{passage}")
                for clip in clips:
                    tab_clips.append(clip)
    return tab_clips

#transforme la date englaise en francais
#Fonction temporaire dans l'attente d'un fixe pour la variable locale
#prend en parametre le date entière
def date_eng_to_fr (date_time):
    date_time = date_time.split(" ")
    eng_to_fr_day(date_time)
    eng_to_fr_month(date_time)
    date_str = tab_date_to_str(date_time)
    return date_str

#Traduis le jour anglais en jour francais
def eng_to_fr_day(day):
    match day[0]:
        case "Monday" :
            day[0] = "Lundi"
            return day
        case "Tuesday" :
            day[0] = "Mardi"
            return day
        case "Wednesday" :
            day[0] = "Mercredi"
            return day
        case "Thursday":
            day[0] = "Jeudi"
            return day
        case "Friday" :
            day[0] = "Vendredi"
            return day
        case "Saturday" :
            day[0] = "Samedi"
            return day
        case "Sunday" :
            day[0] = "Dimanche"
            return day
        case _ :
            print("c'est quoi ce bordel")

#Traduis le mois anglais en mois francais
def eng_to_fr_month(month):
    match month[2]:
        case "January" :
            month[2] = "Janvier"
            return month
        case "February" :
            month[2] = "Février"
            return month
        case "March" :
            month[2] = "Mars"
            return month
        case "April":
            month[2] = "Avril"
            return month
        case "May" :
            month[2] = "Mai"
            return month
        case "June" :
            month[2] = "Juin"
            return month
        case "July" :
            month[2] = "Juillet"
            return month
        case "August" :
            month[2] = "Aout"
            return month
        case "September" :
            month[2] = "Septembre"
            return month
        case "October":
            month[2] = "Octobre"
            return month
        case "November" :
            month[2] = "Novembre"
            return month
        case "December" :
            month[2] = "Décembre"
            return month
        case _ :
           print("je comprends pas")
        
#Transforme la tableau de date en string
def tab_date_to_str(date_time):
    date_str = ""
    for date in date_time:
        date_str += date + " "
    return date_str