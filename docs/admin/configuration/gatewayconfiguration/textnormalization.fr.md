
# Normalisation du corps du message

Les **Normalisation du corps du message** Règle est une fonctionnalité intégrée dans **Puissance SMPP**, conçu pour permettre aux administrateurs de modifier et d'affiner le contenu des messages avant de les soumettre à la passerelle. 
Cela garantit que tous les messages sortants sont bien formatés, ce qui améliore la lisibilité et l'efficacité.

Ce document explique comment **Normalisation du corps du message** fonctionne et comment les administrateurs peuvent le configurer pour ajuster automatiquement le contenu des messages en fonction de règles prédéfinies, en assurant la cohérence et le respect des exigences de passerelle.

---

## Caractéristiques principales

La règle de normalisation de l'organisme de message étend l'actuel **Règle de normalisation OA/DA**. Il fournit plusieurs façons de manipuler le contenu des messages, y compris:

- **Extraction des codes/des OTP:** Détecter et extraire automatiquement les OTP ou les codes spécifiques du texte du message. 
- **Ajouter des préfixes ou des suffixes :** Insérer un texte spécifique avant ou après le message pour maintenir un format standard. 
- **Remplacement du texte :** Remplacer certains mots ou phrases selon des règles prédéfinies pour une meilleure cohérence.

Ces options aident les administrateurs à s'assurer que tous les messages sont conformes aux normes de passerelle, ce qui améliore l'expérience globale de messagerie.

---

## Accès à la normalisation du corps des messages

Pour configurer la normalisation du corps du message :

1. Naviguez vers la **Module de configuration**. 
2. Sélectionner **Configuration de la passerelle**. 
3. Choisir **Normalisation du corps du message**. 
4. Cliquez sur **Ajouter un nouveau** créer une nouvelle règle de normalisation.

![Message Body Normalization UI](images/mbn1.png)

---

## Configuration des règles

Après avoir cliqué **Ajouter un nouveau**, une page de configuration apparaît avec plusieurs champs.

### **Nom de la règle**
Définir un nom descriptif et significatif pour la règle.

---

### **Paramètres de l' état**

#### 1. Sélectionnez l'interface
Spécifiez l'interface où la règle s'applique. Vous pouvez sélectionner un ou plusieurs des éléments suivants :

- WEB 
- API 
- SMPP 
- Toutes les interfaces 

![Interface Selection](images/mbn3.png)

Cela permet l'application de règles ciblées selon l'interface opérationnelle.

---

