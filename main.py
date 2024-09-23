import view.window_create_folders as window_create_folders

#Début de la boucle principale
if __name__ == "__main__":
    app = window_create_folders.main_window()
    app.mainloop()
    
#Fonction qui créer la fenetre pour créer les dossiers (appel le fichier "view/window_create_folders.py")
def main_win():
    app = window_create_folders.main_window()
    app.mainloop()