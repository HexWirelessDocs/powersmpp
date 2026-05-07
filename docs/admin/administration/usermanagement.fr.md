---
tags:
  - Admin
  - User Management
---

## Administration

**Bienvenue sur iTextPRO**, votre passerelle vers une gestion efficace des documents!

Pour commencer avec l'accès au site d'administration iTextPRO, vous devrez vous connecter en utilisant le **URL Admin** et **identifiants de connexion** fourni par notre équipe de prestation de services.

Une fois que vous avez réussi à vous connecter, vous serez accueilli par un **interface conviviale** équipé de divers contrôles de navigation. Le principal contrôle de navigation pour démarrer votre expérience est **'Administration des utilisateurs — Gestion des utilisateurs'.** Gardez à l'esprit que les contrôles associés nichés sous ce menu ne seront visibles que lorsque vous **saisie d'un nom d'utilisateur spécifique** et frappe le **Afficher** bouton.

Pour des informations approfondies sur la fonctionnalité de la section Administration, vous trouverez **description détaillée** des divers contrôles dans les sections suivantes du présent document.

---

## Administration des utilisateurs

Naviguer jusqu'au **Gestion des utilisateurs** page est une brise. Cliquez simplement sur le **'Gestion de l'utilisateur'** option, et il vous guidera parfaitement vers la page de gestion de l'utilisateur.

Pour continuer, **saisir le nom d'utilisateur** vous êtes intéressé par dans la boîte de recherche dédiée et frapper le **Afficher** bouton. La boîte de recherche **peuple automatiquement les enregistrements correspondants** par ordre alphabétique, rendant votre recherche rapide et sans effort.

![User Management](images/Administration1.png)

---

## Ajouter un nouvel utilisateur

Plonger dans le processus d'expansion de votre base d'utilisateurs est simple. Cliquez simplement sur le **"Ajouter un nouvel utilisateur"** bouton pour lancer la création d'un nouveau compte utilisateur.

Cependant, pour assurer une configuration complète, vous devrez fournir les informations essentielles suivantes.

### **Étape 1: Entrez les détails de l'utilisateur**

En cliquant sur le **"Ajouter un nouvel utilisateur"** bouton, iTextPRO vous guidera vers une page dédiée. Remplissez ce qui suit :

- **Prénom**
- **Nom**
- **Adresse**
- **Nom d' utilisateur** - Ça doit être unique.
- **Mot de passe** – Minimum 8 caractères, avec au moins :
  - 1 lettre majuscule
  - 1 lettre minuscule
  - 1 caractère numérique
  - 1 caractère spécial
