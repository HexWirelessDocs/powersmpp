---
tags:
  - HTTP
  - DLR
  - Handler
  - Configuration
---

# Configuration du gestionnaire HTTP DLR

Une fois la passerelle HTTP configurée sur l'application, l'utilisateur pourra envoyer des messages et la réponse sera mise à jour sur l'application.

!!! note
 Les **Réponse de la passerelle** est seulement le **1ère réponse** qui indique si les messages ont été soumis au fournisseur avec succès ou non.

Pour recevoir le **DLR (Recueil de livraison)** du fournisseur, l'administrateur doit configurer un **Handler HTTP DLR** de sorte que chaque fois que le fournisseur envoie le DLR, le DLR sera mis à jour sur l'application en utilisant le gestionnaire DLR.

Dans ce document, nous partagerons toutes les étapes et configurations qui doivent être effectuées par l'administrateur pour recevoir correctement le DLR sur l'application.

![Manage HTTP DLR Handler list](images/dlrhandler-01-list.png)

---

## Navigation

<span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span> - Oui. <span data-ph="3"></span>.

![Add New Handler form with Method selector](images/dlrhandler-02-add-new.png)

---

## Exemple de charge utile DLR

Pour configurer le Handler HTTP DLR, nous aurions besoin du **Format de réponse DLR** ou un exemple de DLR du fournisseur afin que l'administrateur puisse compléter la configuration sur l'application.

Par exemple, nous utiliserons l'échantillon DLR ci-dessous pour HTTP DLR Handler Configuration:

```json
{
    "messageId": "161a9168-623c-4411-9e30-cf69353f9bef",
    "status": "EXPIRED",
    "errorCode": "1039",
    "mobile": "91123537072",
    "shortMessage": "Test Message",
    "doneDate": "2024-05-22 11:07:46"
}
```

---

## Étapes de configuration

Suivez les étapes ci-dessous pour configurer le gestionnaire DLR pour l'échantillon DLR fourni ci-dessus:

1. **Ajouter un nom convivial** pour le gestionnaire.
2. **Whitelist IP du vendeur** *(Non obligatoire)*.
3. **Sélectionnez la méthode prise en charge** par le vendeur — <span data-ph="0"></span> ou <span data-ph="1"></span>.
4. **Configurer les charges utiles** — Sous les charges utiles, le client doit configurer le nom du paramètre qui stocke les valeurs spécifiques.

### Référence de la cartographie sur le terrain

| Champ d'application | Cartes à la clé JSON | Exemple de valeur |
|-------------------|------------------|---------------|
| **MessageId** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **État du message** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Date de réalisation** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Code d'erreur** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Numéro mobile** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **ID de l'expéditeur** | *(optionnel, carte si le vendeur l'envoie)* | — |
| **Message** | <span data-ph="0"></span> | <span data-ph="0"></span> |

!!! tip
 Dans l'exemple ci-dessus, le paramètre <span data-ph="0"></span> stocke la valeur du statut DLR et <span data-ph="1"></span> stocke la valeur du code d'erreur. Ces paramètres doivent être configurés comme dans **État du message** et **Code d'erreur** respectivement. Appliquer la même logique pour tous les autres paramètres partagés par le fournisseur.

![Handler configured with payload mapping](images/dlrhandler-03-configured.png)

---

## Point d'arrivée local

Lorsque le gestionnaire est sauvegardé, Power SMPP génère une **Point d'arrivée local** URL (par exemple, <span data-ph="0"></span>). C'est l'URL que le fournisseur rappellera avec les charges utiles DLR.

!!! warning "Important"
 Une fois que tous les détails ont été configurés sur l'application, **enregistrer et s'il vous plaît contacter votre fournisseur de passerelle et leur demander de blanc liste le point d'extrémité du gestionnaire DLR à leur fin**.

---

## Valeurs par défaut

Pour **État du message** et **Code d'erreur** champs, une option <span data-ph="0"></span> peut être configuré. La valeur par défaut est appliquée lorsque le fournisseur ne retourne pas ce champ dans un DLR particulier. Cela garantit que le dossier du DLR est toujours complet et que le message est clos dans les rapports.

---

## Vérification

Après configuration du gestionnaire DLR:

1. Envoyer un message de test à travers la passerelle HTTP correspondante.
2. Demandez au vendeur (ou utilisez un outil de test tel que <span data-ph="0"></span> / <span data-ph="1"></span>) pour envoyer un exemple de charge utile DLR à l'URL d'extrémité locale.
3. Ouvrir les **Rapport DLR** dans <span data-ph="0"></span> pour confirmer que le DLR a été reçu et analysé correctement.

Si le DLR n'apparaît pas, revérifiez les mappages de nom de paramètre — la cause la plus courante est un décalage entre la clé JSON que le fournisseur envoie et la clé configurée dans le gestionnaire.
