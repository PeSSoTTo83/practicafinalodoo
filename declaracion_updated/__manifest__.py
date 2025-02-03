{
    'name': 'Declaración',
    'version': '1.0.0',
    'summary': 'Gestión de declaraciones fiscales',
    'description': """
        Módulo de Odoo para gestionar declaraciones fiscales,
        incluyendo la introducción de datos de capital ingresado, gastado,
        y cálculos automáticos como el IVA y el importe a pagar.
    """,
    'author': 'jose y pepe la lian en el ferry',
    
    'category': 'Accounting',
    'license': 'AGPL-3',
    
    'depends': [
        'base',  # Dependencia básica de Odoo
        'empleados_module',  # Reemplaza 'empleado_module' por el nombre técnico del módulo de empleados
    ],
    
    'data': [
        'security/ir.model.access.csv',  # Define permisos de acceso
        'views/declaracion_views.xml',   # Define vistas para el módulo de declaraciones
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}

