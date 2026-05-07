
# Configuration du télévendeur

Avec l'introduction de **RÉGLEMENTATION DE LA DLT TRAI**, le trafic SMS en Inde doit suivre un obligatoire **Chaîne PE-TM** (Chaîne principale d'entités-commerçants). Cette chaîne assure la traçabilité et la conformité réglementaire de tous les intervenants impliqués dans la livraison des messages, y compris la **Utilisateur, revendeur, application et fournisseur**.

Pour se conformer à ce règlement, l'application doit être configurée pour : **annexer les renseignements requis du télévendeur** avant de soumettre des messages au fournisseur en amont ou SMSC.

---

## Logique de formation de chaîne PE-TM

La chaîne PE-TM est construite dynamiquement lors de la soumission de messages **type de fournisseur**.

### Flux de messages

1. Les **utilisateur** soumet le message avec leur **Numéro d'identification de l'entité principale**.
2. Les **demande** ajoute sa configuration **ID de télévendeur (TMID)**.
3. La structure finale de la chaîne dépend du type de fournisseur.

---

## Types de fournisseurs et formation de chaînes

=== « Agrégateur »

 Une **Agrégateur** est un fournisseur intermédiaire qui transmet le message à un autre fournisseur ou SMSC.

    - La demande ajoute **TMID**
    - L'agrégateur ajoute sa propre **TMID2**
    - Le message est ensuite transmis au prochain saut

 **Formation de la chaîne:** <span data-ph="0"></span>

    !!! info
 Hashing est **non requis** au niveau de l'application pour les fournisseurs Agrégator.

=== "Partenaire de livraison"

 A **Partenaire de livraison** est le SMSC final chargé de transmettre le message au combiné.

    - La demande ajoute **TMID**
    - La chaîne finale doit être **déchiqueté** avant la soumission

 **Formation de la chaîne:** <span data-ph="0"></span>

    !!! info
 Le hachage assure le respect des exigences de sécurité et d'intégrité de TRAI.

---

## Configuration du télévendeur dans l'application

**Voie de navigation :** <span data-ph="0"></span>

![Telemarketer Configuration List](images/telemarketer1.png)

---

## Étapes de configuration

1. Cliquez sur **Ajouter un nouveau**
2. Sélectionnez la **Nom de la passerelle**
3. Saisissez la **ID de télévendeur (TMID)**
4. Configurer le hachage en fonction du type de fournisseur :
    - **Agrégateur:** Jeu **Hashing Active = OFF**
    - **Partenaire de livraison:** Jeu **Hashing Active = ON**
5. **Type de fuite:**
    - Par défaut à **SHA-256** (recommandé et conforme aux MARI)
6. Cliquez sur **Enregistrer** pour appliquer la configuration

![Telemarketer Configuration Dialog](images/telemarketer2.png)

---

!!! danger "Remarques importantes"
    - Une configuration de hachage incorrecte peut entraîner **Rejet de la DLT** par le fournisseur ou SMSC.
    - Assurez-vous que le type de fournisseur (Agrégateur vs partenaire de livraison) est confirmé avant la configuration.
    - SHA-256 est appliqué comme algorithme de hachage par défaut pour répondre aux normes réglementaires.
