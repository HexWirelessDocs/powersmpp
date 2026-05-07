
## Gestion des services

Les **Gestion des services** section dans iTextPRO fournit la visibilité dans les divers **Contexte et services de premier plan** qui conduisent les fonctionnalités de base de la plateforme. Cette interface est principalement destinée aux utilisateurs ou administrateurs experts.

!!! danger "Attention"
 Bien qu'il soit possible d'arrêter ou de démarrer un service depuis l'interface web, cela devrait être fait **avec une extrême prudence**, en particulier pendant les périodes de pointe de charge, car il peut en résulter **perte de données** ou **interruption des services**.

---

### Aperçu des services

Voici une brève description de chaque service visible **Gestion des services** rubrique:

| **Nom du service**         | **Désignation des marchandises**                                                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Service à la clientèle**       | Connecte iTextPRO à votre SMSC via SMPP pour la gestion **SMS MT (Mobile Terminé)** et **SMS MO (d'origine mobile)** La circulation.                      |
| **DLR Service**          | Poignées en temps réel **Rapports d ' exécution** et met à jour l'état des messages dans le système pour obtenir des rapports exacts.                                      |
| **Service serveur SMPP**  | Écoute le trafic SMPP entrant depuis **Utilisateurs ESME** sur un port prédéfini, permettant aux utilisateurs externes de soumettre des SMS.                                      |
| **Service de ramassage de fichiers**  | Lire les fichiers de messages de campagne téléchargés par les utilisateurs et les transmettre au **file d'attente passerelle** pour traitement.                                               |
| **Service de validation**    | Valide **paramètres de liaison** pour les utilisateurs qui se connectent par les interfaces API et SMPP, en veillant à ce que le trafic ne soit accepté que par les clients autorisés.       |
| **Service de compilation de données** | Gère le stockage de **Registres PDU** et **journaux de messages** dans la base de données pour l'enregistrement et le débogage.                                          |
| **Service de compilation de rapports** | Profils et compilations **nombres envoyés et rapports sommaires** pour les utilisateurs, en facilitant le suivi de l'utilisation et la facturation.                                            |
| **Télécharger le service de rapport** | Procéder et générer **Rapports téléchargeables** pour les administrateurs et les utilisateurs sur la base des données demandées.                                                  |
| **Service de notification** | Envois **Alerte par courriel** aux utilisateurs et aux administrateurs et moniteurs actifs **état de santé de la porte**.                                               |

---

### Caractéristiques principales

- Voir la **État actuel** de chaque service.
- Option **Démarrer** ou **Arrête** services depuis l'interface web.
- Conçu pour être utilisé par **utilisateurs ou administrateurs avancés** avec une bonne compréhension des dépendances du service.
- Chaque service comprend des métadonnées comme **version de la demande**.

---

### Meilleures pratiques

- Confirmez toujours les heures de pointe avant d'arrêter tout service critique (p. ex. client, DLR, Validateur).
- Évitez de redémarrer les services sans consulter les registres du système ou le support technique.
- S'assurer que les services de base de données et de passerelle sont synchronisés pour éviter les incohérences dans les données.

---

Les **Gestion des services** fonctionnalité offre un moyen centralisé de surveiller et de contrôler les processus au niveau du système, assurant un fonctionnement en douceur dans l'environnement iTextPRO.
