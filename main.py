
import tkinter as tk
from tkinter import messagebox

def main():
    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Message")
    root.geometry("400x200")
    
    # Ajouter un label avec le message
    label = tk.Label(
        root, 
        text="Voici votre message!", 
        font=("Arial", 16),
        pady=20
    )
    label.pack()
    
    # Ajouter un bouton qui affiche 100 messages avec un décalage
    def show_message():
        # Position initiale
        x, y = root.winfo_x() + 50, root.winfo_y() + 50
        
        for i in range(2):
            # Créer une fenêtre pour chaque message
            msg_window = tk.Toplevel(root)
            msg_window.title(f"Message {i+1}/100")
            msg_window.geometry(f"500x300+{x}+{y}")
            
            # Jouer un son (bip système)
            root.bell()
            
            # Ajouter le contenu
            label = tk.Label(
                msg_window,
                text=f"Message {i+1}/100 dans une boîte de dialogue!",
                font=("Arial", 12),
                pady=20
            )
            label.pack(expand=True)
            
            # Bouton pour fermer
            close_button = tk.Button(
                msg_window,
                text="Fermer",
                command=msg_window.destroy
            )
            close_button.pack(pady=10)
            
            # Mettre à jour les coordonnées pour la prochaine fenêtre 
            # Décalage de gauche à droite puis de haut en bas
            x += 30
            # Si on atteint le bord droit de l'écran, on revient à gauche et on descend
            if x > root.winfo_screenwidth() - 300:
                x = root.winfo_x()
                y += 30
            
            # Afficher la fenêtre et attendre un peu avant de passer à la suivante
            msg_window.update()
            root.after(100)  # Pause de 100ms entre chaque fenêtre
    
    button = tk.Button(
        root, 
        text="Cliquez ici", 
        command=show_message,
        font=("Arial", 12),
        padx=10,
        pady=5
    )
    button.pack(pady=20)
    
    # Lancer la boucle principale
    root.mainloop()

if __name__ == "__main__":
    main()
