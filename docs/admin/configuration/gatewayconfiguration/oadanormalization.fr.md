
## Règles de normalisation OA/DA dans iTextPRO

![OA/DA Normalization](images/oada1.png)

**OA (Adresse de l'initiateur)** et **DA (Adresse de destination)** La normalisation dans iTextPRO permet le contenu des messages, l'expéditeur (source) et les adresses des destinataires de **Mobile Terminé (MT)** les messages à régler automatiquement selon des règles prédéfinies.

Cette fonctionnalité est cruciale lorsque vous travaillez avec différents fournisseurs ou passerelles de télécommunications qui peuvent suivre différents protocoles ou exigences de formatage.

---

### 1. Objet
Normaliser **initiateur (OA)** et **destination (DA)** adresses à:
- Rencontre **directives réglementaires**
- Réalisation **exigences spécifiques de formatage des entreprises ou des fournisseurs**

---

### 2. Moteur iTextPRO OA/DA
iTextPRO comprend un intégré **Moteur de normalisation OA/DA** qui fonctionne à côté du moteur de routage. 
Il permet de modifier **PDU (unité de données protocolaires)** en-têtes pour la livraison et la conformité des messages.

---

### 3. Exemple du monde réel

#### Message original envoyé :
- **ID de l'expéditeur**: <span data-ph="0"></span> 
- **Message**: 
 <span data-ph="0"></span>

#### Message après la règle OA/DA appliquée :
- **ID de l'expéditeur**: <span data-ph="0"></span> 
- **Message modifié**: 
 <span data-ph="0"></span>

Cette transformation est automatiquement gérée par les règles de normalisation OA/DA définies dans iTextPRO.

---

### 4. Note sur les caractères Unicode

- Pour **Unicode** messages: Limite maximale de caractères = **70 caractères**
- Pour **Anglais (GSM)** messages: Limite maximale de caractères = **160 caractères**

Si un message dépasse ces limites, le système **parures automatiques** les caractères supplémentaires à conserver dans les contraintes de codage SMS.

---

### 5. Étapes de mise en œuvre

Pour appliquer la normalisation OA/DA :

1. **Créer de nouvelles règles OA/DA** dans le panneau de configuration.
2. Définir la logique de transformation :
   - Modifier l'identifiant de l'expéditeur
   - Réécrire le contenu du message
   - Modifier le formatage du numéro de destination
3. Attribuer les règles aux passerelles ou sources de trafic pertinentes.

---

### 6. Principaux avantages

- Interopérabilité des fournisseurs sans soudure
- Conformité aux normes de télécommunication ou de réglementation
- • Sanitisation ou réécriture automatique du contenu
- Personnalisation de l'identifiant de l'expéditeur et du contenu de messagerie

---

**Normalisation OA/DA** dans iTextPRO offre un mécanisme puissant pour le formatage et la conformité des messages, permettant le routage des messages à la fois techniquement robuste et réglementaire.
