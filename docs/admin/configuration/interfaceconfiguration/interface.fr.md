---
tags:
  - SMPP
  - ESME
  - HTTP API
  - Configuration
---

## Gérer l'interface

Les **Gérer l'interface** section dans iTextPRO permet aux administrateurs de configurer et gérer la connectivité des partenaires par **Connecteurs SMPP (comptes ESME)** et **Connecteurs HTTP**. Ces connecteurs améliorent les capacités de communication en permettant une intégration transparente avec les systèmes externes.

---

### 1. Connecteur SMPP (compte ESME)

![SMPP Connector](images/manage1.png)

Les **Connecteur SMPP**, également appelé **Compte ESME (entité externe de messagerie courte)**, facilite les connexions avec les partenaires **Serveur SMPP** dans iTextPRO.

#### Comment ajouter un nouveau connecteur SMPP :
1. Rechercher le compte utilisateur spécifique.
2. Cliquez sur **"Ajouter nouveau"** pour lancer la configuration.
3. Remplissez les détails requis:

**Champs de configuration des comptes ESME :**

| Champ | Désignation des marchandises |
|-------|-------------|
| **ID système** | Nom d'utilisateur utilisé pour se connecter au compte ESME |
| **Mot de passe** | Mot de passe d'authentification pour le compte ESME |
| **IP de liste blanche** | Seules les connexions de cette IP sont autorisées |
| **Tx Compte** | Nombre de sessions de l'émetteur (Tx) |
| **Nombre Rx** | Nombre de séances du receveur (Rx) |
| **Nombre TRx** | Nombre de sessions des émetteurs (TRx) |

#### Paramètres avancés & #160;:
- **Valider la PI**: Permet la validation des adresses IP source. Seules les IP de liste blanche peuvent se connecter.
- **Le compte est actif**: Une fois activé, l'utilisateur ESME peut se connecter au serveur SMPP.
- **Liste noire**: Ceci est automatiquement activé si l'utilisateur ESME viole **Règle ESME sur la liste noire**.

---

### 2. Connecteur HTTP

![HTTP Connector Setup](images/manage2.png)

Les **Connecteur HTTP** permet aux partenaires de s'intégrer à iTextPRO en utilisant **API basées sur HTTP**.

#### Étapes pour activer l'accès à l'API HTTP :
1. Activer **État de l' API** dans le compte utilisateur souhaité.
2. Une fois activé, le **API développeur** section devient visible dans l'interface utilisateur.
3. De là, les utilisateurs peuvent:
   - Affichage **Vérification des API**
   - **Télécharger la documentation de l'API** (format PDF)
   - Commencez à utiliser les paramètres de l'API HTTP pour soumettre des messages, des rapports et plus encore.

![HTTP API Dashboard](images/manage3.png)

---

### Résumé

Les **Gérer l'interface** iTextPRO offre une configuration unifiée et intuitive pour les deux **Connecteurs SMPP et HTTP**, permettant:
- Accès sécurisé et contrôlé pour les partenaires et revendeurs.
- Documentation API et outils pour une intégration facile.
- Contrôle au niveau de la session et gestion de l'accès par IP.

En exploitant ces connecteurs, les utilisateurs d'iTextPRO peuvent étendre leur portée de messagerie tout en maintenant un contrôle et une flexibilité stricts.
