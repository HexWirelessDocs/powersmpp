---
tags:
  - Reporting
  - Business Insight
  - User
  - Profit
---

# Rapport sur les bénéfices des utilisateurs

**Navigation:** <span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span>.

## Aperçu général

Les **Rapport sur les bénéfices des utilisateurs** permet aux administrateurs d'analyser le trafic SMS au niveau de l'utilisateur et la rentabilité pour toute plage de dates sélectionnée. Le rapport est fondé sur **entièrement sur les messages soumis par les utilisateurs à travers la demande** et fournit des données détaillées sur les revenus, les coûts et la marge par compte client.

---

## 1. Sélection de l'utilisateur

Sélectionnez un compte utilisateur spécifique dans la liste déroulante pour générer un rapport de profit ciblé pour ce client.

## 2. Sélection des pays

Filtrer les données sur le trafic par pays de destination pour obtenir une analyse granulaire de la rentabilité des utilisateurs par région.

## 3. Filtre de portée de date

Définissez une plage de dates personnalisées pour générer des rapports de profit utilisateur pour toute période de facturation ou d'exploitation.

---

## 4. Rapport d'affichage des tableaux

Les **Affichage du tableau** affiche des informations détaillées sur la rentabilité par utilisateur au format tabulaire.

![User Wise Profit — Table View (all users)](images/userprofit-01-table-all.png)

![User Wise Profit — Table View (highlighted)](images/userprofit-02-table-highlighted.png)

### Référence colonne

| Colonne | Désignation des marchandises |
|--------|-------------|
| **Nom d' utilisateur** | Nom / identifiant du compte utilisateur. |
| **Nom du pays** | Pays de destination du trafic SMS de l'utilisateur. |
| **MCCMNC** | Code pays mobile + Code réseau mobile. |
| **Nom du réseau** | Nom du réseau mobile de destination. |
| **Nombre de messages** | Total des messages SMS soumis par l'utilisateur. |
| **Prix d'achat** | Frais d'acheminement réels engagés pour le traitement du trafic de l'utilisateur. |
| **Prix de vente** | Montant total de la vente facturé à l'utilisateur. |
| **Marge % (ventes − achat)** | Pourcentage de profit calculé pour le trafic de l'utilisateur. |
| **Marge (ventes − achat)** | Bénéfice total tiré du trafic des utilisateurs en USD. |

---

## 5. Rapport d'affichage graphique

Les **Affichage graphique** rend un diagramme à barres de rentabilité par utilisateur, permettant une comparaison rapide entre les clients.

![User Wise Profit — Graph View (Margin by user)](images/userprofit-03-graph-view.png)

---

## 6. Analyse de la soumission des messages

Tous les calculs du rapport sur les bénéfices des utilisateurs sont effectués **exclusivement** par les messages envoyés du côté utilisateur à travers l'application. Le trafic qui contourne le chemin de soumission de l'utilisateur de l'application n'est pas inclus dans ce rapport.

---

## 7. Formule de calcul des bénéfices

```
Margin (USD)          =  Sales Price − Purchase Price

Margin Percentage (%) = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

!!! tip
 Combiner ce rapport avec **Gateway Wise Profit** voir la rentabilité sous deux angles complémentaires: le client (côté recettes) et le vendeur (côté coûts).
