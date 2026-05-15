---
tags:
  - Reporting
  - Business Insight
  - Gateway
---

# Gateway Wise Count

**Navigation:** <span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span>.

## Aperçu général

Les **Gateway Wise Count** rapport fournit aux administrateurs une vue consolidée des volumes de soumission de message sur toutes les passerelles configurées. Le rapport porte sur la **sept derniers jours** par jour, ce qui facilite l'identification des schémas de trafic et de la répartition des charges en un coup d'oeil.

![Gateway Wise Count — All Gateways (7-day view)](images/gwcount-01-all-gateways.png)

---

## Utilisation du filtre Gateway

Pour restreindre le rapport à une passerelle spécifique, sélectionnez la passerelle souhaitée à partir de la **filtre déroulant** disponible sur l'écran du rapport. Le tableau se rafraîchira pour montrer seulement les données de soumission de cette passerelle.

![Gateway Wise Count — Filtered by a single gateway](images/gwcount-02-filtered.png)

---

## Ce que le rapport montre

| Colonne | Désignation des marchandises |
|--------|-------------|
| **Nom de la passerelle** | Nom amical de la passerelle configurée. |
| **Colonnes de date (une par jour)** | Nombre total de messages acheminés par cette passerelle le jour correspondant. |

!!! note
 Le nombre de messages visibles est calculé en fonction de chaque **propre fuseau horaire de la passerelle**, pas le fuseau horaire d'application. Ceci est indiqué dans la note en page au-dessus du tableau.

---

## Quand utiliser ce rapport

- Spot jour après jour des diminutions de trafic qui pourraient indiquer des problèmes de fournisseur ou de réseau.
- Identifier les passerelles sous-utilisées qui peuvent être des candidats à la retraite ou à la réaffectation.
- Vérifiez que les nouvelles passerelles reçoivent la part prévue du trafic.
- Fournir aux intervenants des instantanés de volume hebdomadaires rapides.
