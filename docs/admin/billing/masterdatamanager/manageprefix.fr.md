
# Gérer le préfixe

Les **Gérer le préfixe** fonctionnalité dans iTextPRO est conçu pour gérer efficacement les préfixes de numéros mobiles associés à certains pays et opérateurs de réseau. Il joue un rôle important pour assurer une cartographie et une facturation exactes du réseau.

---

## Utiliser le cas pour gérer les préfixes

### Considérations relatives à la structure de facturation

#### Facturation par réseau (MCC-MNC)
- **Préfixe comme paramètre de cartographie** – Lorsque la facturation est basée sur le réseau (MCC-MNC), l'ajout de préfixes est crucial. Les préfixes servent de paramètres de cartographie pour identifier avec précision les modèles de facturation par réseau.
- **Précision de facturation améliorée** – La gestion du préfixe assure l'alignement du système de facturation sur les configurations réseau spécifiques liées aux codes MCC-MNC.

#### Facturation par pays
- **Aucune gestion des préfixes requise** – Pour la facturation plate et par pays, les préfixes ne sont pas nécessaires. La facturation est effectuée directement sur la base des codes de pays.
- **Processus de facturation simplifié** – Le système facture les transactions en utilisant uniquement le code de pays, en rationalisant le processus.

![Manage Prefix Overview](images/manageprefix1.png)

---

## Ajout de nouveaux préfixes

![Add Prefix](images/manageprefix2.png)

1. **Sélection du pays et de l'opérateur** – Sélectionnez le pays désiré et l'opérateur de réseau associé.
2. **Préfixe Entrée** – Coller ou saisir manuellement le préfixe (sans le code pays) dans la boîte d'entrée.
3. **Ajouter ou remplacer les options** – 
   - Sélectionner **Oui** pour ajouter le nouveau préfixe à la liste existante. 
   - Sélectionner **Numéro** remplacer entièrement la liste des préfixes existante.
4. **Présentation** – Cliquez **Soumettre** pour finaliser l'importation du préfixe.

---

## Vérifier la fonctionnalité du préfixe

![Verify Prefix](images/manageprefix3.png)

Les **Vérifier le préfixe** outil fournit des détails réseau rapides pour un numéro mobile donné.

1. **Saisissez le numéro mobile** – Saisissez le numéro que vous souhaitez vérifier.
2. **Affichage des résultats** – Le système montre:
   - Nom du pays
   - Nom du réseau
   - MCC-MNC

Cela permet de confirmer l'exactitude des détails des numéros de téléphone mobile et des informations réseau connexes.
