# 🛠️ Guide Développeur — Smart Expense Auditor

Ce guide explique l'architecture technique du module et comment étendre ou modifier les règles de détection d'anomalies.

## 📂 Structure du Module

- **`models/expense.py`** : Contient la logique métier et l'algorithme de scoring.
- **`views/expense_views.xml`** : Définit les modifications de l'interface (colonnes, boutons, couleurs).

## 🧠 Logique de Scoring

La méthode principale est `_compute_audit_score()` dans le modèle `hr.expense`.
Elle parcourt chaque dépense et accumule des points dans la variable `score` tout en ajoutant des explications dans `notes`.

### Algorithme Actuel
1. **Week-end** : Vérifie `date.weekday() >= 5`. (+30 pts)
2. **Doublons** : Cherche des dépenses similaires (même employé, montant, +/- 2 jours). (+50 pts)
3. **Montant** : Vérifie si `total_amount > 1000`. (+20 pts)
4. **Mots-clés** : Scanne la description pour `["gift", "cadeau", "personal", "perso", "casino"]`. (+40 pts)

## 🔧 Comment Personnaliser les Anomalies

Pour ajouter ou modifier des règles, vous devez hériter du modèle `hr.expense` et surcharger la méthode `_compute_audit_score`.

### Exemple : Ajouter une règle "Dépense de nuit"

Créez un nouveau module ou ajoutez ce code dans votre extension :

```python
from odoo import models

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    def _compute_audit_score(self):
        # 1. Exécuter la logique existante (super)
        super()._compute_audit_score()

        # 2. Ajouter votre propre logique
        for expense in self:
            current_score = expense.audit_score
            current_notes = expense.audit_notes or ""
            
            # Exemple : Pénaliser les dépenses sans reçu joint
            if expense.nb_attachment == 0:
                current_score += 15
                current_notes += "\nPas de reçu joint (+15)"
            
            # Mettre à jour les champs
            expense.write({
                'audit_score': current_score,
                'audit_notes': current_notes
            })
```

### Modifier les seuils existants

Si vous souhaitez modifier les seuils (ex: changer la limite de 1000€ à 500€), il est préférable de **remplacer** la méthode ou de rendre les seuils configurables via `res.config.settings` (nécessite un développement supplémentaire pour stocker les paramètres).

Pour un remplacement rapide, surchargez la méthode sans appeler `super()` (déconseillé si vous voulez garder les autres règles) ou copiez-collez la logique en l'adaptant.

## ⚠️ Bonnes Pratiques

- **Performance** : Évitez les requêtes lourdes (comme `search_count` complexes) à l'intérieur de boucles si vous traitez des milliers de dépenses.
- **Idempotence** : La méthode doit pouvoir être relancée plusieurs fois sans dupliquer les notes (le code actuel réinitialise `score` et `notes` au début de la fonction, ce qui est correct).
