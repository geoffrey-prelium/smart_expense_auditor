{
    'name': 'Smart Expense Auditor',
    'author': 'Geoffrey Lecluse (Prelium)',
    'version': '1.0',
    'category': 'Human Resources/Expenses',
    'summary': 'Automated audit and risk scoring for employee expenses',
    'description': """
        This module extends the HR Expense module to automatically audit expenses.
        It calculates a 'Risk Score' based on:
        - Weekend dates
        - Duplicate expenses
        - High amounts
        - Suspicious keywords
    """,
    'depends': ['hr_expense'],
    'data': [
        'security/ir.model.access.csv',
        'views/expense_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
