---
tags:
  - Billing
  - Rate Plan
  - Pricing
---

# Facturation

## Gestion simplifiée de la facturation avec iTextPRO

Les agrégateurs de l'industrie des SMS sont souvent confrontés à des défis dans la gestion **passerelles multiples**, **Structures de tarification diverses**et **Opérations internationales**. 
Les **Module de facturation iTextPRO** répond à ces défis avec des caractéristiques avancées qui assurent des opérations simplifiées, précises et rentables.

---

## 1. Mise en place de la monnaie de base

- **Importance**: assure la cohérence et l'exactitude des transactions financières.
- **Recommandation**: Euro (EUR) est largement utilisé dans l'industrie mondiale de l'agrégation SMS.
- **Examen**: Une fois la monnaie de base réglée, la modifier peut être complexe. Décidez au début du voyage d'affaires.

---

## 2. Comprendre les codes MCC et MNC

- **MCC (Code pays mobile)** et **MNC (Code réseau mobile)** sont essentiels pour personnaliser les prix basés sur les réseaux mobiles dans un pays.
- **Prix de l'opérateur**: De nombreux opérateurs de télécommunications fondent leur tarification sur des combinaisons MCC + MNC.
- **Flexibilité**: iTextPRO active **tarification spécifique au réseau** pour une plus grande optimisation des recettes.

---

## 3. Comprendre le préfixe pour les numéros mobiles d'ingénierie inverse

- **Objet**: Indique l'origine et le réseau d'un numéro mobile.
- **Préfixe**: Les 3-4 premiers chiffres aident à détecter **Code pays** et **Réseau mobile**.
- **Exemple**: 
  - Numéro: <span data-ph="0"></span> 
  - Code pays: <span data-ph="0"></span> (EAU) 
  - Avec prix forfaitaire : le calcul des coûts est simple. 
  - Avec les prix MCC/MNC: Une recherche supplémentaire est nécessaire (aucun outil actuel ne fournit MCC/MNC directement à partir de ce numéro).

![Manage Countries](images/managecountries1.png)

---

## 4. Conversion des devises

- **Monnaie de base**: Utilisé pour les transactions internes.
- **Affichage de la monnaie**: Les utilisateurs peuvent visualiser les transactions dans leur devise préférée.
- **Prestations**: Simplifie les opérations internationales tout en maintenant l'exactitude comptable.

---

## 5. Politique de protection contre les pertes

- **Outil de fuite des recettes**: Indique les pertes potentielles en temps réel.
- **Mesures préventives**: Arrête les transactions causées par des typos, des manipulations de nombres ou des erreurs d'administration.
- **Protection financière**: Protège contre les pertes de revenus et assure la précision de facturation.

---

## Principaux avantages

- **Simplification opérationnelle** – Facturation globale simplifiée des SMS. 
- **Prix précis** – Contrôle au niveau du réseau pour des prix compétitifs. 
- **Traitement clair des devises** – Base sans couture et affichage de la gestion des devises. 
- **Sécurité financière** – Politiques automatisées de prévention des pertes. 

---

# Gestionnaire de données principal

Les **Gestionnaire de données principal** section contient quatre options de configuration clés:

1. **Gérer les pays** 
2. **Gestion du MCC/MNC** 
3. **Gérer le préfixe** 
4. **Gérer le prix de la passerelle**

---

## 1. Gérer les pays

Les **Gérer les pays** fonctionnalité permet la configuration et la gestion de la terminaison du trafic SMS dans plusieurs pays.

![Manage Countries](images/managecountries2.png)

### Ajouter un seul pays

- **Nom du pays** – Nom complet du pays pour une identification claire. 
- **Code pays** – Identifiant unique pour le routage. 
- **Code ISO du pays** – Code normalisé pour la compatibilité mondiale. 
- **Ajouter un processus** – Cliquez **Ajouter** d'inclure le pays dans la liste maîtresse.

![Single Country Add](images/managecountries3.png)

---

### Fonctionnalité du chargement en vrac

![Bulk Upload](images/managecountries4.png)

- **Télécharger l'exemple Excel** – Pré-formaté avec tous les pays pour un montage facile. 
- **Choisissez Fichier & Télécharger** – Prend en charge plusieurs entrées à la fois. 
- **Cartographie des colonnes** – Carte des champs Excel vers **Nom du pays**, **ISO**et **Code**. 
- **Soumettre & afficher** – Ajouter des pays en vrac et personnaliser l'affichage des enregistrements.

![Bulk Upload Results](images/managecountries5.png)

---

### Fonction action

![Action Options](images/managecountries6.png)

- **Modifier** – Mettre à jour les détails existants. 
- **Mise à jour** – Actualiser les données nationales. 
- **Supprimer** – Supprimer les entrées inutilisées. 

---

**Meilleure pratique :** 
Examiner et mettre à jour régulièrement votre **Gestionnaire de données principal** veiller à ce que les configurations des pays et des réseaux restent exactes en ce qui concerne les prix et l'acheminement.
