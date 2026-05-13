---
tags:
  - HTTP
  - OAuth
  - Handler
  - Configuration
---

# Configuration des mains OAuth

Dans **Gateway HTTP**, nous soutenons **3 types d'autorisation**:

| ♪ | Type | Désignation des marchandises |
|---|------|-------------|
| 1 | **Pas d'heure** | Aucune autorisation n'est requise. |
| 2 | **Niveau de base** | Un nom d'utilisateur et un mot de passe sont requis pour l'authentification sécurisée de l'API. |
| 3 | **Auth 2.0** | La dernière version de l'autorisation, utilisée pour régénérer de nouveaux identifiants après une certaine période pour maintenir une haute sécurité de l'API en utilisant **Maître OAuth** API. |

Dans ce document, nous expliquerons toutes les étapes et toutes les informations requises pour **Maître OAuth** configuration pour la passerelle HTTP.

![Manage OAuth Handler list](images/oauthhandler-01-list.png)

---

## Navigation

<span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span> - Oui. <span data-ph="3"></span>.

![Manage OAuth Handler form](images/oauthhandler-02-add-new.png)

---

## Champs OAuth Handler

| Champ | Requis | Désignation des marchandises |
|-------|----------|-------------|
| **Nom** | Oui | Un nom convivial pour le gestionnaire OAuth. Il aide à identifier et gérer facilement différents gestionnaires OAuth dans l'application. |
| **URL token** | Oui | Le paramètre URL où l'application demandera le jeton OAuth. C'est l'URL fournie par le fournisseur pour obtenir le jeton d'accès. |
| **Heure d'expiration** | Oui | La durée en minutes pour laquelle le jeton d'accès restera valide. Après cette période, le jeton expirera, et il faudra en créer un nouveau. |
| **Code d'expiration des jetons** | Oui | Le code d'erreur indiquant que le jeton a expiré. Lorsque ce code d'erreur est reçu, le système saura qu'il doit rafraîchir le jeton. |
| **Méthode de demande** | Oui | La méthode HTTP utilisée pour demander le jeton à partir de l'URL Token — <span data-ph="0"></span> ou <span data-ph="1"></span>. |
| **Type de réponse** | Oui | Le format dans lequel la réponse de l'URL Token sera reçue — <span data-ph="0"></span>, <span data-ph="1"></span>ou <span data-ph="2"></span>. |
| **Champ d'accès** | Facultatif | Le nom du champ dans la réponse qui contient le jeton d'accès. Le système extrait le jeton d'accès de ce champ pour authentifier les demandes futures. |
| **Rafraîchir le champ** | Facultatif | Le nom du champ dans la réponse qui contient le jeton rafraîchissant. Le jeton de rafraîchissement est utilisé pour obtenir un nouveau jeton d'accès lorsque le jeton actuel expire. Ce champ est facultatif selon l'implémentation du fournisseur. |

---

## Charge utile

Cette section permet à l'administrateur de définir **paires de valeurs clés supplémentaires** qui doivent être envoyées avec la demande de jeton.

| Champ | Désignation des marchandises |
|-------|-------------|
| **CLÉS** | Le nom du paramètre à inclure dans la requête. |
| **VALEUR** | La valeur du paramètre à inclure dans la requête. |
| **TYPE DE PARAM** | Spécifie le type de paramètre. Les types de paramètres communs comprennent : <span data-ph="0"></span>, <span data-ph="1"></span>, etc. |

!!! example
    - **CLÉS**: <span data-ph="0"></span>
    - **VALEUR**: <span data-ph="0"></span>
    - **TYPE DE PARAM**: <span data-ph="0"></span> *(indiquant que ce paramètre sera inclus dans le corps de la requête de jeton)*

Cette configuration aide à configurer **Authentification OAuth** pour accéder aux API en automatisant le processus d'obtention et de rafraîchissement des jetons.

---

## Comment ça marche

1. Quand un message doit être envoyé via une passerelle HTTP qui utilise **Auth 2.0**, Power SMPP vérifie d'abord si un jeton d'accès valide (non expiré) est déjà mis en cache.
2. Si un jeton valide existe, il est attaché à l'appel d'API sortant (généralement via un <span data-ph="0"></span> en-tête).
3. Si aucun jeton valide n'existe — ou si le jeton a expiré et configuré **Code d'expiration des jetons** est retourné par la passerelle — Power SMPP appelle le **URL token** avec la configuration <span data-ph="0"></span>, <span data-ph="1"></span>et <span data-ph="2"></span> Des paires.
4. La réponse est analysée en utilisant la **Type de réponse**, les **Champ d'accès** est extrait, et le jeton est mis en cache pour la durée de **Heure d'expiration**.
5. Les requêtes de messages sortants utilisent maintenant le jeton nouvellement obtenu jusqu'à ce qu'il expire à nouveau.

---

## Lien entre le manuel OAuth et une passerelle HTTP

Après avoir sauvé le manuel OAuth:

1. Ouvrez la passerelle HTTP que vous souhaitez sécuriser avec OAuth.
2. Sous **Section 1 : Pouvoirs requis**, ensemble **Authentification** à **Auth 2.0**.
3. Des **Maître OAuth** déroulant, choisissez le gestionnaire que vous venez de créer.
4. Sauvez la passerelle.

La passerelle HTTP va maintenant utiliser le mandant OAuth configuré pour obtenir et rafraîchir automatiquement les jetons — aucune rotation manuelle de jeton n'est requise.

!!! tip
 Gardez **Heure d'expiration** un peu plus court que la valeur annoncée par le fournisseur (par exemple, <span data-ph="0"></span> minutes si les jetons du vendeur sont derniers <span data-ph="1"></span> minutes). Cela évite les conditions de course où la première demande après expiration échoue avant que le rafraîchissement ne soit déclenché.
