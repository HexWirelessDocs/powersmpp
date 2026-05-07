
## Codes d'erreur de la passerelle

![Gateway Error Codes](images/error1.png)

**Codes d'erreur de la passerelle** dans iTextPRO vous permettent d'interpréter et de gérer les messages de réponse de **Centre de service des messages courts (SMSC)** lorsque la livraison du message échoue. Cette fonctionnalité améliore la visibilité par rapport aux échecs de livraison et permet des retours de crédit basés sur des codes d'erreur spécifiques.

---

![Configure Error Codes](images/error2.png)

### 1. Aperçu général
Lorsque le SMSC ne peut pas transmettre un message, il retourne un **code d'erreur non zéro** avec un statut de message de référence. Ils sont appelés **Codes d'erreur de la passerelle**.

### 2. Objet
iTextPRO permet aux administrateurs de configurer et de mapper ces codes d'erreur. Lorsque **Rapport d'exécution (DLR)** iTextPRO vérifie la configuration et:
- Affiche un **marque d'erreur personnalisée**
- La carte à une **statut SMPP standard** 
Cette information est présentée dans les deux **Administrateur** et **Rapports des utilisateurs**, améliorer la transparence.

### 3. Préalables
Avant la configuration, obtenir un **Liste des codes d'erreur de la passerelle** de votre SMSC.

---

### 4. Étapes de configuration

#### a. Sélection de la passerelle
Choisissez la passerelle pour laquelle vous configurez le code d'erreur.

#### b. Code d'erreur
Saisissez la **code d'erreur spécifique** reçu de votre SMSC.

#### c. Affichage de l'étiquette d'erreur
Insérer la **statut de référence** ou le nom d'étiquette du SMSC (p. ex., <span data-ph="0"></span>, <span data-ph="1"></span>).

#### d. Code d'erreur standard (matériel)
Carter l'erreur sur l'un des statuts standard SMPP:
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>

#### e. Description de l'erreur
Fournir **brève description** de l'étiquette d'erreur. Ceci sera montré dans le **Rapports des utilisateurs** aider à comprendre l'état de livraison.

#### f. est actif
Basculer le code d'erreur **en cours ou en cours** selon les besoins.

#### g. Retour en arrière du crédit
Activer cette option **retour des crédits d'utilisateur** automatiquement si un message échoue avec le code d'erreur cartographié.

---

### 5. Chargement en vrac

- Utilisez la **Envoi en vrac** fonction pour configurer plusieurs codes d'erreur simultanément.
- Cliquez sur **"Téléchargement de buses"**, puis:
  - **Télécharger le fichier exemple**
  - **En-têtes de colonnes de cartes** dans l'assistant d'importation

---

### 6. Soumettre
Une fois configuré, cliquez sur **"Soumettre"** pour enregistrer les codes d'erreur pour la passerelle sélectionnée.

Les **Remarque:** 
La bonne configuration du code d'erreur améliore la surveillance et permet un suivi précis des **défaut de livraison du message**, **Actions de renversement**et **exactitude des rapports**.

---
