# 📘 Guide Utilisateur — Smart Expense Auditor

## 🏁 Introduction
**Smart Expense Auditor** aide les comptables et les gestionnaires à identifier rapidement les notes de frais suspectes ou non conformes grâce à un système automatique de **notation des risques**.

---

## 🚀 Fonctionnalités Clés

### 🔢 Calcul du Score de Risque  
Chaque dépense reçoit un score de **0 à 100+**.

### 🔍 Détection d'Anomalies  
Le module détecte automatiquement plusieurs types de risques :
- Dépenses effectuées **le week-end**  
- **Montants élevés** (> 1000)  
- **Doublons potentiels**  
- Présence de **mots-clés suspects** (ex : *cadeau*, *casino*)

### 🎨 Indicateurs Visuels  
- Les lignes identifiées comme à risque apparaissent **en rouge**.

---

## 🧭 Comment Utiliser le Module

### 1️⃣ Lancer l'Audit
L'audit ne se déclenche pas automatiquement à la création (sauf configuration spécifique).  
Vous devez le lancer **manuellement** sur un ensemble de dépenses.

1. Ouvrez le menu **Notes de Frais**.  
2. Passez en **Vue Liste** (icône avec des lignes horizontales).  
3. Sélectionnez les dépenses à auditer en cochant les cases à gauche.  
4. Cliquez sur **Lancer l'Audit** (en-tête ou menu *Actions*).

---

### 2️⃣ Analyser les Résultats

Après l'exécution de l’audit, consultez la colonne **Audit Score** :

| Couleur | Score | Signification |
|--------|--------|----------------|
| 🟢 Vert | 0 | Aucun risque détecté |
| 🔴 Rouge | > 50 | Risque élevé, nécessite une vérification |
| ⚫ Noir | 1–50 | Risque modéré |

---

### 3️⃣ Comprendre le Score

Pour connaître les raisons d’un score élevé :

1. Cliquez sur la dépense concernée.  
2. Consultez le champ **Audit Notes** (Notes d’Audit) :  
   - Exemple : *"Date is on a weekend (+30)"*

---

## 📊 Barème de Notation

| Critère | Points |
|---------|--------|
| Dépense un week-end (Samedi/Dimanche) | +30 |
| Doublon (même employé / montant / date) | +50 |
| Montant élevé (> 1000) | +20 |
| Mots-clés suspects | +40 |

> 🔎 **Note :** Un score supérieur à **50** est considéré comme *suspect*.

---

