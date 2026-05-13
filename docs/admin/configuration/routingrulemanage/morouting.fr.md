---
tags:
  - MO
  - Routing
  - Rules
  - Configuration
---

# MO Règles d'acheminement

## Aperçu général

**MO Règles d'acheminement** dans iTextPro sont utilisés pour définir comment les messages MO entrants devraient être identifiés, filtrés et acheminés dans la plate-forme.

La règle de routage détermine :

- Quel trafic MO entrant devrait être traité
- Quel mot-clé devrait déclencher le routage
- Quel utilisateur devrait recevoir le trafic MO
- Quel type d'interface devrait être utilisé pour la livraison

MO Routing Rules travaillent ensemble avec la configuration **Serveur HTTP MO**.

---

## Voie de navigation

<span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span> - Oui. <span data-ph="3"></span>.

![Manage MO Routing Rules list](images/morouting-01-list.png)

---

## MO Paramètres des règles d'acheminement

Les paramètres suivants doivent être configurés lors de la création de la règle de routage.

## Paramètres généraux

### 1] Nom de la règle

Les **Nom de la règle** identifie uniquement la règle d'acheminement MO dans la plate-forme.

Ce nom est utilisé pour :

- Gestion des règles
- Surveillance de la circulation
- Administration
- Dépannage

!!! example
    ```
    MO_ROUTE_KEYWORD_01
    ```

---

### 2] Durée de vie

Les **Durée de vie** paramètre définit la durée de validité de la règle de routage.

**Utilisation :**

- Peut être utilisé pour des campagnes temporaires
- Prend en charge le routage de MO basé sur le temps
- Utile pour les services à temps limité

!!! tip
 Si aucune expiration n'est requise, ce champ peut être laissé en blanc.

---

## Configuration de l'interface de passerelle

### Maître

Les **Maître** champ est utilisé pour sélectionner le HTTP MO Handler précédemment configuré dans la plate-forme.

Ce gestionnaire traitera toutes les demandes MO correspondant aux conditions d'acheminement. Le gestionnaire sera utilisé si le fournisseur envoie MO avec **Connexion HTTP**.

### Passerelle

Dans le cas où le fournisseur supporte **SMPP** protocole pour envoyer les touches MO, puis lors de la création de la règle MO Routing l'administrateur doit sélectionner le **Passerelle** et choisissez la passerelle correcte afin de récupérer les hits de la passerelle correcte.

**Objet:**

- Liens entre le trafic MO et le bon paramètre
- Associés routage avec le canal entrant
- Active le flux de traitement des messages

![Add New MO Rule — General Parameters & Gateway Interface](images/morouting-02-general.png)

---

## Conditions d'acheminement

Les conditions d'acheminement définissent **logique de filtrage** pour le trafic MO entrant. La plateforme évalue ces conditions avant le traitement ou le routage de la demande MO.

### 1] État de l'auteur

Les **Auteur** condition définit le filtrage basé sur le numéro mobile de l'expéditeur.

**Exemple de configuration :** <span data-ph="0"></span>

Sélection **Aucune** permet les messages MO de tous les numéros d'expéditeur. Le filtrage spécifique de l'expéditeur peut également être configuré si nécessaire.

---

### 2] État de destination

Les **Destination** la condition définit le code abrégé ou le numéro de code long.

| Champ | Valeur |
|-------|-------|
| **Type de condition** | <span data-ph="0"></span> |
| **Exemple** | <span data-ph="0"></span> |

La règle de routage ne déclenchera que si le message MO entrant est reçu sur le numéro de destination configuré.

---

### 3] État du message

Les **Message** condition définit les critères de correspondance des mots-clés.

| Champ | Valeur |
|-------|-------|
| **Type de condition** | <span data-ph="0"></span> |
| **Exemple de mot clé** | <span data-ph="0"></span> |

La règle de routage ne déclenchera que si le message entrant commence par le mot-clé configuré.

!!! example
 Pour un message entrant <span data-ph="0"></span>, puisque le message commence par <span data-ph="1"></span>, la règle de routage traitera la requête MO.

![Routing Conditions and User / Endpoint selection](images/morouting-03-condition-user.png)

---

## Cartographie des utilisateurs et des points d'arrivée

### 1] Utilisateur

Sélectionnez la **compte utilisateur** à laquelle le trafic MO devrait être cartographié et livré.

Cette cartographie garantit que l'utilisateur correct reçoit les messages MO entrants.

### 2] Type d'interface utilisateur

Les **Type d'interface utilisateur** définit comment le message MO doit être transmis après le routage.

**Types d'interface pris en charge :**

| Type | Désignation des marchandises |
|------|-------------|
| **Non sélectionné** | Aucun routage spécifique à l'interface ne sera appliqué. |
| **ESME** | Route le trafic MO via la connectivité SMPP. Généralement utilisé lorsque l'utilisateur est connecté via le protocole SMPP. |
| **Webhook** | Route le trafic MO vers un paramètre externe de l'API HTTP. Utilisé couramment pour les intégrations CRM, les applications tierces, les systèmes de traitement en ligne et les workflows basés sur l'API. |

---

## Enregistrer la règle d'acheminement

Après avoir configuré tous les paramètres de routage :

1. Vérifier les conditions de routage.
2. Valider la configuration du mot-clé.
3. Cliquez sur **Enregistrer**.

La règle d'acheminement MO est maintenant configurée avec succès et active pour le traitement du trafic MO.

!!! tip "Vérification"
 Après avoir enregistré la règle, envoyez un message MO test qui correspond aux conditions configurées (sender autorisé, numéro de destination correct, message commençant par le mot-clé configuré) et confirmez que la règle s'allume en vérifiant les journaux de MO ou de webhook de l'utilisateur.
