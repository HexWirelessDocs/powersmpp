---
tags:
  - Billing
  - WhatsApp
  - Rate Plan
---

# Configuration du plan de taux WhatsApp

**Navigation:** <span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span> - Oui. <span data-ph="3"></span>.

## Aperçu général

Les **Configuration du plan de taux WhatsApp** module permet aux administrateurs de définir **modèles de prix** pour la messagerie WhatsApp. Ces plans de tarification régissent la facturation et le suivi des messages au sein de la plate-forme PowerSMPP et sont affectés aux comptes d'utilisateurs pour une gestion précise des coûts et des revenus.

---

## Créer un nouveau plan de taux WhatsApp

Le processus de création du plan tarifaire est structuré en **trois étapes**.

![Manage WA Rate Plans — List of configured plans](images/warateplan-01-list.png)

### Étape 1: Détails de base

| Champ | Désignation des marchandises |
|-------|-------------|
| **Nom du régime** | Attribuer un nom descriptif unique pour le plan. |
| **Est actif** | Mettre le plan en place <span data-ph="0"></span> ou <span data-ph="1"></span> État. |

![Add New WA Rate Plan — Step 1: Basic Details](images/warateplan-02-step1-basic.png)

### Étape 2: Détails des prix (par pays)

Définir la structure des prix pour chaque pays de destination.

![Add New WA Rate Plan — Step 2: Price Details](images/warateplan-03-step2-price.png)

| Champ | Désignation des marchandises |
|-------|-------------|
| **Code pays** | Sélectionnez le pays de destination (par exemple, <span data-ph="0"></span>). Le plan tarifaire appuie la tarification multi-pays. |
| **Prix** | Le coût d'achat / de gros par message WhatsApp pour le pays sélectionné. |
| **Prix de vente** | Le prix de détail facturé à l'utilisateur final ou au client pour chaque message WhatsApp. |
| **Charge plate-forme** | Frais supplémentaires de plate-forme appliqués en plus du prix de vente (le cas échéant). |

### Étape 3: Assigner aux utilisateurs

Une fois le plan tarifaire sauvegardé, il devient disponible pour être affecté à des comptes d'utilisateur individuels. L'attribution du plan garantit que tous les messages WhatsApp envoyés par l'utilisateur sont facturés selon la structure de tarification configurée.

---

## Gestion des régimes tarifaires existants

Les **Gérer le plan de taux d'AE** liste de tous les plans de tarifs WhatsApp configurés avec les informations suivantes:

| Colonne | Désignation des marchandises |
|--------|-------------|
| **Nom du plan** | L'identificateur du plan tarifaire. |
| **Taux** | Nombre d'entrées par pays configurées. |
| **Utilisateur assigné** | Nombre d'utilisateurs actuellement affectés au plan. |
| **Créer une date** | Date de création du plan. |
| **Est actif** | Situation actuelle (<span data-ph="0"></span> / <span data-ph="1"></span>). |
| **Est par défaut** | Indique si le plan est le système par défaut. |
| **Décision** | <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>ou <span data-ph="3"></span> le plan. |

---

## Objet de la configuration du plan de taux WhatsApp

!!! info "Utilisez ce module pour..."
    - Définir le prix des messages WhatsApp par pays.
    - Soutenir les plans de tarifs multipays dans un modèle unique.
    - Attribuer des plans tarifaires à des comptes d'utilisateur précis pour la facturation.
    - Suivre les coûts et les revenus des messages WhatsApp par utilisateur.
    - Permettre des rapports financiers précis pour le trafic de WhatsApp.
    - Gérer les frais de plateforme en plus des coûts et des prix de vente.

!!! tip
 Le clonage est le moyen le plus rapide de faire tourner une variante régionale d'un plan existant — cloner le parent, ajuster un ou deux prix par pays, et attribuer au nouveau groupe d'utilisateurs.
