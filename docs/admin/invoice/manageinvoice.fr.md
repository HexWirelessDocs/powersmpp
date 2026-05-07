
# Facturation

Le module Facturation permet aux administrateurs de gérer la facturation pour leurs utilisateurs directs (Type de compte : **Utilisateur**) en fournissant un plugin pour générer des factures, les télécharger ou les envoyer par e-mail. Le flux de génération de facture est automatisé et déclenché à des intervalles spécifiques configurés par l'Admin.

Ce module aide les administrateurs à gérer efficacement les opérations de facturation de leurs enfants utilisateurs.

---

## Facture [Prépayée / Postpayée] comme Plugin

L'administrateur doit choisir **Licence de facturation** séparément. Une fois activé, le module de facturation devient accessible dans l'application avec le mode de facturation sélectionné—**Prépayé** ou **Postes payés**.

- Les **Méthode de facturation** (Prépayé/Postpayé) pour chaque utilisateur est défini lors de la création de l'utilisateur.
- Admin peut configurer la méthode de facturation pour chaque utilisateur.
- Les utilisateurs qui s'inscrivent par eux-mêmes auront **Prépayé** facturation par défaut.

---

## Tableau de bord de facturation

Lorsque l'Admin accède au module de facturation, la première vue présentée est la **Tableau de bord de facturation**. Le tableau de bord fournit des renseignements clés sur la facturation :

### 1. Facture totale
Affiche la **Nombre total de factures**, y compris:
- Factures approuvées 
- Factures non approuvées 

### 2. Factures payées
Affiche le nombre de **factures entièrement payées**.

### 3. Factures non réglées
Indique le nombre de factures en attente, avec:
- Factures impayées 
- Factures partiellement payées 

### 4. Gérer la facture
Résumé succinct *Gérer la facture* Chapitre. 
Les administrateurs peuvent cliquer **Aller à la page** pour naviguer vers la gestion détaillée des factures.

### 5. Gérer les factures récurrentes
Applicable **uniquement pour les utilisateurs Postpayés**. 
D'ici, les administrateurs peuvent :
- Créer des factures récurrentes 
- Démarrer ou arrêter le cycle de facturation 
- Modifier les paramètres du cycle de facturation 

### 6. Gérer les paiements reçus
Résumé succinct *Gérer les paiements reçus* Chapitre. 
Admins peut rediriger vers la page détaillée en utilisant le **Aller à la page** bouton.

---

## Gérer les factures

Les **Gérer les factures** page affiche toutes les factures (y compris les factures récurrentes) ainsi que leur statut de paiement. Les administrateurs peuvent demander des factures, les télécharger et envoyer des courriels de rappel de paiement.

![Manage Invoices](images/manage1.png)

### Principales caractéristiques :

#### **Télécharger le rapport de facture**
Permet aux administrateurs d'exporter et de télécharger le rapport de facture sous forme de feuille Excel.

#### **Envoyer un rappel en vrac**
Permet d'envoyer des rappels de paiement aux utilisateurs dont les factures sont **Non payé** ou **Partiellement payé**.

#### **Projets**
Les factures récurrentes générées automatiquement pour les utilisateurs Postpayés sont stockées comme **projets**. 
Les administrateurs doivent examiner et approuver les ébauches manuellement à partir du menu Action.

#### **Recherche préalable**
L'option de recherche avancée permet de filtrer les factures par :
- Utilisateur 
- Numéro de facture 
- État dû 
- État du paiement 

Cela aide Admins à localiser les factures rapidement en fonction des besoins spécifiques.

---

## Créer une facture

Cette section permet à Admins de créer manuellement des factures pour les utilisateurs.

---

### **Pour les utilisateurs prépayés :**

1. Sélectionnez le type d'utilisateur & #160;: **Prépayé**
2. Choisissez l'utilisateur.
3. Saisissez la **Date de facturation** et **Date d'échéance**.
4. Saisissez la **Montant de la redevance** (avant impôts).
5. Fournir **description** pour la facture.
6. Modifier **Conditions générales** ou **Notes du client** si nécessaire (ou utiliser des valeurs configurées par défaut).
7. Choisissez l'une des options suivantes :
   - **Créer une facture** (si le paiement n'est pas encore reçu)
   - **Créer une facture de & revendication** (si le paiement a déjà été reçu — le système invite à entrer les détails du paiement)

---

### **Pour les utilisateurs postpayés :**

Les factures postpayées sont généralement générées automatiquement à la fin du cycle de facturation défini sous **Factures récurrentes**. 
Cependant, si un cycle a été ignoré ou nécessite une intervention manuelle, Admins peut créer la facture manuellement:

1. Sélectionnez le type d'utilisateur & #160;: **Postes payés**
2. Choisissez l'utilisateur.
3. Sélectionnez la **date** pour laquelle la facture doit être créée et récupérer les dossiers.
4. Le système affichera les enregistrements de messagerie pour la période sélectionnée.
5. Après vérification, choisissez :
   - **Créer une facture**
   - **Créer et réclamer une facture**

