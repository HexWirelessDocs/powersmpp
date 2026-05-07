---
tags:
  - Routing
  - Configuration
  - MT
---

## Gestionnaire de règles d'acheminement

L'acheminement joue un rôle crucial dans le maintien d'un avantage concurrentiel et la maximisation des recettes. Les **Gestionnaire de règles d'acheminement** dans iTextPRO permet une transmission efficace du trafic SMS utilisateur à sa destination ultime par une logique de routage dynamique et intelligente.

Les applications SMPP prennent en charge plusieurs chemins de routage. iTextPRO simplifie cette complexité en vous permettant de créer des règles dynamiques d'acheminement MT (Mobile Termined) qui améliorent les performances de livraison, réduisent les coûts et distribuent le trafic intelligemment.

Les principaux avantages sont les suivants :
- Sélection de la passerelle en fonction du délai de livraison
- Optimisation des coûts via le routage le moins coûteux
- Togging dynamique entre les protocoles HTTP et SMPP
- Distribution en temps réel du trafic et équilibre des charges

Une fois à l'intérieur **MT Règles d'acheminement** section, une liste des règles de routage déjà configurées sera affichée. Vous pouvez **Modifier** toute règle en cliquant sur l'icône d'édition.

!!! tip
 Aucun redémarrage ou recharge manuel n'est nécessaire. Toutes les mises à jour des règles de routage sont appliquées à la volée.

---

### Gérer la règle d'acheminement MT

![Manage Routing Rule](images/routingrule1.png)

Pour créer une nouvelle règle, cliquez sur la **"Ajouter une nouvelle règle MT"** bouton. Vous serez invité à configurer les éléments suivants :

#### 1. **Nom de la règle**
- Saisissez un nom descriptif amical pour faciliter l'identification.

#### 2. **Type de filtre**
- Deux types de filtres sont disponibles :

##### **Passer par le filtre**
- Conçu pour les politiques de routage globales.
- Il est recommandé de créer une règle de passage hautement prioritaire pour servir de voie de repli.

![Pass Through Filter](images/routingrule2.png)

##### **Filtre personnalisé**
- Messages d'itinéraire basés sur des paramètres plus spécifiques:

![Custom Filter](images/routingrule3.png)

- **Code pays**: Sélectionnez le pays pour l'acheminement du trafic SMS.
- **MCC/MNC**: Choisissez un réseau mobile spécifique du pays sélectionné.
- **Utilisateur**: Appliquer la règle à un utilisateur individuel.
- **Groupe d'utilisateurs**: Appliquer la règle à un groupe spécifique d'utilisateurs.
- **Date de début et de fin**: Définir la période de validité de la règle.
- **Adresse source**: Définir le routage source-adresse spécifique.
- **Adresse de destination**: Définir le routage spécifique à destination-adresse.

---

### Politiques d'acheminement

Vous pouvez définir des politiques de routage en fonction des exigences opérationnelles ou des SLA. Les politiques d'acheminement disponibles comprennent :

#### **LCR (acheminement des coûts les plus bas)**
- Route le trafic à travers la passerelle du fournisseur offrant le coût configuré le plus bas pour une destination donnée.
- Aide à optimiser les prix et augmenter les marges bénéficiaires.

#### **Portail fixe**
- Tout le trafic est acheminé à travers une seule passerelle prédéfinie.

#### **Rond Robin**
- Distribue le trafic uniformément sur les passerelles sélectionnées.
- Assurer une utilisation optimale de toutes les passerelles configurées.

#### **Distribué**
- Méthode avancée d'équilibrage des charges.
- Route le trafic vers plusieurs passerelles en fonction des ratios (p. ex., 60 %, 30 %, 10 %).

#### **ACD/DLR (livraison reconnue)**
- Aussi appelé routage basé sur la livraison.
- Route le trafic vers la passerelle du fournisseur avec le plus haut rapport de livraison (DLR), assurant des performances de qualité en temps réel.

---

### Traitement des priorités

!!! info "Traitement des priorités"
 Si plusieurs règles de routage correspondent à un message, **iTextPRO sélectionnera la règle avec la valeur la plus prioritaire** (numériquement le plus élevé).

Cette puissante logique de routage assure que votre trafic SMS est livré efficacement, économiquement et dans le respect de la logique d'affaires, sans interruption de service ni redémarrage du système.
