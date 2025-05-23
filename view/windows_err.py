import customtkinter

#Class qui définit la fenetre des erreurs
class window_err(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__()
        
    def win_err(self, **kwargs):
        self.err_window = customtkinter.CTkToplevel(self)
        self.err_window.title("Erreurs déplacement des fichiers")
        self.err_window.minsize(300,200)
        self.err_window.grid_columnconfigure(0, weight=1)
        #On créer la fenetre erreur, selon les kwargs
        ####################################################
        ### Trouver un moyen de rendre cela plus lisible ###
        ####################################################
        #Créé la fenêtre d'erreur qui affiche si les fichiers on une mauvaise extension / en double / pas pu etre déplacé
        if 'list_bad_extensions' in kwargs and 'list_video_err' in kwargs:
            list_bad_extensions = kwargs['list_bad_extensions']
            list_video_err = kwargs['list_video_err']
            list_video_err_double = kwargs['list_video_err_double']
            self.err_window.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)          
            string_list_bad_extensions = '\n'.join(list_bad_extensions)
            string_list_video_err = '\n'.join(list_video_err)
            string_list_video_err_double = '\n'.join(list_video_err_double)
            label_err_extension = customtkinter.CTkLabel(self.err_window, text="Liste des erreurs dû à une mauvaise extension de fichier : ")
            label_err_folder_extension = customtkinter.CTkLabel(self.err_window,text_color='red', text=string_list_bad_extensions)
            label_list_video_err_double = customtkinter.CTkLabel(self.err_window, text="Liste des fichiers en doubles : ")
            label_string_video_err_double = customtkinter.CTkLabel(self.err_window,text_color='red', text=string_list_video_err_double)
            label_err_video = customtkinter.CTkLabel(self.err_window, text="Liste des fichiers qui n'ont pas pu être déplacé : ")
            label_string_list_video_err = customtkinter.CTkLabel(self.err_window,text_color='red', text=string_list_video_err)
            label_err_extension.grid(row=0, column=0, pady=(20,5), padx=20)
            label_err_folder_extension.grid(row=1, column=0, pady=5)
            label_list_video_err_double.grid(row=2, column=0, pady=(20,5))
            label_string_video_err_double.grid(row=3,column=0, pady=5)            
            label_err_video.grid(row=4, column=0, pady=(20,5))
            label_string_list_video_err.grid(row=5, column=0, pady=5)
            button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            button_quit.grid(row=6, column=0, pady=5)
        #Créé la fenêtre d'erreur qui affiche les erreurs liées aux fichiers manquants lorsque l'on check si tout les fichiers vidéos sont présents
        elif 'dict_check' in kwargs:
            dict_check = kwargs.get('dict_check', {})
            err_str = ''
            self.err_window.grid_rowconfigure((0,1,2), weight=1)
            for key, value in dict_check.items():
                err_str += key + ' ' + value + '\n'
            label_titre = customtkinter.CTkLabel(self.err_window,text="Liste des fichiers manquants pour chaque dossiers")
            label_no_err = customtkinter.CTkLabel(self.err_window, text=err_str)
            button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            label_titre.grid(row=0, column=0, pady=(20,5), padx=20)
            label_no_err.grid(row=1, column=0, pady=(20,5), padx=20, sticky='w')
            button_quit.grid(row=2, column=0, pady=5)
        #Créé la fenêtre d'erreur qui affiche que tous c'est bien passé.
        elif 'no_err' in kwargs:
            err_type = kwargs['no_err']
            if err_type == 'no_err_create_folder':
                button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window_redirect)
            else : 
                button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            self.err_window.grid_rowconfigure((0,1), weight=1)
            label_no_err = customtkinter.CTkLabel(self.err_window, text="Aucune erreur détecté", text_color="#40f561")
            label_no_err.grid(row=0, column=0, pady=(20,5), padx=20)
            button_quit.grid(row=1, column=0, pady=5)
        #Créé la fenêtre qui affiche les erreurs si les dossiers non pas pus être crée
        elif 'simple_err' in kwargs:
            self.err_window.grid_rowconfigure((0,1), weight=1)
            label_no_err = customtkinter.CTkLabel(self.err_window, text="Un problème est survenue lors de la création des dossiers", text_color="red")
            button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            label_no_err.grid(row=0, column=0, pady=(20,5), padx=20)
            button_quit.grid(row=1, column=0, pady=5)
        #Créé la fenêtre qui affiches les erreurs liée a la création du fichier excel
        elif "err_save" in kwargs or "err_dates" in kwargs or  "err_passage" in kwargs :
            self.err_window.grid_rowconfigure((0,6), weight=1)
            if kwargs["err_save"] != "":
                label_err_sauvegarde = customtkinter.CTkLabel(self.err_window, text="Un problème est survenur lors la sauvegarde du fichier excel.", text_color="red")
                label_err_sauvegarde.grid(row=0, column=0, pady=(20,0), padx=20)
            if len(kwargs["err_dates"]) > 0 :
                label_err_dates = customtkinter.CTkLabel(self.err_window, text="Les dates de ces fichiers ne sont pas au bon format : ", text_color="red")
                for err in kwargs["err_dates"] :
                    str_err = f"{err} \n"
                label_str_err_dates = customtkinter.CTkLabel(self.err_window, text=str_err)
                label_err_dates.grid(row=2, column=0, pady=(20,0), padx=20)
                label_str_err_dates.grid(row=3, column=0, pady=(20,0), padx=20)
            if len(kwargs["err_passage"]) > 0 :
                label_err_passages = customtkinter.CTkLabel(self.err_window, text="Les passages de ces fichiers ne sont pas au bon format : ", text_color="red")
                for err in kwargs["err_passage"] :
                    str_err = f"{err} \n"
                label_str_err_passages = customtkinter.CTkLabel(self.err_window, text=str_err)
                label_err_passages.grid(row=4, column=0, pady=(20,0), padx=20)
                label_str_err_passages.grid(row=5, column=0, pady=(20,0), padx=20) 
            button_quit = customtkinter.CTkButton(self.err_window, text="OK", command=self.close_window)
            button_quit.grid(row=6, column=0, pady=5)
                           
        self.err_window.attributes('-topmost', True)
        self.err_window.lift()