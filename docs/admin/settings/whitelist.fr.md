
# Numéros de liste blanche

Les **Numéros de liste blanche** fonctionnalité permet aux administrateurs de définir une liste de numéros de téléphonie mobile mondial. Lorsque **Indemnisation des DLR** est activé dans l'application, tout message envoyé à un numéro inclus dans la liste blanche sera toujours soumis au fournisseur et **ne sera pas considéré pour l'indemnisation DLR**, quel que soit le statut de livraison.

## Objet

Cette fonction est utile pour exclure de la logique de rémunération des numéros spécifiques (comme les numéros d'essai, les numéros de surveillance interne ou les contacts prioritaires) tout en assurant la livraison ininterrompue des messages.

![White List Numbers](images/whitelist1.png)

---

## Ajout de numéros à la liste blanche

1. Naviguez vers la **Numéros de liste blanche** section du panneau d'administration.
2. Cliquez sur **Ajouter un nouveau**.
3. Entrez les numéros mobiles dans le champ d'entrée.
4. Plusieurs nombres peuvent être ajoutés à la fois en les séparant par des virgules (<span data-ph="0"></span>).
5. Veiller à ce que **chaque numéro mobile comprend le code du pays** (par exemple, +91XXXXXXXXXX).
6. Enregistrer les modifications pour appliquer les entrées de la liste blanche dans le monde entier.

![Add Whitelist Numbers](images/whitelist2.png)

---

## Suppression des numéros de liste blanche

La demande supporte **suppression en vrac**, permettant aux administrateurs de supprimer plusieurs entrées de liste blanche en une seule action.

Les administrateurs peuvent également supprimer **entrées sélectionnées individuellement** selon les besoins.

![Bulk Delete Whitelist](images/whitelist4.png)

---

## Notes clés

!!! info "Important"
    - Les numéros figurant sur la liste blanche sont appliqués **dans l'ensemble de l'application**.
    - Les messages envoyés à ces numéros sont **Non compris dans les calculs de compensation DLR**.
    - Un formatage approprié avec les codes de pays est obligatoire pour une fonctionnalité correcte.
