bibliotheque = []

def ajouter_livre(titre):
    livre = {'titre': titre}
    bibliotheque.append(livre)
    print(f"Le livre '{titre}' a été ajouté à la bibliothèque !")

def supprimer_livre(titre):
    for livre in bibliotheque:
        if livre['titre'] == titre:
            bibliotheque.remove(livre)
            print(f"Le livre '{titre}' a été supprimé de la bibliothèque.")
            return
    print(f"Aucun livre avec le titre '{titre}' n'a été trouvé dans la bibliothèque.")

def rechercher_livre(titre):
    for livre in bibliotheque:
        if livre['titre'] == titre:
            print(f"Le livre '{titre}' est dans la bibliothèque.")
            return
    print(f"Aucun livre avec le titre '{titre}' n'a été trouvé dans la bibliothèque.")

def afficher_livres():
    if not bibliotheque:
        print("La bibliothèque est vide.")
    else:
        print("Les livres dans la bibliothèque sont:")
        for livre in bibliotheque:
            print(f"'{livre['titre']}'.")

def trier_livres():
    bibliotheque.sort(key=lambda livre: livre['titre'])
    print("Les livres ont été triés par titre.")

while True:
    print("Que voulez-vous faire ?")
    print("1. Ajouter un livre à la bibliothèque.")
    print("2. Supprimer un livre de la bibliothèque.")
    print("3. Rechercher un livre par titre.")
    print("4. Afficher tous les livres.")
    print("5. Trier les livres par titre.")
    print("6. Fermer le programme.")
    
    choix = input("Votre choix : ")
    print()

    if choix == "1":
        titre_livre = input("Entrez le titre du livre : ")
        ajouter_livre(titre_livre)

    elif choix == "2":
        titre_livre = input("Entrez le titre du livre à supprimer : ")
        supprimer_livre(titre_livre)

    elif choix == "3":
        titre_livre = input("Entrez le titre du livre à rechercher : ")
        rechercher_livre(titre_livre)

    elif choix == "4":
        afficher_livres()

    elif choix == "5":
        trier_livres()
    
    elif choix == "6":
        print("Fermeture du programme.")
        break

    else:
        print("Choix invalide. Veuillez choisir une option valide.")

    print()