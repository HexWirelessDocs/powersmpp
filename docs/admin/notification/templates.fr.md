
# Modèles de courriel

## Caractéristiques principales

### Surveillance automatisée
- **iTextPro** surveille en permanence les paramètres critiques de l'application à intervalles réguliers.
- Identification proactive des problèmes potentiels avant qu'ils ne s'aggravent.

### Alertes par courriel
- Les intervenants reçoivent des alertes par courriel.
- Les notifications sont envoyées à l'avance, ce qui permet aux parties prenantes de prendre des mesures préventives.

### Gestion des modèles personnalisés
- Prend en charge les modèles d'alerte personnalisables.
- Les utilisateurs peuvent gérer et adapter les modèles de notification en fonction de leurs besoins.

### Intégration des variables système
- Les modèles personnalisés peuvent inclure des variables système pertinentes.
- Communication personnalisée grâce à une mise à jour dynamique des informations du système.

---

## Lignes directrices pour l'utilisation

### Gestion des modèles
- Personnalisez les modèles d'alerte pour répondre à des besoins de communication spécifiques.
- Intégrer des variables de système pertinentes pour les notifications dynamiques et contextuelles.

### Engagement des parties prenantes
- Veiller à ce que les intervenants concernés soient configurés pour recevoir des notifications.
- Vérifiez que les paramètres d'email sont correctement configurés pour une communication transparente.

---

## Avantages
- Améliore la fiabilité et la stabilité du **iTextPro** demande.
- Fournit un mécanisme proactif de détection et d'alerte des problèmes.
- Des modèles personnalisables et des variables système permettent une communication personnalisée et informative.
- Aide les organisations à rester en avance sur les défis potentiels.

!!! note
 Les détails SMTP sont obligatoires pour Admin ainsi que pour les comptes revendeurs pour déclencher des courriels.

---

## Gestion des modèles de courriel

![Email Templates](images/template1.png)

---

## Événements de notification et modèles correspondants

### Défaut de déclaration globale
Déclenchement lorsque le service de déclaration globale rencontre une défaillance inconnue. 
![Aggregate Reporting Failure](images/template2.png)

### Notification d'agrément
Envoyé à l'approbation de l'administrateur des demandes d'identification de l'expéditeur et du modèle. 
![Approval Notification 1](images/template3.png) 
![Approval Notification 2](images/template4.png)

### Demande d'approbation Notification
Déclenchement lorsqu'un revendeur/utilisateur lance une demande d'identification de l'expéditeur ou d'approbation de modèle. 
![Approval Request Notification 1](images/template5.png) 
![Approval Request Notification 2](images/template6.png)

### Modifier le mot de passe
Envoyé lorsqu'un utilisateur modifie avec succès son mot de passe. 
![Change Password](images/template7.png)

### Notification de crédit
Alerte lorsque le solde disponible d'un utilisateur est inférieur au seuil de crédit. 
![Credit Notification](images/template8.png)

### Transfert de crédits
Démarré par l'ajout d'un solde à un compte utilisateur par l'utilisateur ou les revendeurs. 
![Credit Transfer](images/template9.png)

### Courriel
Envoyé à la réception d'un message entrant (MO) lorsque la transmission des courriels MO est active. 
![Email Post](images/template10.png)

### Liste noire Esme
Alerte lorsqu'un compte ESME est sur la liste noire en raison du spamming. 
![Esme Blacklist](images/template11.png)

### Portail d'échec
Déclenchement lorsque le changement de message automatique survient en raison d'une panne de passerelle primaire. 
![Failover Gateway](images/template12.png)

### Mot de passe oublié
Envoyé quand il y a une demande pour changer le mot de passe du compte de connexion. 
![Forgot Password](images/template13.png)

### Portail Liste noire
Alerté lorsqu'une passerelle/route du fournisseur SMPP est sur la liste noire après des tentatives de liaison ratées. 
![Gateway Blacklisted](images/template14.png)

### Expiration du prix de la passerelle
Déclenchement lorsqu'une route avec un taux expiré est détectée. 
![Gateway Price Expiry](images/template15.png)

### Avis de refus d'emploi
Envoyé lorsqu'une demande d'ID ou de modèle d'expéditeur est désapprouvée par l'administrateur/vendeur. 
![Job Disapproved Notification 1](images/template16.png) 
![Job Disapproved Notification 2](images/template17.png)

### Demande de message
Déclenchement lorsque la file d'attente du fournisseur viole la limite de seuil. 
![Message Queue](images/template18.png)

### Nouveau compte par administrateur
Envoyé lorsqu'un nouvel utilisateur est ajouté de l'administration ou s'inscrit. 
![New Account by Admin](images/template19.png)

### Nouveau compte par revendeur
Envoyé aux utilisateurs revendeurs lorsqu'un revendeur ajoute un nouvel utilisateur ou qu'un nouvel utilisateur signe. 
![New Account by Reseller](images/template20.png)

### Nouvel utilisateur Vérification par courriel
Déclenchement pour les nouveaux utilisateurs s'inscrivant à la vérification par courriel. 
![New User Email Verification](images/template21.png)

### OTP
Envoyé pour vérification OTP pendant les connexions utilisateur. 
![OTP](images/template22.png)

### État des services
Alerte lorsqu'un démon/service est automatiquement récupéré.

### Service arrêté
Déclenchement lorsqu'un démon/service est intentionnellement arrêté. 
![Service Stopped](images/template23.png)

### Détection du pourriel
Alerte lorsque le contenu en SPAM est détecté. 
![Spam Detection](images/template24.png)

### Mise à jour de vente de l'utilisateur
Envoyé lorsque le prix de vente du client est mis à jour par le compte parent. 
![User Selling Update](images/template25.png)

---

Ces notifications couvrent un large éventail d'événements, fournissant des informations complètes et des alertes en temps opportun pour assurer un suivi et une gestion efficaces de la **iTextPro** plate-forme.