#### 2. Utilisateur
Choisissez si la règle s'applique à :
- Une **Utilisateur**ou 
- **TOUS** (s'applique à tous les utilisateurs).

---

#### 3. ID de l ' expéditeur
Configurer les conditions d'identification de l'expéditeur en fonction de modèles de correspondance spécifiques:

- **Égalité** – Correspond exactement à l'ID de l'expéditeur spécifié 
- **Commencez par** – Déclenche si l'identifiant de l'expéditeur commence par un mot-clé spécifique 
- **Terminer avec** – S'applique si l'identifiant de l'expéditeur se termine par un mot-clé spécifique 
- **Contient** – S'applique si le mot-clé est trouvé n'importe où dans l'ID de l'expéditeur 

![Sender ID Condition](images/mbn4.png)

---

#### 4. Adresse de destination
Fonctions similaires à **ID de l'expéditeur**, permettant les mêmes conditions — *Égalité*, *Commencez par*, *Terminer avec*, *Contient* — appliquer des règles fondées sur le format d'adresse de destination.

---

#### 5. Message
Les mêmes options conditionnelles que ci-dessus peuvent être appliquées au contenu du message, permettant un contrôle précis du formatage.

---

## Actions: explication détaillée

Dans **Puissance SMPP**, les **Décision** section offre trois méthodes configurables pour manipuler le contenu de message avant la soumission à la passerelle:

1. **Code d'extraction** 
2. **Rechercher et remplacer** 
3. **Annexer et préparer**

Chacun sert un cas d'utilisation spécifique. Laissez-les explorer chacun en détail.

---

### Code d'extraction

Les **Code d'extraction** action permet aux administrateurs de tirer des OTP ou des codes des messages.

#### a) Modèle fixe
Si le message a un motif fixe, vous pouvez utiliser <span data-ph="0"></span> définir le nombre de caractères pour l'extraction.

**Exemple :**

- Message : <span data-ph="0"></span> 
- Configuration & #160;: <span data-ph="0"></span> 
- Produit : <span data-ph="0"></span> 

![Extract Code - Fixed Template](images/mbn6.png)

---

#### b) Par son indice d'occurrence
Utilisez ceci lorsque les messages contiennent plusieurs codes, et vous voulez en extraire un par son index.

**Exemple :**
- Message : <span data-ph="0"></span> 
- Configuration & #160;: 
  - Longueur : <span data-ph="0"></span> 
  - Indice <span data-ph="0"></span> 
- Produit : <span data-ph="0"></span>

![Extract Code - Occurrence Index](images/mbn7.png)

---

### Rechercher et remplacer

Utilisez ceci pour remplacer des mots ou des phrases spécifiques dans le message.

**Exemple :**
- Message : <span data-ph="0"></span> 
- Configuration & #160;: 
  - Rechercher : <span data-ph="0"></span> 
  - Remplacer : <span data-ph="0"></span> 
- Produit : <span data-ph="0"></span>

![Find and Replace](images/mbn8.png)

---

### Annexe et préparation

Cela permet d'ajouter du texte personnalisé avant (prépend) ou après (annexer) le message, ou les deux.

#### a) Annexe  
Ajoute du texte **fin** du message. 
**Exemple :** 
- Message : <span data-ph="0"></span> 
- Ajouter : <span data-ph="0"></span> 
- Produit : <span data-ph="0"></span> 

![Append Example](images/mbn10.png)

---

#### b) Préparation  
Ajoute du texte **début** du message. 
**Exemple :** 
- Message : <span data-ph="0"></span> 
- Préparation: <span data-ph="0"></span> 
- Produit : <span data-ph="0"></span> 

![Prepend Example](images/mbn11.png)

---

#### c) Les deux  
Ajoute un préfixe et un suffixe. 
**Exemple :** 
- Message : <span data-ph="0"></span> 
- Préparation: <span data-ph="0"></span> 
- Ajouter : <span data-ph="0"></span> 
- Produit : <span data-ph="0"></span> 

![Append and Prepend Both](images/mbn12.png)

---

## Combiner plusieurs actions

Les administrateurs peuvent appliquer plusieurs actions en une seule règle.

**Exemple :**
- Message : <span data-ph="0"></span> 
- Actions: 
  - Code d'extraction (à partir du modèle fixe) 
  - Annexer et préparer (les deux) 

Ceci extrait le OTP et applique le formatage de texte supplémentaire tel que configuré.

![Combined Actions](images/mbn13.png)

---

## Priorité et compatibilité

- **Normalisation du corps du message** exécute **avant** des **Normalisation OA/DA**. 
- Cela garantit que le contenu du message est optimisé et formaté d'abord, en prévenant les conflits de règles. 
- Les deux règles de normalisation fonctionnent en couches pour une soumission de passerelle précise.

---

## Résumé

**Normalisation du corps du message** Dans Power SMPP, les administrateurs peuvent :
- Extraire les PAO ou codes, 
- Ajouter les préfixes/suffixes, 
- Remplacer les mots ou les phrases, 
- Combiner plusieurs règles, et 
- Appliquer les règles par utilisateur, expéditeur ou interface. 

Cette fonction permet de garantir que tous les messages respectent un format uniforme et respectent les exigences de passerelle, ce qui accroît la fiabilité et le professionnalisme dans la livraison des messages.
