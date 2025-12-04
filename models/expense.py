from odoo import models, fields, api
from datetime import timedelta

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    audit_score = fields.Integer(string='Audit Score', readonly=True, default=0)
    audit_notes = fields.Text(string='Audit Notes', readonly=True)
    is_suspicious = fields.Boolean(string='Is Suspicious', compute='_compute_is_suspicious', store=True)

    @api.depends('audit_score')
    def _compute_is_suspicious(self):
        for expense in self:
            expense.is_suspicious = expense.audit_score > 50

    def action_audit_expenses(self):
        for expense in self:
            expense._compute_audit_score()

    def _compute_audit_score(self):
        for expense in self:
            score = 0
            notes = []

            # 1. Weekend Check
            if expense.date and expense.date.weekday() >= 5:
                score += 30
                notes.append('Date is on a weekend (+30)')

            # 2. Duplicate Check
            if expense.employee_id and expense.total_amount:
                date_from = expense.date - timedelta(days=2)
                date_to = expense.date + timedelta(days=2)
                domain = [
                    ('id', '!=', expense.id),
                    ('employee_id', '=', expense.employee_id.id),
                    ('total_amount', '=', expense.total_amount),
                    ('date', '>=', date_from),
                    ('date', '<=', date_to),
                ]
                duplicates = self.search_count(domain)
                if duplicates > 0:
                    score += 50
                    notes.append('Potential duplicate found (+50)')

            # 3. High Amount Check
            if expense.total_amount > 1000:
                score += 20
                notes.append('Amount > 1000 (+20)')

            # 4. Suspicious Keywords Check
            suspicious_keywords = ["gift", "cadeau", "personal", "perso", "casino"]
            if expense.description:
                found_keywords = [word for word in suspicious_keywords if word in expense.description.lower()]
                if found_keywords:
                    score += 40
                    notes.append(f'Suspicious keywords found: {", ".join(found_keywords)} (+40)')

            expense.write({
                'audit_score': score,
                'audit_notes': '\n'.join(notes)
            })
