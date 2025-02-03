{
    'name': 'Empleados',
    'version': '1.0.0',
    'summary': 'Gestión de empleados',
    'description': """
        Módulo de Odoo para gestionar empleados, incluyendo la
        información personal, departamento y salario.
    """,
    'author': 'pepico soto la lio en el ferry',
    'category': 'Human Resources',
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',  # Define permisos de acceso
        'views/empleado_views.xml',      # Define vistas para el módulo de empleados
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
