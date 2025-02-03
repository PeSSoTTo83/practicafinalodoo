from odoo import models, fields, api

class Declaracion(models.Model):
    _name = 'declaracion.declaracion'
    _description = 'Modelo para declaraciones fiscales'

    codigo_modelo = fields.Selection([
        ('303', 'Modelo 303'),
        ('310', 'Modelo 310'),
    ], string='Código del Modelo', required=True)

    anio = fields.Integer(string='Año', required=True)
    trimestre = fields.Selection([
        ('1', 'Primer Trimestre'),
        ('2', 'Segundo Trimestre'),
        ('3', 'Tercer Trimestre'),
        ('4', 'Cuarto Trimestre'),
    ], string='Trimestre', required=True)

    capital_ingresado = fields.Float(string='Capital Ingresado (sin IVA)', required=True)
    capital_gastado = fields.Float(string='Capital Gastado (sin IVA)', required=True)

    diferencia = fields.Float(string='Diferencia (Ingresos - Gastos)', compute='_compute_diferencia', store=True)
    iva = fields.Float(string='IVA (21%)', compute='_compute_iva', store=True)
    importe_pagar = fields.Float(string='Importe a Pagar o Devolver', compute='_compute_importe_pagar', store=True)

    empleado_id = fields.Many2one(
        comodel_name='empleado.empleado',
        string='Empleado Responsable',
        required=True,
        help='Selecciona el empleado responsable de esta declaración.'
    )

    @api.depends('capital_ingresado', 'capital_gastado')
    def _compute_diferencia(self):
        for record in self:
            record.diferencia = record.capital_ingresado - record.capital_gastado

    @api.depends('diferencia')
    def _compute_iva(self):
        for record in self:
            record.iva = record.diferencia * 0.21

    @api.depends('diferencia', 'iva')
    def _compute_importe_pagar(self):
        for record in self:
            record.importe_pagar = record.diferencia + record.iva

