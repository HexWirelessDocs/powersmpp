---
tags:
  - SMPP
  - Error Codes
  - Reference
  - Gateway
---

# Liste standard des codes d'erreur SMPP

Cette page fournit une référence complète de tous les codes d'erreur de protocole SMPP, les codes d'erreur d'application iTextPro et les codes d'erreur de passerelle HTTP iTextHub. Utilisez cette référence pour diagnostiquer les défaillances de livraison de messages observées dans les rapports, les journaux PDU et les téléspectateurs d'événements.

---

## Codes d'erreur standard SMPP

Il s'agit de codes d'erreur au niveau du protocole définis par la spécification SMPP v3.4. Ils sont retournés par le SMSC (Centre de services aux messages courts) en réponse aux opérations du SMPP.

| Sr. Non | Code d'erreur (Hex) | Code d'erreur (décimal) | Nom de l'erreur | Description de l'erreur |
|--------|-----------------|---------------------|------------|-------------------|
| 1 | 0x00 | 0 | Commande exécutée avec succès | La commande SMPP a été traitée sans erreur |
| 2 | 0x01 | 1 | La longueur du message est invalide | La longueur du message dépasse les limites autorisées |
| 3 | 0x02 | 2 | La longueur de commande est invalide | Le champ de longueur de commande PDU est incorrect |
| 4 | 0x03 | 3 | ID de commande non valide | L'ID de commande n'est pas reconnu par le SMSC |
| 5 | 0x04 | 4 | Statut BIND incorrect pour une commande donnée | L'ESME a tenté une commande qui n'est pas autorisée dans son état de liaison actuel |
| 6 | 0x05 | 5 | ESME Déjà dans l'État de Bound | L'ESME est déjà lié et ne peut pas relier |
| 7 | 0x06 | 6 | Drapeau prioritaire non valide | La valeur du drapeau prioritaire dans le PDU n'est pas valide |
| 8 | 0x07 | 7 | Drapeau de livraison enregistré non valide | La valeur du drapeau de livraison enregistré n'est pas valide |
| 9 | 0x08 | 8 | Erreur système | Une erreur générale du système s'est produite sur le SMSC |
| 10 | 0x0A | 10 | Adresse de source non valide | L'adresse source (sender) est invalide ou non autorisée |
| 11 | 0x0B | 11 | Adresse de destination non valide | L'adresse de destination (bénéficiaire) est invalide |
| 12 | 0x0C | 12 | L'identifiant du message est invalide | L'ID du message référencé n'existe pas |
| 13 | 0x0D | 13 | Échec du bind | L'opération de liaison a échoué en raison de problèmes d'authentification ou de configuration |
| 14 | 0x0E | 14 | Mot de passe non valide | Le mot de passe fourni lors de bind est incorrect |
| 15 | 0x0F | 15 | ID système non valide | L'ID système fourni pendant la liaison n'est pas reconnu |
| 16 | 0x11 | 17 | Annuler l'échec SM | L'opération annulation sm n'a pas pu être terminée |
| 17 | 0x13 | 19 | Remplacer SM échoué | L'opération de remplacement sm n'a pas pu être terminée |
| 18 | 0x15 | 21 | Type de service non valide | Le paramètre service type n'est pas valide |
| 19 | 0x33 | 51 | Nombre de destinations non valable | Le nombre de destinations dans submit multi est invalide |
| 20 | 0x34 | 52 | Nom de la liste de distribution non valide | Le nom de la liste de distribution référencé n'existe pas |
| 21 | 0x40 | 64 | Le drapeau de destination est invalide (submit multi) | Le dest flag dans submit multi contient une valeur invalide |
| 22 | 0x42 | 66 | Soumettre w/remplacer sans support | Soumettre avec la fonctionnalité de remplacement a été demandé si elle n'est pas soutenue ou inappropriée pour le MC particulier |
| 23 | 0x43 | 67 | Données de champ esm class non valides | Le champ esm class contient des données non valides |
| 24 | 0x44 | 68 | Impossible de soumettre à la liste de distribution | Le message ne peut pas être soumis à la liste de distribution spécifiée |
| 25 | 0x45 | 69 | submit sm, data sm ou submit multi a échoué | L'opération soumise a échoué |
| 26 | 0x48 | 72 | Adresse de la source non valide TON | Le type de numéro pour l'adresse source est invalide |
| 27 | 0x49 | 73 | Adresse source non valide NPI | L'indicateur du plan de numérotation pour l'adresse source est invalide |
| 28 | 0x51 | 81 | Adresse de destination non valide NPI | L'indicateur du plan de numérotation pour l'adresse de destination est invalide |
| 29 | 0x53 | 83 | Champ  type système non valide | Le paramètre system type n'est pas valide |
| 30 | 0x54 | 84 | Signal de remplacer si présent | Le drapeau remplace if présent contient une valeur non valide |
| 31 | 0x55 | 85 | Nombre de messages non valide | Le paramètre nombre de messages est invalide |
| 32 | 0x58 | 88 | Erreur de glissade | L'ESME a dépassé les limites de messages autorisées (grottling du SPT) |
| 33 | 0x61 | 97 | Délai de livraison non valide | Le format ou la valeur du délai de livraison prévu est invalide |
| 34 | 0x62 | 98 | Période de validité du message non valide | La période de validité du message (temps d'expiration) est invalide |
| 35 | 0x63 | 99 | L'identifiant de message prédéfini est invalide | Le message prédéfini spécifié n'a pas été trouvé |
| 36 | 0x65 | 101 | Code d'erreur de l'application permanente du récepteur ESME | Erreur d'application permanente sur le récepteur ESME |
| 37 | 0x66 | 102 | Code d'erreur du message de rejet du récepteur ESME | Le récepteur ESME a rejeté le message |
| 38 | 0x67 | 103 | La requête Query Sm a échoué | L'opération requête sm n'a pas pu être terminée |
| 39 | 0xC0 | 192 | Erreur dans la partie optionnelle du corps PDU | Les paramètres optionnels TLV du corps PDU contiennent des erreurs |
| 40 | 0xC1 | 193 | TLV non autorisé | Le paramètre TLV n'est pas autorisé pour cette opération |
| 41 | 0xC2 | 194 | Longueur du paramètre non valide | Un paramètre TLV a une longueur non valide |
| 42 | 0xC3 | 195 | TLV manquant | Un paramètre TLV requis est absent du PDU |
| 43 | 0xC4 | 196 | Valeur TLV non valable | Un paramètre TLV contient une valeur invalide |
| 44 | 0xFE | 254 | Défaut de livraison de la transaction | La transaction de message n'a pas pu être livrée |
| 45 | 0xFF | 255 | Erreur inconnue | Une erreur inconnue ou non précisée est survenue |
| 46 | 0x100 | 256 | ESME Non autorisé à utiliser le type de service spécifié | L'ESME n'est pas autorisé pour le type de service demandé |
| 47 | 0x101 | 257 | ESME Interdit d'utiliser une opération spécifiée | L'ESME est sur la liste noire ou interdit d'utiliser l'opération spécifiée |
| Annexe | 0x102 | 258 | Type de service non disponible | Le type de service demandé est actuellement indisponible |
| Autres | 0x103 | 259 | Type de service refusé | Le type de service demandé a été refusé |
| 50 | 0x105 | 261 | Source Adresse Sous-unité est invalide | Le paramètre de sous-unité d'adresse source est invalide |
| 51 | 0x106 | 262 | Destination Adresse Sous-unité est invalide | Le paramètre de sous-unité d'adresse de destination est invalide |
| 52 | 0x107 | 263 | Intervalle de fréquence de radiodiffusion est invalide | Le paramètre d'intervalle de fréquence de diffusion est invalide |
| 53 | 0x108 | 264 | Le nom de l'alias diffusé est invalide | Le nom du pseudonyme diffusé n'est pas valide |
| 54 | 0x109 | 265 | Le format de zone de diffusion est invalide | Le paramètre de format de zone de diffusion est invalide |
| 55 | 0x10A | 266 | Nombre de zones de radiodiffusion est invalide | Le nombre de zones de radiodiffusion spécifiées est invalide |
| 56 | 0x10B | 267 | Type de contenu diffusé est invalide | Le paramètre de type de contenu de radiodiffusion est invalide |
| 57 | 0x10C | 268 | Catégorie de message de radiodiffusion est invalide | La classe de message diffusé est invalide |
| 58 | 0x10D | 269 | L'opération Broadcast sm a échoué | L'opération broadcast sm n'a pas pu être achevée |
| 59 | 0x10F | 271 | L'opération Cancel broadcast sm a échoué | L'opération annulation diffusion sm n'a pas pu être terminée |
| 60 | 0x110 | 272 | Nombre de diffusions répétées est invalide | Le paramètre nombre de diffusions répétées est invalide |
| 61 | 0x111 | 273 | Groupe de service de radiodiffusion est invalide | Le paramètre du groupe de services de radiodiffusion est invalide |
| 62 | 0x112 | 274 | L'indicateur de diffusion est invalide | L'indicateur de la chaîne de radiodiffusion est invalide |
| 63 | 0x15F95 | 90005 | Exception locale | Consultez la propriété LastException pour plus de détails |

---

## Codes d'erreur iTextPro

Ce sont des codes d'erreur de niveau d'application générés par la plate-forme iTextPro / Power SMPP. Ils indiquent des problèmes de routage, de facturation, de configuration de compte ou d'exploitation du système.

| Sr. Non | Code d'erreur (Hex) | Code d'erreur (décimal) | Nom de l'erreur | Description de l'erreur |
|--------|-----------------|---------------------|------------|-------------------|
| 64 | 0x439 | 1081 | Pays | Pays non défini par admin dans Master Data Manager |
| 65 | 0x43A | 1082 | Réseau non valide | Réseau non défini par admin dans Master Data Manager |
| 66 | 0x43B | 1083 | Prix non défini | Prix non définis par admin pour chaque pays et réseau sur la passerelle primaire |
| 67 | 0x43C | 1084 | Expiré (protection contre les pertes) | Message non livré en raison de la politique de protection contre les pertes |
| 68 | 0x43D | 1085 | Défendre la route | Routage non défini par admin pour chaque pays et réseau |
| 69 | 0x43E | 1086 | Défaillance de la route | Master failover non défini par admin pour chaque pays et réseau |
| 70 | 0x43F | 1087 | Échec expiré | Message non livré en raison de la protection de perte sur la passerelle de sauvegarde |
| 71 | 0x440 | 1088 | Prix d'échec Undef | Prix non définis par admin pour chaque pays et réseau sur la passerelle de basculement |
| 72 | 0x441 | 1089 | Échec | Erreur système : Exception non prise en charge pendant le routage |
| 73 | 0x442 | 1090 | Validité du compte expirée | La validité du compte utilisateur a expiré |
| 74 | 0x443 | 1091 | Erreur de codage | Erreur système : Erreur de codage en raison de la valeur de codage de données invalide (peut être régénérée en envoyant des valeurs de codage de données sauf 0 & 8) |
| 75 | 0x444 | 1092 | Erreur OA/DA | Erreur système : Erreur OA/DA en raison de l'invalidité de Regex dans les règles de normalisation |
| 76 | 0x445 | 1093 | Message de réponse expiré | Erreur système : le message de la file d'attente a expiré en raison d'une panne prolongée de la passerelle |
| 77 | 0x446 | 1094 | Configuration de la passerelle HTTP non valide | Erreur système : Configuration de passerelle HTTP ou code de réponse non valide |
| 78 | 0x417 | 1047 | Compte utilisateur Inactif | Le compte utilisateur est inactif et ne peut pas envoyer de messages |
| 79 | 0x400 | 1024 | Compte utilisateur verrouillé | Le compte utilisateur a été verrouillé par l'administrateur |
| 80 | 0x401 | 1025 | Solde insuffisant | Solde insuffisant du compte utilisateur (prépayé) |
| 81 | 0x402 | 1026 | Modèle Mismatch | Erreur détectée dans le modèle — le contenu du message ne correspond pas au modèle approuvé |
| 82 | 0x405 | 1029 | ID de l'expéditeur non valide | ID de l'expéditeur non valide ou non approuvé détecté |
| 83 | 0x407 | 1031 | Numéro de la liste noire mondiale | Le numéro de destination est sur la liste noire mondiale |
| 83 | 0x40B | 1035 | Pas de connexion active | Aucune connexion SMPP active disponible sur la passerelle |
| 84 | 0x40C | 1036 | Erreur de serveur de requêtes | Erreur système : Erreur de serveur interne de file d'attente de messages |
| 85 | 0x40D | 1037 | Erreur du serveur Cache | Erreur système : erreur de base de données Cache |
| 86 | 0x40E | 1038 | État de connexion non valide | Erreur réseau : passerelle inaccessible |
| 87 | 0x40F | 1039 | Délai d'exécution du SMPP | Erreur réseau : sortie de la passerelle — aucune réponse reçue |
| 88 | 0x410 | 1040 | Erreur SMPP inconnue | Erreur système : Une erreur SMPP non classifiée s'est produite |
| 89 | 0x411 | 1041 | Débranchement final | La connexion SMPP a été définitivement déconnectée |
| 90 | 0x412 | 1042 | Délai final | La connexion s'est arrêtée définitivement |
| 91 | 0x413 | 1043 | Aucune passerelle trouvée | Aucune passerelle appropriée trouvée pour le routage du message |
| 92 | 0x404 | 1028 | IP non valide | Adresse IP non valide pour le compte SMPP (la validation IP a échoué) |
| 93 | 0x414 | 1044 | Spam détecté | Message échoué en raison du mot-clé spam détecté dans le contenu |
| 94 | 0x448 | 1096 | Longueur du message dépassée | La longueur du message SMS dépasse la limite autorisée |

---

## Codes d'erreur de la passerelle HTTP iTextHub

Ces codes d'erreur sont retournés par la passerelle HTTP iTextHub lors du traitement des requêtes d'API HTTP.

| Sr. Non | Code d'erreur (décimal) | Nom de l'erreur | Description de l'erreur |
|--------|---------------------|------------|-------------------|
| 95 | 110 | Erreur lors de l'obtention de la réponse texte | Impossible de récupérer la réponse texte à partir de la passerelle HTTP |
| 96 | 111 | Erreur lors de l'obtention de la réponse JSON/XML | Impossible d'analyser la réponse JSON ou XML depuis la passerelle HTTP |
| 97 | 112 | Erreur en lisant la réponse | Impossible de lire le flux de réponse HTTP |
| 98 | 113 | Erreur lors de la lecture de la réponse du résultat | Impossible d'extraire les données du résultat de la réponse HTTP |
| 99 | 114 | Erreur lors de la demande d'API REST/JSON | Impossible de faire une requête d'API REST/JSON vers la passerelle HTTP |
| 100 | 115 | Erreur lors de la demande d'API HTTP simple | Impossible de faire une simple requête d'API HTTP vers la passerelle HTTP |
| 101 | 116 | Erreur lors de la demande d'API SOAP | Impossible de faire une requête d'API SOAP vers la passerelle HTTP |
| 102 | 1095 | Erreur lors de la demande d'API SOAP/Simple/RestJson | Code d'erreur combiné pour 114, 115 et 116 (utilisé dans la dernière version) |

---

!!! tip "Comment utiliser cette référence"
    - Lorsque vous voyez un code d'erreur dans votre **Rapports de campagne**, **Registres PDU**ou **Visionneur d'événements**, regardez dans les tableaux ci-dessus
    - **Codes SMPP standard** (0–255) sont retournés par le SMSC externe/porte
    - **Codes iTextPro** (1024-1096) sont générés en interne par la plate-forme Power SMPP
    - **Codes HTTP GW** (110–1095) se rapportent à des problèmes de connectivité de passerelle HTTP
    - Pour la configuration du code d'erreur spécifique à la passerelle, voir [Codes d'erreur de passerelle](errorcode.md)
