
## Règle ESME sur la liste noire

Les **Règle ESME sur la liste noire** dans iTextPRO sert de protection proactive pour protéger votre serveur SMPP des clients ESME voyous ou mal configurés. Ces clients peuvent causer une dégradation des performances en raison de demandes de commandes répétées ou anormales. En créant cette règle, les administrateurs peuvent **liste noire automatique** des clients suspects et de prévenir d'autres dommages.

---

### Objet

Dans les scénarios où un utilisateur d'ESME voyous présente une menace – soit par une implémentation défectueuse, soit par des requêtes à haute fréquence involontaires – cette règle permet à iTextPRO de déposer définitivement les requêtes de cet utilisateur, en maintenant **stabilité et intégrité du serveur**.

---

### Options de configuration

![Blacklist Rule Setup](images/blacklist1.png) 
![Blacklist Rule Fields](images/blacklist2.png)

Pour configurer une nouvelle règle ESME Blacklist :

1. **Nom de la règle**: 
   - Entrez un nom descriptif et amical pour la règle de la liste noire (p. ex. <span data-ph="0"></span>).

2. **Utilisateur**: 
   - Sélectionnez le compte utilisateur ESME que la règle doit surveiller.

3. **Numéro de système ESME**: 
   - Choisissez le particulier **ID système** de l'utilisateur ESME.

4. **Type de commande**: 
   - Choisissez le type de commande à surveiller :
     - **Demande de lien**
     - **Reliure**

5. **Intervalle**: 
   - Définissez l'intervalle dans :
     - Heures
     - Procès-verbal
     - Deuxièmes

6. **Fréquence**: 
   - Définissez combien de fois le type de commande sélectionné peut se produire dans l'intervalle de temps spécifié.

7. Après avoir rempli les détails, cliquez sur **"Enregistrer"** pour activer la règle.

---

### Exemple Cas d'utilisation

Supposons que vous vouliez bloquer un utilisateur ESME qui envoie **Requêtes de bind ou de Enquire Link** supérieur à **10 fois dans 1 minute**. 
- Jeu <span data-ph="0"></span> 
- Jeu <span data-ph="0"></span> 
- Si la condition est remplie, iTextPRO:
  - **Blacklist le compte ESME**
  - **Envoyer une alerte à l'adresse email de l'administrateur**

Cela empêche les clients abusifs ou mal configurés de surcharger le serveur SMPP.

---

### Résultat & Alertes

Une fois la règle violée :
- L'ESME est automatiquement **Liste noire**.
- Une **Alerte par courriel** est envoyé à l'administrateur.

![Blacklist Result](images/blacklist3.png)

---

### Résumé

Les **Règle ESME sur la liste noire** est une caractéristique essentielle pour:
- Détecter le comportement anormal ou abusif du client.
- Protégez votre infrastructure de la dégradation des performances.
- Automatiser l'atténuation en appliquant la liste noire en temps réel.

Utilisez cette fonctionnalité pour maintenir robuste **Performance du serveur SMPP** et de faire respecter l'hygiène opérationnelle dans toutes les connexions ESME.
