---
tags:
  - HTTP
  - MO
  - Handler
  - Configuration
---

# Serveur HTTP MO

## Aperçu général

Les **Serveur HTTP MO** iTextPro est utilisé pour recevoir et traiter l'entrée **MO (d'origine mobile)** messages des opérateurs de télécommunications ou des fournisseurs de passerelles. Le gestionnaire agit comme un paramètre d'API qui accepte les demandes MO et transmet les données reçues à la plate-forme pour un routage et un traitement ultérieurs.

La configuration HTTP MO Handler définit :

- Méthode de communication
- Détails du canal
- Carte de la charge utile
- Restrictions à la sécurité
- Génération d'extrémités

!!! warning "Préalable"
 Cette configuration est **obligatoire** avant de créer MO Routing Rules.

---

## Voie de navigation

<span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span>.

![Manage MO Handler list](images/mohandler-01-list.png)

---

## Paramètres de configuration du manuel

Les paramètres suivants doivent être configurés lors de la création d'un Handler HTTP MO.

### 1] Nom du préposé

Les **Nom de l'utilisateur** est utilisé pour identifier uniquement la configuration MO Handler au sein de la plate-forme.

Ce nom est utilisé en interne pour :

- Configuration de routage
- Sélection manuelle
- Carte du trafic MO
- Administration et dépannage

!!! example
    ```
    MO_HANDLER_INDIA_01
    ```

---

### 2] Type de canal

Les **Type de canal** définit le type de numéro de télécommunication associé au trafic MO entrant.

**Types de canaux pris en charge :**

| Type | Désignation des marchandises |
|------|-------------|
| **Code long** | Un numéro mobile standard utilisé pour la communication bidirectionnelle. |
| **Code abrégé** | Code numérique court généralement utilisé pour les campagnes d'entreprise, les systèmes de vote, les abonnements ou les services promotionnels. |

Le type de canal sélectionné doit correspondre à la configuration de l'opérateur ou du fournisseur.

![Manage MO Handler — full configuration form](images/mohandler-02-add-new.png)

---

### 3] Numéro de canal

Les **Numéro de canal** représente le numéro de destination réel sur lequel le trafic MO sera reçu.

!!! example
    ```
    567890
    ```

Ce numéro doit être configuré **exactement comme prévu** par l'opérateur de télécommunications ou le fournisseur de passerelle.

---

### 4] Point d'arrivée local

Les **Point d'arrivée local** est généré automatiquement par iTextPro une fois la configuration du gestionnaire créée.

Ce paramètre sert d'URL de réception pour les requêtes HTTP MO entrantes.

L'URL générée est généralement partagée avec :

- Fournisseurs de passerelle SMS
- Opérateurs de télécommunications
- Agrégateurs
- Plateformes tierces

Le fournisseur utilise ce paramètre pour pousser les messages MO entrants dans la plate-forme iTextPro.

**Exemple de débit :**

```
Operator/Vendor → Local Endpoint → iTextPro Processing
```

---

### 5] Liste blanche IP

Les **IP de liste blanche** la section est utilisée pour sécuriser le paramètre MO en limitant l'accès aux adresses IP autorisées.

Seules les demandes reçues d'adresses IP configurées seront acceptées par la plateforme.

**Objet:**

- Empêcher l'accès non autorisé
- Améliorer la sécurité de l'API
- Restreindre le trafic inconnu
- Protéger le paramètre MO contre les abus

!!! example
    ```
    192.168.10.20
    ```

!!! tip
 Plusieurs IP peuvent être configurés selon les besoins opérationnels.

---

### 6] Méthode

Les **Méthode** définit la méthode de communication HTTP utilisée par le fournisseur lors de l'envoi des requêtes MO.

**Méthodes soutenues :** <span data-ph="0"></span>, <span data-ph="1"></span>.

#### Méthode GET

Dans la méthode GET:

- Les paramètres sont transmis dans l'URL.
- Les données sont envoyées sous forme de paramètres de requête.
- Convient pour les intégrations légères.

!!! example
    ```
    https://domain.com/mo?originator=9876543210&destination=567890&message=TEST
    ```

#### Méthode POST

Dans la méthode POST:

- Les paramètres sont transmis dans le corps de requête HTTP.
- Soutient des charges utiles structurées et plus importantes.
- Utilisé couramment pour les intégrations d'API modernes.

**Avantages:**

- Une meilleure sécurité
- Structure de demande plus propre
- Prise en charge des charges utiles JSON / XML
- Convient aux intégrations complexes

---

## Configuration de la charge utile

Les **Charge utile** section définit comment les paramètres de requête entrants seront mapisés dans iTextPro.

La cartographie correcte de la charge utile est **obligatoire** pour une transformation réussie des MO. Configurez les paramètres de charge utile exactement comme indiqué ci-dessous:

| Paramètres de la plate-forme | Paramètres du fournisseur |
|--------------------|------------------|
| **Auteur** | <span data-ph="0"></span> |
| **Destination** | <span data-ph="0"></span> |
| **Message** | <span data-ph="0"></span> |

### Description du paramètre de charge utile

#### Auteur

Les **Auteur** paramètre représente le numéro mobile de l'expéditeur à partir duquel le message MO est reçu.

!!! example
    ```
    9876543210
    ```

#### Destination

Les **Destination** paramètre représente le **Code abrégé** ou **Code long** numéro sur lequel le message MO a été envoyé.

!!! example
    ```
    567890
    ```

#### Message

Les **Message** paramètre représente le contenu réel du texte soumis par l'utilisateur final.

!!! example
    ```
    ASKRK BALANCE
    ```

---

## Enregistrer la configuration du gestionnaire

Après toutes les configurations:

1. Vérifier tous les détails configurés.
2. Cliquez sur **Enregistrer**.

Le HTTP MO Handler est maintenant configuré avec succès et prêt à recevoir du trafic MO.

!!! tip "Prochaine étape"
 Une fois que le gestionnaire est enregistré, procéder à la création d'un **MO Règles d'acheminement** définir comment le trafic MO entrant sera filtré et livré aux utilisateurs finaux.
