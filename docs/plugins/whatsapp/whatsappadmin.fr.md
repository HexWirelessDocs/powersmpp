---
tags:
  - WhatsApp
  - Plugin
  - Configuration
---

# Administration - Module WhatsApp

## 1. Description du service actif
**WhatsApp :** 
En permettant ce plugin, l'utilisateur pourra :
- Accédez et envoyez des messages via WhatsApp.
- Configurez des chatbots pour des réponses automatisées pour leurs entreprises.

---

## 2. Crédits ouverts
- Les utilisateurs ont une **solde portefeuille séparé pour WhatsApp**.
- L'administrateur peut voir le solde créditeur pour **Messagerie SMS** et **WhatsApp** séparément.

**Étapes pour ajouter des crédits :**
1. Cliquez sur **Ajouter un nouveau** ajouter des crédits au solde de l'utilisateur.
2. Sélectionner **WhatsApp** de la liste des services.
3. Entrez un **référence de paiement**.
4. Saisissez la **Montant**.
5. Cliquez sur **Ajouter des crédits** pour compléter le solde de l'utilisateur.

![WhatsApp Admin Credits](images/whatsappadmin1.png)

---

## 3. Plan de taux d'utilisation
Dans la section WhatsApp, vous pouvez **plan de taux** à appliquer à l'utilisateur.

- Sélectionnez le plan tarifaire dans le menu déroulant.
- Tous les plans de tarifs configurés dans le **Facturation** section apparaîtra ici pour la sélection.

---

### Plans de taux WhatsApp
Comme les plans de taux de messages MT, l'administrateur doit définir **Plans tarifaires spécifiques à WhatsApp** pour gérer la facturation.

**Actions disponibles:**
1. **Modifier** – Changer le nom du plan tarifaire ou activer/désactiver le plan.
2. **Affichage** – Afficher et modifier tous les prix configurés dans le plan tarifaire. Les mises à jour s'appliqueront à tous les utilisateurs assignés.
3. **Copier** – Dupliquer un plan tarifaire existant avec un nouveau nom.
4. **Supprimer** – Enlever un plan de tarifs en permanence. *(Ne peut être défait)*

![WhatsApp Admin Rate Plans](images/whatsappadmin2.png)

---

## Créer un nouveau plan tarifaire

**Étape 1:** 
- Saisissez la **Nom du régime tarifaire amiable**.
- Choisir **Actifs/inactifs** État.
- Cliquez sur **Continuer**.

![WhatsApp Admin Step 1](images/whatsappadmin3.png)

---

**Étape 2:** 
- Définir les prix du plan tarifaire.
- Configurez les détails de facturation pour l'utilisateur.

![WhatsApp Admin Step 2](images/whatsappadmin4.png)

**Champs:**
- **Code pays** – Sélectionnez le pays applicable.
- **Prix** – Le montant facturé par META par message.
- **Prix de vente** – Le prix facturé à l'utilisateur par message.
- **Charge plate-forme** – Frais optionnels pour l'utilisation de votre plateforme.

---

### Cas d'utilisation

**Décision 1:** 
- Facturation avec META gérée par admin. 
- Pas de frais de plateforme. 
- **Crédits déduits** selon *Prix de vente*.

**Décision 2:** 
- Facturation avec META gérée par l'utilisateur. 
- Seuls les frais de plateforme sont facturés. 
- **Prix de vente** conservé comme <span data-ph="0"></span>.

**Décision 3:** 
- L'administrateur facture à la fois le prix de vente et les frais de plate-forme. 
- Crédits déduits **Prix de vente + frais de plateforme**.

---

**Étape 3:** 
- Revoir **résumé du plan tarifaire**.
- Assurez-vous que tous les détails sont exacts.
- Cliquez sur **Enregistrer** pour finaliser.

---
