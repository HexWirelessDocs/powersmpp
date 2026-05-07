
# Nombres de listes noires

Les **Nombres de listes noires** fonctionnalité permet aux administrateurs de définir une liste de numéros mobiles qui sont bloqués dans l'application. Une fois qu'un nombre est ajouté à la liste noire, **tous les messages sortants vers ce numéro sont automatiquement rejetés par la demande**, et aucun utilisateur ne pourra lui envoyer des messages.

## Objet

Cette fonctionnalité est utilisée pour empêcher la livraison de messages à des numéros restreints, invalides, non conformes ou interdits afin de maintenir la conformité réglementaire et de contrôler l'utilisation abusive.

![Blacklist Numbers](images/blacklist2.png)

---

## Ajout de numéros à la liste noire

1. Naviguez vers la **Nombres de listes noires** section dans le panneau administratif.
2. Cliquez sur **Ajouter un nouveau**.
3. Entrez les numéros mobiles dans le champ d'entrée.
    - Plusieurs nombres peuvent être ajoutés à la fois en les séparant par des virgules (<span data-ph="0"></span>).
4. Veiller à ce que **chaque numéro mobile comprend le code du pays** (par exemple, +91XXXXXXXXXX).
5. Enregistrer les modifications pour appliquer les entrées de liste noire dans l'application.

![Add Blacklist Numbers](images/blacklist3.png)

---

## Suppression des numéros figurant sur la liste noire

La demande supporte **suppression en vrac**, permettant aux administrateurs de supprimer plusieurs entrées de liste noire en une seule opération.

Les administrateurs peuvent également **supprimer les entrées sélectionnées individuellement** selon les besoins.

![Bulk Delete Blacklist](images/blacklist4.png)

---

## Comportement de traitement des messages

!!! warning "Messages bloqués"
    - Tout message envoyé à un numéro de liste noire sera **bloqué au niveau de l'application**.
    - La demande de message sera **immédiatement rejeté**, et il ne sera pas transmis au vendeur.

!!! tip
 S'assurer que chaque numéro de téléphone mobile comprend les **code pays** (par exemple, +91XXXXXXXXXX) pour une fonctionnalité correcte.