- **Adresse électronique** – Utilisé pour les alertes par e-mail incluant les OTP et les emails de bienvenue (basés sur les paramètres SMTP d'Admin).
- **Numéro mobile**
- **fuseau horaire** – affecte les horodatages de rapport et l'affichage spécifique à l'utilisateur.
- **Monnaie utilisateur** – Objectif d'affichage uniquement; sujet à la conversion en temps réel.
- **Validité du compte utilisateur**:
  - **Validité personnalisée** – Définir une date de fin.
  - **Validité à vie** – Pas d'expiration (accès permanent).
- **Type de compte utilisateur**:
  - **Utilisateur** – Accès au panneau utilisateur.
  - **Revendeur** – Compte en marque blanche avec options de marque et de prix.

![Add User Step 1](images/adduser1.png)

---

### **Étape 2: Détails de la notification (facultatif)**

Personnalisez vos notifications en ajoutant des courriels de plusieurs intervenants pour des alertes comme :

- Connexion OTP
- Nouvelle vérification de l'utilisateur
- Mises à jour du plan de taux
- Notifications d'agrément

![Add User Step 2](images/adduser2.png)

En cliquant sur **"Créer un nouvel utilisateur"**, une **email de bienvenue** est envoyé (exige une configuration SMTP). iTextPRO confirme le succès et présente:

- **Je le ferai une autre fois.** – Redirige vers le profil du nouvel utilisateur.
- **Ça va ! Laissez-les faire.** – Lance le **Assistant de configuration de compte**.

![Add User Step 3](images/adduser3.png)

---

### **Étape 3: Configuration des paramètres de la passerelle**

Choisissez votre méthode de routage :

- **Oui** – Utiliser un **passerelle fixe** pour tous les messages.
- **Non, j'ajouterai la règle de routage plus tard.** – Laissez les **Moteur principal d'acheminement** gérer dynamiquement le routage.

Vous pouvez également cliquer **"Passer"** poursuivre.

![Gateway Settings](images/adduser4.png)
![Routing Option](images/adduser5.png)

---

### **Étape 4: Ajout de crédits SMS**

- **Entrez les crédits** – Nombre de crédits SMS.
- **Enregistrer les modifications**
- **Passer à l'étape suivante**

!!! note
 Toutes les transactions de crédit sont **monnaie de base seulement**.

![Credits](images/adduser6.png)

---

### **Étape 5: Choix de la politique d'identification de l'expéditeur**

Sélectionnez :

- **ID de l'expéditeur dynamique** – Les utilisateurs peuvent utiliser n'importe quel ID d'expéditeur (numérique/alphanumérique).
- **ID de l'expéditeur fixe** – Utilisez un identifiant d'expéditeur prédéfini pour assurer la cohérence.

Cliquez sur **"Enregistrer"** Pour confirmer.

![Sender ID](images/adduser7.png)
![Sender ID Settings](images/adduser8.png)

---

### **Étape 6: Mise en place du SMPP Compte pour les clients de gros**

Pour créer un compte SMPP :

- Sélectionner **Oui**
- Configuration & #160;:
  - **ID système**
  - **Mot de passe**
  - **IP de la liste blanche** (pour la sécurité)

!!! tip "Meilleure pratique"
 Whitelist IPs pour éviter le spamming par SMS.

Utilisation **0,0,0,0** pour l'accès libre (authentification via ID système et mot de passe).

![SMPP Setup 1](images/adduser9.png)
![SMPP Setup 2](images/adduser10.png)

---

### **Étape 7 : Gestion du compte utilisateur**

Une fois la configuration terminée, vous verrez le message final avec 3 options:

#### **Option 1: Impersonnalité**
Connectez-vous en tant qu'utilisateur instantanément – pas besoin d'identifier séparément.

#### **Option 2 : Établissement de la facturation anticipée**
Gérer les plans tarifaires :

- **Ajouter un nouveau prix de vente**:
  - Pays
  - MCC/MNC
  - Prix de vente
  - Statut d'activation
- **Modèle de plan de taux d'importation**

!!! warning "Protection contre les pertes"
 Assurer **prix de vente ≥ coût de la passerelle** pour éviter les chutes de message (Politique de protection de perte).

#### **Option 3: Gérer cet utilisateur**
Accès **Profil** ou **Gestion des utilisateurs** page pour d'autres ajustements.

A **email de bienvenue** sera envoyé automatiquement.

![Impersonate](images/adduser11.png)
![Rate Plan Setup](images/adduser12.png)
![Manage User](images/adduser13.png)

---

Les **Vous êtes prêts !** Vous avez maintenant entièrement configuré un utilisateur dans **iTextPRO**, et sont prêts à gérer les utilisateurs, la facturation, les notifications et bien plus encore, tous d'un seul endroit.

# Gestion des utilisateurs

Les **Gestion des utilisateurs** section est organisée en plusieurs onglets pour améliorer la disposition du contrôle. Cette division des contrôles associés au compte utilisateur fournit **commodité dans la gestion efficace du compte utilisateur**.

Pour trouver un utilisateur spécifique, il suffit **saisir le nom d'utilisateur** dans la zone de recherche et cliquez sur **Affichage** bouton. La boîte de recherche est équipée d'un **fonctionnalité intelligente** qui peuple automatiquement la boîte avec **des enregistrements correspondants par ordre alphabétique**.

Pour une représentation visuelle, voir la figure ci-dessous:

![User Management](images/usermanagement1.png)

---

## Détails des onglets de gestion des utilisateurs

### Options de première rangée

#### **Personnalité**
- **Exposé succinct:** La sélection de cette option vous permet de **Connectez-vous ou incarnez un utilisateur** dans leur compte.
- **Authentification :** Saisissez la **mot de passe administrateur** pour vérification.
- **Remarque:** Le compte utilisateur s'ouvre dans un **nouvel onglet** dans la même fenêtre du navigateur, facilitant **gestion simultanée** des comptes utilisateur et administrateur.

#### **Gérer le plan de taux**
- **Fonctionnalité:** Cet hyperlien vous redirige vers le **Plan de taux d'utilisation** page.
- **Objet:** Configuration **prix de vente pour les pays et réseaux**.

#### **État**
- **Utilisation :** **Activer ou désactiver** un compte utilisateur/vendeur.
- **Résultat :** Utilisateurs désactivés **ne peut pas se connecter**.

#### **Supprimer cet utilisateur**
- **Mesures à prendre** Permanent **supprimer un compte utilisateur**.
- **Mise en garde:** Utilisateurs supprimés **ne peut être restauré**.

---

### Options de deuxième ligne

#### **Profil (Détails inclus)**

- Nom d' utilisateur 
- ID utilisateur 
- Numéro mobile 
- Adresse électronique *(utilisé pour la communication et les alertes)* 
- fuseau horaire 
- Priorité de l'utilisateur *(pour les messages de routage)* 
- Rôle du compte *(Vendeur ou utilisateur)* 
- Monnaie utilisateur *(affichage de la monnaie, sous réserve de conversion)* 
- Validité jusqu'à *(Douane ou durée de vie)* 
- Dernière connexion IP 
- Dernière connexion Date Heure 

**Fonctionnalité:** Accès et gestion **informations de base sur le profil utilisateur**.

#### **Réinitialiser le mot de passe**
- **Mesures à prendre** Réinitialiser le mot de passe pour **comptes utilisateurs ou revendeurs**.

!!! note
 Toutes les actions de la section Gestion des utilisateurs contribuent à **une gestion complète et rationalisée du compte utilisateur** expérience. Pour plus de détails, consultez le manuel d'utilisation iTextPRO.

---

## Privilèges supplémentaires et paramètres avancés

![Advanced Privileges](images/usermanagement2.png)

### **État de verrouillage de l' utilisateur**
- **Exposé succinct:** Permettre cette option **verrouille le compte utilisateur**, restreignant les activités de connexion.

### **Validation du pourriel utilisateur**
- **Exposé succinct:** Lorsque activé, iTextPro **valide les mots clés SPAM de l'utilisateur** pour chaque campagne. Les utilisateurs fiables peuvent **remplacement** Ceci en désactivant le basculement.

### **Validation globale du pourriel**
- **Exposé succinct:** Active l'application à **valider les mots-clés SPAM Global** pour les campagnes d'utilisation. Les utilisateurs fiables peuvent passer outre cette validation.

### **Validation IP de l'API**
- **Exposé succinct:** Activer cette option garantit iTextPRO **valide l'adresse IP de la liste blanche** avant de traiter les requêtes API.

### **Push Web HTTP SMS**
- **Exposé succinct:** Lorsqu'elle est activée, l'application **transmet des copies DLR** vers l'URL HTTP configurée dans l'option de gestion de webhooks du compte utilisateur.

### **WhatsApp HTTP Web Push**
- **Exposé succinct:** Activer ce bouton de bascule permet à admin d'activer **Option webhook WhatsApp** pour que l'utilisateur reçoive les DLR/Conversations WhatsApp vers les paramètres configurés.

![WhatsApp HTTP Web Push](images/usermanagement14.png)

### **Afficher le numéro mobile masqué**
- **Exposé succinct:** Le numéro masqué d'affichage permet à admin d'activer la fonctionnalité de **Numéro masquage**. Une fois que ce bouton de bascule a été défini comme actif, tous les numéros mobiles sur lesquels les campagnes ont été initiées à partir de l'application, **les quatre derniers chiffres** pour le numéro mobile sera masqué.

![Show Masked Mobile Number](images/usermanagement15.png)

!!! example
 Dans le rapport de campagne de l'utilisateur, les chiffres masqués apparaissent comme <span data-ph="0"></span>.

![Masked Number in Report](images/usermanagement16.png)

### **Seuil de survente de l'utilisateur**
- **Exposé succinct:** Active la configuration d'un **Limite du seuil de survente** sur les utilisateurs, leur permettant de consommer une quantité déterminée au-delà du solde alloué.

**Exemple :** 
Si le seuil est fixé à **500 euros**, l'utilisateur peut consommer jusqu'à **500 euros de plus** que le solde alloué.

---

## Paramètres avancés

![Advanced Settings](images/usermanagement3.png)

### **Ouvrir l'expéditeur**
- **Exposé succinct:** Permet aux utilisateurs finals de soumettre des messages **ID de l'expéditeur dynamique** (numérique ou alphanumérique).

### **Ouvrir le modèle**
- **Exposé succinct:** Permet aux utilisateurs d'utiliser **contenu dynamique** dans les messages en permettant des modèles ouverts.

### **Passer le profil OTP**
- **Exposé succinct:** Envoie un **OTP à l'identifiant de courriel enregistré de l'utilisateur** pour les activités de mise à jour du profil.

### **Est Skip Login OTP**
- **Exposé succinct:** Envoie un **OTP à l'identifiant de courriel enregistré de l'utilisateur** pour les activités de connexion.

### **Permettre la compensation DLR**
- **Exposé succinct:** Permet d'activer ou de désactiver **Indemnisation des DLR** pour les comptes de revendeur d'enfants.

### **Rémunération des DLR**
- **Exposé succinct:** Cette fonctionnalité permet à admin de générer des bénéfices supplémentaires en appliquant la compensation sur les messages et en générant le DLR de l'application **sans soumettre les messages à la passerelle**.

![DLR Compensation](images/dlrcompensation1.png)

**Configuration & #160;:**

- **DLR État :** Sélectionnez le statut du message qui doit être appliqué aux messages sur lesquels la compensation a été appliquée.
- **Pourcentage:** Ajouter le pourcentage auquel la compensation doit être appliquée.
- **Code d'erreur :** Configurez le code d'erreur en fonction de l'état, de sorte que la même chose sera mise à jour dans les rapports.
- **Limite du seuil de SMS :** Définit le seuil du numéro de destination pour l'application de la compensation DLR. Une fois le seuil atteint, la compensation sera appliquée selon la configuration.

!!! note
 Pour l'interface web, la limite de seuil fonctionnera sur la base de la campagne et dans le cas de SMPP/API, le seuil fonctionnera sur une base quotidienne.

![DLR Compensation Controller](images/dlrcompensation2.png)

??? example "Exemple de rémunération DLR"
 Un utilisateur a lancé une campagne sur 2000 numéros avec la configuration suivante:

    - **DLR Rémunération :** 20 %
    - **Limite de seuil :** 1 000

 Selon la configuration:

    - Sur 2000 messages, seulement **1600 messages** sera soumis au fournisseur de passerelle.
    - Pour **400 messages**, iTextPRO génère **DLR automatiques faux**, ce qui vous permet de maximiser votre rentabilité pour 400 messages.

 Si l'utilisateur envoie une campagne sur **1000> numéros mobiles** (sous le seuil), **L ' indemnisation du DLR n ' est pas appliquée**.

---

## Services actifs

Cette section se compose de **Plugins proposés par iTextPRO**. Ces plugins doivent être **choisi séparément** car ils ne font pas partie de l'application emballée.

![Active Services](images/activeservices1.png)

**Affichage des services actifs :** Affiche les plugins actuellement activés. En outre, l'administrateur peut activer ou désactiver les plugins à partir du bouton basculer.

### 1. **MO (Promoteur mobile)**
- **Fonction:** Active la **Service MO** pour les utilisateurs.
- Une fois que iTextPRO+ reçoit **Message entrant (MO)**, il apparaît dans le **rapport de boîte de réception de l'utilisateur**.
- Les messages peuvent être envoyés à **SMPP, HTTP push, email**, ou déclencheur **réponses automatiques**.

### 2. **SMS intelligent**
- **Fonction:** Active la **SMS intelligent** Caractéristique.
- Convertit de longues URLs en **raccourcir les liens intelligents**.
- Voies & #160;:
  - Utilisateur **numéro de téléphone mobile**,
  - **Adresse IP**,
  - **Détails du périphérique**,
  - **Géolocalisation**.

### 3. **Courriel au SMS**
- **Fonction:** Convertir **e-mails dans les SMS**, permettant la communication par e-mail passerelles.

### 4. **WhatsApp**
- **Fonction:** Il permet **Services WhatsApp** à l'utilisateur.
- Une fois le plugin activé, le module WhatsApp apparaîtra dans l'application.
- Les utilisateurs peuvent connecter leur compte d'affaires à l'application.
- Ajouter des modèles, configurer les webhooks pour DLR et Conversations.
- Obtenez des API pour envoyer des messages via des API.

---

## ID de l'expéditeur

Les **ID de l'expéditeur** onglet permet aux utilisateurs de configurer leurs identifiants d'expéditeur directement. Il affiche :

- **En attente**
- **Approuvé**
- **Rejeté** IDs de l'expéditeur

Accessible via le **"Voir l'identifiant de l'expéditeur"** lien.

![Sender ID](images/usermanagement6.png)

Aux **ajouter un ID d'expéditeur**:

- Cliquez sur **Ajouter un nouveau**
- Définir la **ID de l'expéditeur** et **Objet**
- Cliquez sur **Enregistrer**

L'identifiant de l'expéditeur (état: **approuvé**) sera ajouté au compte utilisateur.

![Add Sender ID](images/usermanagement7.png)

---

## Modèle

Les **Modèle** section permet aux utilisateurs de visualiser les modèles existants. Chaque modèle **État** (approuvé, en attente, rejeté) est clairement indiqué.

![Templates](images/usermanagement8.png)

---

## Détails du message

Les utilisateurs ont un aperçu **les trois derniers messages de campagne** et leurs **Statistiques sur le statut**, aider à évaluer **Résultats de la campagne**.

![Message Details](images/usermanagement9.png)

---

## Crédits

Les **Crédits** l'onglet affiche :

- **Solde disponible de l'utilisateur**
- **Historique des transactions**

Les utilisateurs peuvent gérer leur solde de compte via **"Ajouter plus de crédit"**:

![Credits](images/usermanagement10.png)

Pour ajouter des crédits :

- Sélectionner **type de service**
- Entrez **détails du paiement**
- Préciser **montant du crédit**

!!! note
 Les crédits doivent être ajoutés dans le **monnaie de base**.

![Add Credit](images/usermanagement11.png)

---

## Filtre

Les **Filtre** option permet aux utilisateurs de **liste blanche numéros mobiles**, assurant **L ' indemnisation du DLR n ' est pas appliquée** à ceux-là.

Ajouter des numéros mobiles avec **codes pays** facilement.

![Filter](images/usermanagement12.png)

---

## MT Routage

Les **MT Règles d'acheminement** est une caractéristique essentielle. Vous pouvez :

- Créer **Règles de routage** pour diriger le trafic SMS
- Appliquer à:
  - **Interface Web**
  - **API**
  - **Présentations de SMPP**

Les utilisateurs peuvent également configurer **règles de routage de passerelle fixe**, entrées auto-populantes dans le **Moteur principal d'acheminement**.

!!! tip
 La configuration d'une passerelle fixe est optionnelle mais améliore **efficacité du routage**.

![MT Routing](images/usermanagement13.png)

---

## Gérer le plan de taux

Les **Gérer le plan de taux** option permet à l'administrateur de configurer **Prix de vente** pour l'utilisateur.

**Prix de vente:** Le montant admin sera facturé à leur utilisateur par message sera le prix de vente.

Pour ajouter un prix de vente à l'utilisateur, suivez les étapes suivantes :

**Étape 1:** Aller à Administration >> Administration des utilisateurs >> Gestion des utilisateurs >> Utilisateur >> **Gérer le plan de taux**.

![Manage Rate Plan](images/rateplan1.png)

**Étape 2:** Choisissez la méthode appropriée pour ajouter le prix de vente.

### 1] Ajouter un nouveau prix de vente

Cela permet à l'administrateur d'entrer le prix de vente un par un au Pays et aux Réseaux pour l'utilisateur.

Sélectionnez le type d'interface & #160;: **TOUS** ou **SMPP**

![Add New Selling Price](images/rateplan2.png)

#### a) TOUTES les interfaces

Si l'interface a été choisie comme ALL, l'administrateur doit spécifier le Pays & Réseau puis le prix de vente. Une fois tous les détails ajoutés, cliquez sur **AJOUTER** pour enregistrer la configuration.

![ALL Interface](images/rateplan3.png)

#### b) Interface SMPP

Si l'interface a été choisie comme SMPP, l'administrateur doit spécifier **Nom du connecteur SMPP ou nom ESME**, de sorte que le plan tarifaire s'appliquera à ce compte particulier. Ensuite, spécifiez le Pays & Réseau et le prix de vente. Une fois tous les détails ajoutés, cliquez sur **AJOUTER** pour enregistrer la configuration.

![SMPP Interface](images/rateplan4.png)

!!! info "Interface ALL vs SMPP"
 **TOUS** indique les messages lancés depuis toutes les interfaces (Web, API et SMPP). **SMPP** indique un plan tarifaire seulement lorsque l'utilisateur envoie du trafic à l'aide de l'interface SMPP. Si aucun prix de vente spécifique à SMPP n'est configuré, les messages seront traités avec le prix configuré pour ALL.

![Rate Plan List](images/rateplan8.png)

### 2] Modèle de plan de taux d'importation

Cette option permet à l'administrateur d'importer tous les tarifs existants ou feuille de tarifs préparés sur le compte utilisateur en une seule fois. Il réduira les itérations à ajouter plusieurs prix de vente au compte utilisateur.

**Étape 1:** Sélectionnez le plan tarifaire
**Étape 2:** Admin peut également choisir l'interface (ALL ou SMPP)
**Étape 3:** Option d'écraser tout prix de vente existant.
**Étape 4:** Cliquez sur le bouton Importer pour ajouter le prix de vente au compte utilisateur.

![Import Rate Plan Template](images/rateplan6.png)

### Aviser l'utilisateur

Chaque fois que le prix de vente est mis à jour par l'administrateur, un e-mail sera envoyé à l'e-mail enregistré dans le compte utilisateur avec la ligne objet **"Avis de mise à jour de prix - Vos taux de messagerie ont été révisés"**.

Cet email contient les fichiers Excel pour tous les prix de vente configurés dans l'application.

Aussi, l'administrateur/le revendeur peut cliquer sur le **Aviser l'utilisateur** bouton pour déclencher le courriel à l'utilisateur au cas où ils n'ont reçu aucun courriel.

![Notify User](images/rateplan5.png)

---

## Création des utilisateurs - Mode de facturation

Pendant **création d'utilisateurs**, si les **Module de facturation** est activé dans l'application, l'administrateur doit configurer **Mode de facturation** pour l'utilisateur. Le mode de facturation sélectionné détermine comment l'utilisation des messages est facturée et comment les factures sont générées.

![Billing Mode](images/billingmode1.png)

Les modes de facturation suivants sont disponibles :

=== "Prépayé"

 Quand un utilisateur est configuré comme **Prépayé**:

    - L'administrateur doit: **générer une facture manuellement**.
    - Le montant de la facture doit être **crédité au compte de l'utilisateur**.
    - Ce n'est qu'une fois la facture réclamée et le solde disponible que l'utilisateur pourra envoyer des messages de l'application.
    - L'envoi de messages est limité en fonction du solde prépayé disponible.

=== "Postpaid"

 Quand un utilisateur est configuré comme **Postes payés**:

    - L'administrateur doit: **attribuer une limite de découvert** à l'utilisateur.
    - La demande **générer automatiquement des factures** basé sur la configuration **Cycle de facturation**.
    - L'utilisateur peut continuer à envoyer des messages jusqu'à ce que la limite de découvert attribuée soit atteinte.
    - La facturation est calculée en fonction de l'utilisation réelle au cours de la période de facturation.

!!! warning "Notes clés"
    - Les **Mode de facturation** ne s'applique que lorsque le module de facturation est actif.
    - La configuration de facturation a une incidence directe sur la livraison des messages de l'utilisateur et la production de factures.
    - Des limites de découvert et des cycles de facturation appropriés doivent être configurés pour les utilisateurs postpayés afin d'éviter toute perturbation du service.
