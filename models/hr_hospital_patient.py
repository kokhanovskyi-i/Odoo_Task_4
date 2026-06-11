import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):
    _name = "hr.hospital.patient"
    _description = "Hospital patient"
    _inherit = ["hospital.medic.info"]

    name = fields.Char(
        string="Name",
        required=True,
    )

    email = fields.Char(
        string="Email",
    )

    phone = fields.Char(
        string="Phone",
    )

    personal_doctor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        string="Personal Doctor",
    )

    doctor_history_ids = fields.One2many(
        comodel_name="hospital.doctor.history",
        inverse_name="patient_id",
        string="Personal Doctor History",
    )

    insurance_policy_number = fields.Char(
        string="Insurance Policy Number",
        size=20,
    )