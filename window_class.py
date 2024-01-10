import tkinter
import os
import fonctions
import tkinter.messagebox
import customtkinter

#Faire la fonction check folders
#Faire la fonction qui update le fichier texte lorsqu'un nouveau fichier est ajouté.
#avant d'ajouter le fichier, il faut verifier si le fichier est deja existant. de toute facon si il est deja existant le fichier n'est pas déplacer mais creer une erreur


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

width = 825
height = 500

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Move Folder")
        self.minsize(825,500)
        self.geometry(f"{width}x{height}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Essaies Zones")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Analyse de vie")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))


        #Main : Essaies Zones
        self.intro_label = customtkinter.CTkLabel(self, width=350, anchor='center', text="Pour commencer, choisissez si vous voulez créer les fichiers afin de mettre les vidéos des cameras dedans. \n Ensuite, assurez vous que le dossier fournis soit vide pour créer les dossiers des caméras. \n Enfin donnez le chemin des vidéos pour quelles soient deplacés dans les dossiers crée précédement. \n Le nom des vidéos doivent êtres comme suis : 'Nom_THXX-aaaa-mm-jj_10h44min02s083ms_DM.asf'. \n THXX avec XX le numero de la camera (00 à <99) ")
        self.creation_dossiers_label = customtkinter.CTkLabel(self, anchor='center', text="Arborescence des dossiers créer :\n CAM_XX \n         |_rampe \n        |_courir \n           |_marche \n                    |_incomplet.txt")
        self.nb_camera_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Nombre de dossier à créer")
        checked = customtkinter.IntVar()
        self.verification_checkbox = customtkinter.CTkCheckBox(self, variable=checked, onvalue=True, offvalue=False, text="Cocher pour voir les fichiers manquants", command=self.valider_button_event)
        self.chemin_dossier_label = customtkinter.CTkLabel(self, anchor='center', text="Entrer le chemin pour créer / stocker les vidéos")
        self.chemin_video_label = customtkinter.CTkLabel(self, anchor='center', text="Entrer le chemin pour récupérer les vidéos de surveillance")
        self.chemin_dossier_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Chemin pour stocker les vidéos")
        self.chemin_video_entry = customtkinter.CTkEntry(self, width=250, placeholder_text="Chemin pour récupérer les vidéos")
        self.valider_button = customtkinter.CTkButton(self, anchor='center', text="Valider", command=self.main_button_event)
    
        #position of the main_frame_widgets
        self.intro_label.grid(row=0, column=1, pady=(50,0), padx=5, sticky="nswe")
        self.creation_dossiers_label.grid(row=1,column=1, sticky="nsew")
        self.nb_camera_entry.grid(row=2, column=1, pady=(0,5))
        self.verification_checkbox.grid(row=3, column=1)
        self.chemin_dossier_label.grid(row=4, column=1, pady=(5,0), sticky="nsew")
        self.chemin_dossier_entry.grid(row=5, column=1, pady=(0,5))
        self.chemin_video_label.grid(row=6, column=1, pady=(5,0), sticky="nsew")
        self.chemin_video_entry.grid(row=7, column=1, pady=(0,5))
        self.valider_button.grid(row=8,column=1, pady=5)

        #definition initial state       
        self.valider_button.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.bind_all("<KeyPress>", self.functions_calls)

    #Check if the given path exits
    def check_path(self, path):
        if ((os.path.exists(path) or path == '')):
            return True
        else :
            return False
    
    #Get the entrys for the number of cameras, path to get the videos, path to stock the videos and the checkbox state
    def get_entrys(self):
        nb_camera = self.nb_camera_entry.get()
        chemin_stocker = self.chemin_dossier_entry.get()
        chemin_get_videos = self.chemin_video_entry.get()
        check_folders_checkbox = self.verification_checkbox.get()
        if check_folders_checkbox:
            return True
        elif nb_camera.isdigit() and os.path.exists(chemin_stocker) and len(os.listdir(chemin_stocker)) == 0 and chemin_get_videos == '' and not check_folders_checkbox :          # Verifier si nb_camera est bien un entier, si le chemin rensigner est existant et si le chemin renseigner est vide, si il n'y a rien d'entré dans lentré des videos surveillances et si la checkbox est bien décocher.
            return True
        elif nb_camera == '' and os.path.exists(chemin_stocker) and len(os.listdir(chemin_stocker)) > 0 and  os.path.exists(chemin_get_videos) and len(os.listdir(chemin_get_videos)) > 0 and not check_folders_checkbox :   #verifie si le nb de camera est null, si le chemin stocker existe et n'est pas vide, si le chemin pour les videos existe bien et n'est pas vide, si la checkbox n'est pas coché.
            return True
        
    #Change the button state (normal or disabled)
    def valider_button_event(self):
        bool = self.get_entrys()            #Get if the checkbox is checked
        if bool :
            self.valider_button.configure(state="normal")
        else :
            self.valider_button.configure(state="disabled")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")   
        
    def main_button_event(self):
        nb_camera = self.nb_camera_entry.get()
        chemin_stocker = self.chemin_dossier_entry.get()
        chemin_get_videos = self.chemin_video_entry.get()
        if self.verification_checkbox.get() and chemin_stocker != "":
            #appel la fonction pour verifier tous les fichiers
            dict_check = fonctions.check_folders(chemin_stocker)
            self.win_err(dict_check=dict_check)
        elif nb_camera != '' and chemin_stocker!= '':
            #appel la fonction pour créer les dossiers
            if (fonctions.creer_dossier(nb_camera, chemin_stocker)):
                self.win_err(no_err='no_err')
            else :
                self.win_err(simple_err = 'simple_err')

        elif chemin_stocker != '' and chemin_get_videos != '':
            #appel la fonction pour déplacer les videos des cameras
            list_video_err, list_bad_extensions = fonctions.get_video_cam_files(chemin_get_videos, chemin_stocker)
            if (list_video_err or list_bad_extensions):
                self.win_err(list_video_err=list_video_err, list_bad_extensions=list_bad_extensions)
            else :
                self.win_err(no_err = 'no_err')
    
    def functions_calls(self, event):
       self.valider_button_event()


    def win_err(self, **kwargs):
        # Utilisez self.err_window pour définir la fenêtre
        self.err_window = customtkinter.CTkToplevel(self)
        self.err_window.title("Erreurs")
        self.err_window.minsize(300,200)
        # Define the 2nd window with grid configuration
        self.err_window.grid_columnconfigure(0, weight=1)
        
        # Ajouter des widgets à la deuxième fenêtre
        if 'string_list_bad_extensions'and 'string_list_video_err' in kwargs:
            list_bad_extensions = kwargs['string_list_bad_extensions']
            list_video_err = kwargs['string_list_video_err']
            print(list_bad_extensions, list_video_err)
            self.err_window.grid_rowconfigure((0,1,2,3,4), weight=1)
            string_list_bad_extensions = '\n'.join(list_bad_extensions)
            string_list_video_err = '\n'.join(list_video_err)
            label_err_extension = customtkinter.CTkLabel(self.err_window, text="Liste des erreurs du à une mauvaise extension de fichier : ")
            label_err_folder_extension = customtkinter.CTkLabel(self.err_window,text_color='red', text=string_list_bad_extensions)
            label_err_video = customtkinter.CTkLabel(self.err_window, text="Liste des fichiers qui n'ont pas pu être déplacé : ")
            label_string_list_video_err = customtkinter.CTkLabel(self.err_window,text_color='red', text=string_list_video_err)
            label_err_extension.grid(row=0, column=0, pady=(20,5), padx=20)
            label_err_folder_extension.grid(row=1, column=0, pady=5)
            label_err_video.grid(row=2, column=0, pady=(20,5))
            label_string_list_video_err.grid(row=3, column=0, pady=5)
            button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            button_quit.grid(row=4, column=0, pady=5)
        elif 'dict_check' in kwargs:
            err_str = ''
            self.err_window.grid_rowconfigure((0,1,2), weight=1)
            dict_check = kwargs.get('dict_check', {})
            for key, value in dict_check.items():
                err_str += key + ' ' + value + '\n'
            label_titre = customtkinter.CTkLabel(self.err_window,text="Liste des fichiers manquants pour chaque dossiers")
            label_no_err = customtkinter.CTkLabel(self.err_window, text=err_str)
            button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            label_titre.grid(row=0, column=0, pady=(20,5), padx=20)
            label_no_err.grid(row=1, column=0, pady=(20,5), padx=20, sticky='w')
            button_quit.grid(row=2, column=0, pady=5)
            pass
        elif 'no_err' in kwargs:
            self.err_window.grid_rowconfigure((0,1), weight=1)
            label_no_err = customtkinter.CTkLabel(self.err_window, text="Aucune erreur détecté", text_color="#40f561")
            button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            label_no_err.grid(row=0, column=0, pady=(20,5), padx=20)
            button_quit.grid(row=1, column=0, pady=5)
        elif 'simple_err' in kwargs:
            self.err_window.grid_rowconfigure((0,1), weight=1)
            label_no_err = customtkinter.CTkLabel(self.err_window, text="Un problème est survenue lors de la création des dossiers", text_color="red")
            button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            label_no_err.grid(row=0, column=0, pady=(20,5), padx=20)
            button_quit.grid(row=1, column=0, pady=5)
        
        self.err_window.attributes('-topmost', True)
        self.err_window.lift()

    
    
    #Fonction to open the 2nd window to show errors while moving files
    def open_err_window(self, list_video_err, list_bad_extensions):
        string_list_bad_extensions = '\n'.join(list_bad_extensions)
        string_list_video_err = '\n'.join(list_video_err)
        
        # Utilisez self.err_window pour définir la fenêtre
        self.err_window = customtkinter.CTkToplevel(self)
        self.err_window.title("Erreurs")
    
        # Define the 2nd window with grid configuration
        self.err_window.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.err_window.grid_columnconfigure(0, weight=1)
        
        # Ajouter des widgets à la deuxième fenêtre
        label_err_extension = customtkinter.CTkLabel(self.err_window, text="Liste des erreurs du à une mauvaise extension de fichier : ")
        label_err_folder_extension = customtkinter.CTkLabel(self.err_window,text_color='red', text=string_list_bad_extensions)
        label_err_video = customtkinter.CTkLabel(self.err_window, text="Liste des fichiers qui n'ont pas pu être déplacé : ")
        label_string_list_video_err = customtkinter.CTkLabel(self.err_window,text_color='red', text=string_list_video_err)
        button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
        label_err_extension.grid(row=0, column=0, pady=(20,5), padx=20)
        label_err_folder_extension.grid(row=1, column=0, pady=5)
        label_err_video.grid(row=2, column=0, pady=(20,5))
        label_string_list_video_err.grid(row=3, column=0, pady=5)
        button_quit.grid(row=4, column=0, pady=5)
        
        self.err_window.attributes('-topmost', True)
        self.err_window.lift()

    def open_no_err_window(self):        
        # Utilisez self.err_window pour définir la fenêtre
        self.no_err_window = customtkinter.CTkToplevel(self)
        self.no_err_window.title("Erreurs")
        no_err_window_width = 220
        no_err_window_height = 100

        # Define the 2nd window with grid configuration
        self.no_err_window.grid_rowconfigure((0,1), weight=1)
        self.no_err_window.grid_columnconfigure(0, weight=1)
        
        # Ajouter des widgets à la deuxième fenêtre
        label_no_err = customtkinter.CTkLabel(self.no_err_window, text="Aucune erreur détecté", text_color="#40f561")
        button_quit = customtkinter.CTkButton(self.no_err_window, text="OK", command=self.close_window)
        label_no_err.grid(row=0, column=0, pady=(20,5), padx=20)
        button_quit.grid(row=1, column=0, pady=5)

        # Définir les coordonnées de la fenêtre au centre de l'écran
        x, y = self.window_center(no_err_window_width, no_err_window_height)
        print(f"x = {x} y = {y}")
        self.no_err_window.geometry(f"{no_err_window_width}x{no_err_window_height}+{x}+{y}")
        
        self.no_err_window.attributes('-topmost', True)
        self.no_err_window.lift()


    def open_simple_err_window(self):
                # Utilisez self.err_window pour définir la fenêtre
        self.simple_err_window = customtkinter.CTkToplevel(self)
        self.simple_err_window.title("Erreurs")
        simple_err_window_width = 220
        simple_err_window_height = 100

        # Define the 2nd window with grid configuration
        self.simple_err_window.grid_rowconfigure((0,1), weight=1)
        self.simple_err_window.grid_columnconfigure(0, weight=1)
        
        # Ajouter des widgets à la deuxième fenêtre
        label_no_err = customtkinter.CTkLabel(self.simple_err_window, text="Un problème est survenue lors de la création des dossiers", text_color="red")
        button_quit = customtkinter.CTkButton(self.simple_err_window, text="OK", command=self.close_window)
        label_no_err.grid(row=0, column=0, pady=(20,5), padx=20)
        button_quit.grid(row=1, column=0, pady=5)

        # Définir les coordonnées de la fenêtre au centre de l'écran
        x, y = self.window_center(simple_err_window_width, simple_err_window_height)
        self.simple_err_window_height.geometry(f"{simple_err_window_width}x{simple_err_window_height}+{x}+{y}")
        
        self.simple_err_window_height.attributes('-topmost', True)
        self.simple_err_window_height.lift()

    #ferme la bonne fenetre correspondante
    def close_window(self):
        if hasattr(self, 'err_window') and self.err_window:
            self.err_window.destroy()
        elif hasattr(self, 'no_err_window') and self.no_err_window:
            self.no_err_window.destroy()
        elif hasattr(self, 'simple_err_window') and self.simple_err_window:
            self.simple_err_window.destroy()

    def window_center(self,window_width, window_height):
        # Obtenez les dimensions de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculer les coordonnées pour centrer la fenêtre
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        return x,y

if __name__ == "__main__":
    app = App()
    app.mainloop()
