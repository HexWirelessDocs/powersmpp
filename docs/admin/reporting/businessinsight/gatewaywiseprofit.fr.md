---
tags:
  - Reporting
  - Business Insight
  - Gateway
  - Profit
---

# Rapport sur les bénéfices sage de la passerelle

**Navigation:** <span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span>.

## Aperçu général

Les **Rapport sur les bénéfices sage de la passerelle** fournit aux administrateurs une ventilation détaillée de la rentabilité au niveau de la passerelle et de l'analyse du trafic SMS. Il est conçu pour appuyer l'analyse financière, la vérification de la facturation et le suivi du rendement des passerelles en présentant **coût d'achat**, **Valeur des ventes**et **marges bénéficiaires** pour le trafic SMS acheminé par chaque passerelle.

---

## 1. Sélection de la passerelle

Sélectionnez une passerelle spécifique à partir de la liste déroulante pour générer un rapport de profit étendu au trafic de cette passerelle.

![Gateway Wise Profit — Gateway dropdown selection](images/gwprofit-01-gateway-dropdown.png)

---

## 2. Sélection des pays

Le rapport peut être filtré davantage par le pays de destination, ce qui permet une analyse granulaire de la rentabilité au niveau du pays.

![Gateway Wise Profit — Country filter dropdown](images/gwprofit-02-country-filter.png)

---

## 3. Filtre de portée de date

Les administrateurs peuvent définir une **plage de dates personnalisées** générer des rapports de profits pour toute période historique.

!!! info "Caractéristiques de la plage de dates"
    - Analyse quotidienne et historique du trafic
    - Filtrage flexible basé sur la date
    - Appui à la vérification de la période de facturation
    - Examen du rendement opérationnel sur toute période

---

## 4. Rapport d'affichage des tableaux

Les **Affichage du tableau** présente les données sur les bénéfices des passerelles par pays dans un format tabulaire structuré avec les colonnes suivantes:

| Colonne | Désignation des marchandises |
|--------|-------------|
| **Nom de la passerelle** | La passerelle achemine le trafic. |
| **Nom du pays** | Pays de destination du trafic. |
| **MCCMNC** | Code pays mobile + Code réseau mobile. |
| **Nom du réseau** | Réseau mobile de destination. |
| **Nombre de messages** | Total des messages SMS acheminés pour cette tranche. |
| **Prix d'achat** | Coût d'acheminement pour cette tranche. |
| **Prix de vente** | Les revenus de cette tranche. |
| **Marge (ventes − achat) %** | Pourcentage des bénéfices calculés. |
| **Marge (ventes − achat) (EURO)** | Valeur absolue des bénéfices en EURO. |

![Gateway Wise Profit — Table View](images/gwprofit-03-table-view.png)

!!! note
 <span data-ph="0"></span> contre un prix indique que le prix est un prix forfaitaire.

---

## 5. Rapport d'affichage graphique

Les **Affichage graphique** offre une représentation graphique à barres visuelle de la rentabilité des passerelles, permettant d'identifier rapidement les passerelles ou les pays de destination à haut rendement et à faible rendement.

![Gateway Wise Profit — Graph View (Margin bar chart)](images/gwprofit-04-graph-view.png)

---

## 6. Formule de calcul des bénéfices

Le rapport utilise les formules standard suivantes pour calculer les paramètres de rentabilité :

```
Margin (Base Currency) =  Sales Price − Purchase Price

Margin Percentage (%)  = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

---

## But du rapport sur les bénéfices sage de la passerelle

!!! info "Utilisez ce rapport pour..."
    - Surveiller la rentabilité de la passerelle en temps réel
    - Comparer les marges par pays et par passerelle
    - Suivre le volume du trafic SMS et les coûts connexes
    - Examiner les revenus de la passerelle par rapport au coût d'achat
    - Appuyer les rapports financiers et la vérification de la facturation
    - Optimiser les stratégies de routage pour une meilleure gestion des recettes
    - Rapports d'exportation pour l'analyse hors ligne et la tenue de dossiers
