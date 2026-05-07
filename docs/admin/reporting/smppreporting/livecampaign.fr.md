
# Rapport de campagne en direct

Les **Rapport de campagne en direct** module fournit aux administrateurs une visibilité en temps réel dans toutes les campagnes lancées sur la plateforme.

Alors que les utilisateurs finaux ne peuvent voir que leurs propres campagnes depuis le panneau utilisateur, cette section donne aux administrateurs une vue centralisée des campagnes créées par **tout compte utilisateur** dans le système.

Ce module est conçu pour aider les administrateurs :

- Surveiller les campagnes actives et achevées
- Situation du traitement de campagne en temps réel
- Filtrer les campagnes par l'utilisateur ou par la date
- Interviennent et arrêtent les campagnes si nécessaire
- Analyser la distribution de l'état de livraison

## Accès au rapport de campagne en direct

Pour accéder au rapport de campagne en direct :

1. Connectez-vous au panneau d'administration.
2. Naviguez vers **Rapports**.
3. Sélectionner **Rapport de campagne en direct**.

Dès l'ouverture, le système affichera une liste de campagnes lancées dans la plage de dates par défaut (habituellement aujourd'hui).

![Live Campaign Report Overview](images/livecampaign1.png)

---

## Options de filtrage

Le module offre des options de filtrage flexibles pour aider les administrateurs à localiser rapidement des campagnes spécifiques.

### A. Filtre par l'utilisateur

Les administrateurs peuvent :

- Sélectionnez un compte utilisateur spécifique dans le **Filtre utilisateur**
- Voir uniquement les campagnes initiées par cet utilisateur sélectionné

Ceci est utile lorsque:

- Enquêter sur une question de soutien
- Surveillance des expéditeurs à grand volume
- Audit des activités de campagne

### B. Sélection des dates

Les campagnes peuvent être filtrées en utilisant la **Gamme préférée** option:

- **Aujourd'hui** – Affiche les campagnes lancées à la date actuelle
- **Hier** – Affiche les campagnes lancées à la date précédente
- **Plage personnalisée** – Permet la sélection de dates de début et de fin spécifiques

Pour utiliser la gamme personnalisée :

1. Sélectionnez "Custom"
2. Choisissez la date de début souhaitée
3. Choisissez la date de fin
4. Appliquer le filtre

Le système récupérera toutes les campagnes lancées dans le délai choisi.

![User Filter and Date Range Selection](images/livecampaign2.png)

---

## Suivi de la campagne

Si une grande campagne est lancée sous n'importe quel compte utilisateur, l'administrateur peut surveiller son traitement en temps réel.

En cliquant sur le **Afficher l'état** bouton disponible dans l'interface:

- L'administrateur peut afficher les détails actuels du traitement des messages.

Cette caractéristique est particulièrement utile pour les campagnes à grand volume où une surveillance étroite est nécessaire.

![Campaign Status Dialog](images/livecampaign3.png)

---

## Arrêter une campagne

Si nécessaire, l'administrateur peut arrêter une campagne en cours.

Les **Arrête** bouton est disponible sous la **Décision** colonne dans l'interface.

!!! danger "Campagne d'arrêt"
    - Cliquez sur le **Arrête** bouton.
    - La campagne sera interrompue.
    - Les messages déjà traités peuvent ne pas être affectés, selon leur stade.

---

## Bouton Action – Compte de l'état d'avancement

Les **Décision** bouton permet également au vendeur ou à l'administrateur de vérifier le nombre détaillé par statut pour chaque campagne.

En utilisant cette option, l'administrateur peut :

- Visualisez le nombre de messages sous chaque état de livraison.
- Analyser les performances de la campagne.
- Identifiez toute défaillance anormale ou les motifs en attente.

En cliquant dessus, les administrateurs peuvent afficher un décompte complet des messages, y compris :

- **Soumis** Nombre
- **Livraison** Nombre
- **Non livrée** Nombre
- **Rejeté** Nombre
- **Expiré** Nombre (le cas échéant)
- **Inconnu** Nombre
- **Autres** Nombre

![Status-Wise Message Count](images/livecampaign4.png)

---

Les **Rapport de campagne en direct** fournit aux administrateurs une surveillance complète de toutes les activités de campagne, permettant une surveillance en temps réel, un filtrage spécifique à l'utilisateur et des capacités d'intervention pour une gestion efficace de la plateforme.
