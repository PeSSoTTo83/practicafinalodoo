
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Empleado(models.Model):
    _name = 'empleado.empleado'
    _description = 'Gestión de Empleados'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    departamento = fields.Selection([
        ('administracion', 'Administración'),
        ('ventas', 'Ventas'),
        ('it', 'Tecnología de la Información'),
        ('rrhh', 'Recursos Humanos'),
    ], string='Departamento', required=True)
    salario = fields.Float(string='Salario', required=True)

    @api.constrains('salario')
    def _check_salario(self):
        for record in self:
            if record.salario < 0:
                raise ValidationError('El salario no puede ser negativo.')
