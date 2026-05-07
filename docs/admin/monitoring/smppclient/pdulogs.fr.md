---
tags:
  - Monitoring
  - PDU
  - Troubleshooting
---

# Surveillance

iTextPRO fournit des informations complètes **outils de surveillance** pour assurer des performances de livraison de SMS optimales et la stabilité du système. Cela comprend: **Surveillance en direct en temps réel** pour des informations sur le trafic et une robuste **Enregistreur PDU** pour une analyse approfondie au niveau du message.

---

## Surveillance en direct

Les **Surveillance en direct** module dans iTextPRO suit et analyse dynamiquement les points de données clés liés au trafic SMS, permettant **prise de décisions en temps réel** pour le routage et l'optimisation des performances.

### Principaux avantages
- **Gestion proactive du trafic** – Gérer dynamiquement le trafic SMS basé sur des données en direct.
- **Routage optimisé** – Prendre des décisions d'acheminement éclairées pour améliorer les taux de livraison.
- **Affectation efficace des ressources** – Allouer les ressources de façon stratégique pendant les heures de pointe.
- **Amélioration des résultats** – Améliorer la réactivité et le débit avec des informations en temps réel.

**En résumé**, Live Monitoring garantit aux utilisateurs **visibilité jusqu'à la minute** dans le flux de trafic SMS, en particulier pendant les périodes de forte demande.

---

## Registres PDU

iTextPRO emploie **Enregistreur PDU (Unité de données protocolaires)** pour capturer et enregistrer chaque message entrant ou quittant le SMSC. Cet outil est vital pour **dépannage**, **surveillance**et **maintenir** santé du système.

### Caractéristiques principales
- **Voyage de message en temps réel** – Loge chaque message en temps réel pour une analyse immédiate.
- **Capacités de filtrage** – Tracer le trajet d'un message en un seul clic.
- **Prise en charge du type PDU** – Inspecter SubmitSM, DeliverSM, Bind, Unbind, et plus encore.
- **Visibilité et conservation** – Les journaux suivent la **fuseau horaire administrateur** et sont conservés pour **3 jours**.
- **Inspection de la circulation en amont** – Voir le flux de message en sélectionnant les passerelles d'une liste déroulante.
- **Support de dépannage** – Diagnostiquez rapidement les problèmes de livraison ou de séance SMPP.

![PDU Logs](images/pdulogs1.png)

### Lignes directrices pour l'utilisation
1. Accès **Enregistreur PDU** depuis l'interface iTextPRO.
2. Appliquer **filtres** isoler et inspecter des messages spécifiques.
3. Utilisation **Registres du trafic en amont** pour vérifier les déplacements des messages.
4. Exécution **Surveillance régulière** maintenir la fiabilité du système.

---

## Niveaux de converbité dans le logging PDU

L'enregistrement de PDU par iTextPROS prend en charge plusieurs **niveaux de verbosité**, fournissant des informations détaillées sur la communication entre les passerelles iTextPRO et SMPP.

| Niveau de converbosité | Objet | Décision |
|-----------------|---------|--------|
| **Demande de reliure** | Initie la liaison SMPP | iTextPRO envoie une requête pour se connecter à la passerelle SMPP |
| **Réponse du bind** | Confirme la liaison SMPP | La passerelle SMPP répond à la demande de reliure |
| **Demande de lien / Réponse** | Contrôle de santé de la session SMPP | iTextPRO envoie une requête tous les 30 ans; la passerelle répond |
| **Soumettre SM Demande** | Demande de soumission de message | iTextPRO envoie un SMS à la passerelle SMPP |
| **Soumettre SM Réponse** | Remerciements | Gateway répond à la soumission de message |
| **Livraison SM Demande** | Réception du rapport de livraison (DLR) | La passerelle SMPP envoie l'état de livraison |
| **Livraison SM Réponse** | Remerciements de DLR | iTextPRO confirme la réception du DLR |
| **Demande non consolidée** | Fin de la session | iTextPRO ou gateway lance une requête non liée |

**Importance:** Ces journaux donnent aux administrateurs une **vue granulaire des flux de messages**, aider à détecter, diagnostiquer et résoudre les problèmes efficacement.

---

Avec **Surveillance en direct** et **Exploitation forestière par PDU**, iTextPRO habilite les administrateurs à **Système de livraison de SMS très fiable**, détecter proactivement les problèmes et optimiser le trafic en temps réel.
