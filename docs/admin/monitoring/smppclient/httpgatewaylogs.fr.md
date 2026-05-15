---
tags:
  - Monitoring
  - HTTP
  - Gateway
  - Logs
---

# Logs de passerelle HTTP

**Navigation:** <span data-ph="0"></span> - Oui. <span data-ph="1"></span> - Oui. <span data-ph="2"></span>.

## Aperçu général

Les **Logs de passerelle HTTP** section permet aux administrateurs de visualiser le HTTP complet **demande** et **Réponse** communication échangée entre l'application PowerSMPP et les fournisseurs de passerelle configurés. Ces registres sont essentiels pour diagnostiquer les échecs de livraison, vérifier les charges utiles de l'API et vérifier les interactions de passerelle.

---

## Étapes pour afficher les journaux

1. Sélectionnez la **Gateway HTTP** des **Nom de la passerelle** à la baisse.
2. Sélectionnez le nécessaire **Gamme de dates** en utilisant le récupérateur de date.
3. Choisissez le **Type de journal** (<span data-ph="0"></span> / <span data-ph="1"></span> / <span data-ph="2"></span>) selon les besoins.
4. Sélectionnez la **Verbosité** niveau si un filtrage granulaire est nécessaire.
5. Cliquez sur **Soumettre** pour récupérer et afficher les journaux correspondants.

![HTTP Gateway Logs — Log list view](images/httplogs-01-list.png)

---

## Sections de journaux disponibles

### Organe de demande

Les **Organe de demande** contient la charge utile complète transmise depuis l'application PowerSMPP au fournisseur de passerelle.

![HTTP Gateway Logs — Request Body expanded](images/httplogs-02-request-body.png)

!!! info "Organisme requérant — Données incluses"
    - **Numéro mobile** — numéro de destination du SMS
    - **ID de l'expéditeur** — l'adresse d'origine / l'identifiant de l'expéditeur utilisé
    - **Paramètres de demande** — paramètres API complets envoyés à la passerelle
    - **Détails de l'hôte / IP** — Adresse IP et port de la passerelle
    - **Délai de soumission** — date d'envoi de la demande

### Organisme de réponse

Les **Organisme de réponse** contient l'accusé de réception et les données d'état reçues du fournisseur de passerelle.

![HTTP Gateway Logs — Response Body expanded](images/httplogs-03-response-body.png)

!!! info "Organisme de réponse — Données incluses"
    - **Réponse de la passerelle** — réponse brute retournée par la passerelle
    - **Renseignements sur l'état** — codes d'état de livraison ou d'acceptation
    - **Détails de l'erreur** — codes d'erreur et descriptions pour les communications en échec
    - **Réponse Remerciements** — confirmation que la passerelle a traité la demande

---

## Options de filtrage

Les administrateurs peuvent affiner la vue du journal en utilisant les filtres additionnels suivants:

| Filtre | Utilisation |
|--------|-----|
| **Adresse IP** | Filtrer les journaux par l'IP du serveur passerelle. |
| **ID de l'expéditeur** | Filtrer les journaux par l'identifiant d'origine de l'expéditeur. |
| **Numéro mobile** | Filtrer les journaux par numéro de téléphone mobile de destination. |

---

## Flux typique de dépannage

1. Une campagne signale des échecs inattendus ou des messages non transmis.
2. Ouvrir **Logs de passerelle HTTP**, sélectionnez la passerelle affectée et une plage de dates qui couvre le problème.
3. Jeu **Type de journal** à <span data-ph="0"></span> à la surface seulement les échanges échoués.
4. Élargir **Organe de demande** pour confirmer que la charge utile sortante était correcte.
5. Élargir **Organisme de réponse** pour lire le code d'erreur/description retourné par le fournisseur.
6. Utilisation **Adresse IP**, **ID de l'expéditeur**ou **Numéro mobile** filtres pour isoler un échantillon d'essai spécifique pour l'équipe de soutien du fournisseur.
