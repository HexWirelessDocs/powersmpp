
# Utilitaire – Transfert en file d'attente

Les **Transfert en file d'attente** fonctionnalité dans iTextPro permet un transfert sans faille du trafic SMS entre les passerelles, assurant une gestion efficace des opérations de messagerie. 
Cette fonctionnalité est particulièrement utile lorsque votre **passerelle primaire** expériences d'arrêt ou devient non-fonctionnel. En utilisant cette option, vous pouvez **rediriger le trafic vers une passerelle alternative**, assurant une communication ininterrompue.

![Queue-to-Queue Overview](../images/queue1.png)

---

## Configuration de transfert

### 1. Objet du transfert
Précisez l'objet ou la raison du transfert du trafic SMS. 
Cela aide à maintenir **des dossiers clairs** et fournit le contexte pour le transfert.

### 2. Passerelle source
Sélectionnez la **passerelle source** d'où les messages seront transférés. 
iTextPro vous permet de choisir **file d'attente de message spécifique** associé à cette passerelle.

### 3. Portail de destination
Choisissez le **passerelle de destination** où les messages doivent être livrés. 
Cela garantit que le trafic est redirigé vers le bon point d'arrêt opérationnel.

### 4. Ouverture du transfert
Une fois les paramètres de transfert définis:
- Cliquez sur **"Ajouter un emploi"** bouton.
- iTextPro ajoutera la tâche à la file d'attente de transfert.
- Le système transférera automatiquement les messages de la sélection **passerelle source** aux **passerelle de destination**.

Ce processus transparent garantit **continuité des services SMS** même en cas de panne de passerelle.

![Queue Transfer Execution](../images/queue2.png)
