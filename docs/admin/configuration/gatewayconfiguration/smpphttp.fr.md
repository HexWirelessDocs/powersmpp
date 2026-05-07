---
tags:
  - SMPP
  - Gateway
  - Configuration
---

# Configuration

## Portails SMPP (MO/MT)

Les **Application iTextPRO** hiérarchisé a **expérience conviviale** par une interface de conception flexible et un flux de travail de configuration simplifié. Le but est de s'éloigner des complexités de l'ICL et d'immerger les propriétaires d'applications dans un **Interface utilisateur graphique (GUI)**- l'environnement. Un système intégré **Moteur de communication** gère toutes les commandes backend, rationalisant vos tâches opérationnelles.

---

![Manage Gateway](images/httpgateway1.png)

---

Les **"Gérer la passerelle"** fonctionnalité permet aux utilisateurs de gérer la connectivité avec **Centres de service pour messages courts (SMSC)** par **SMPP** et **HTTP** Protocoles.

Pour **SMPP**, une **un seul lien** permet les opérations Mobile-Origine (MO), Mobile-Terminée (MT) et les rapports de livraison (DLR). Prise en charge de iTextPRO **plusieurs SMPP Portails**, permettant **redondance** et **routage rentable**.

---

### Configuration d'une nouvelle passerelle

Pour configurer un connecteur SMPP :

1. Cliquez sur **"Ajouter nouveau"**.
2. Entrez les identifiants fournis par votre **fournisseur de passerelle** ou **opérateur de télécommunications**.

---

![SMPP Gateway Credentials](images/httpgateway2.png)

---

#### Pouvoirs requis

| Champ | Désignation des marchandises |
|-------|-------------|
| **Nom de la passerelle** | Un nom convivial pour identifier votre passerelle |
| **Adresse IP** | L'IP de votre SMSC/vendor |
| **ID système** | Nom d'utilisateur fourni par votre fournisseur/SMSC |
| **Mot de passe** | Utilisé pour l'authentification du SMSC |
| **Port Tx / Port Rx / Port TxR** | Ports pour les liaisons émetteur, récepteur et émetteur-récepteur |
| **Type de système** | *(facultatif)* Inscrivez seulement si le vendeur l'exige |

!!! warning
 Vérifiez toutes les valeurs selon la documentation SMSC/vendor pour assurer une connexion réussie.

---

### Propriétés de la passerelle

![Gateway Properties](images/httpgateway3.png)

Configurer SMPP Propriétés de la passerelle dans iTextPRO pour une performance optimale:

1. **Garder en vie (deuxièmes):** 
 Intervalle *Demande de lien* pour garder la session en vie.

2. **Heure d'ouverture de la passerelle / Heure de fermeture :** 
 Définir les heures de fonctionnement, souvent utilisées pour se conformer **Ne pas déranger** politiques.

3. **Encodage de la passerelle :** 
 Sélection de caractères compatibles avec le telco/SMSC.

4. **Convertir l'ID du message :** 
 Permet la conversion entre **Décimal** Formats de message-ID pour des DLR précis.

5. **Zone horaire :** 
 Tous les rapports refléteront ce fuseau horaire choisi.

6. **Prix d'arrêt de la perte :** 
 Définit la **Coût maximum autorisé de la passerelle** lors de l'utilisation du routage aveugle.

7. **Débit par seconde (TPS):** 
 Définir en fonction de la capacité des fournisseurs. 
 **Formule:** <span data-ph="0"></span>

---

### Configuration TON/NPI

![TON/NPI Setup](images/httpgateway4.png)

- **TON (type de nombre):** 
 Sélectionner selon la documentation du SMSC (p. ex. international, alphanumérique, etc.)

- **NPI (indicateur du plan de numérotation) :** 
 Indique la norme de numérotation utilisée (E.164, RNIS, etc.)

- **Configuration de la session :** 
 Configurer les sessions Tx, Rx et TxR par fournisseur.

---

### Rôles et routage

![Gateway Roles](images/httpgateway5.png)

- **Est actif:** 
 Marque la passerelle comme en direct et prêt à parcourir le trafic.

- **Est par défaut & #160;:** 
 Une seule passerelle peut être marquée par défaut. Les messages sans itinéraires correspondants vont ici.

- **Est-ce que Async:** 
 Active **mode asynchrone** pour les transmissions de messages plus rapides.

- **Routage aveugle:** 
 Permet la transmission de messages aux pays **Sans prix de revient définis**.

!!! tip
 Après la configuration, cliquer **"Enregistrer"** envoie un **Demande de reliure à la volée** — pas de redémarrage manuel nécessaire.
