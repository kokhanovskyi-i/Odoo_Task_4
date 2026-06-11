import logging

from odoo import api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrHospitalDoctor(models.Model):
    _name = "hr.hospital.doctor"
    _description = "Hospital doctor"
    _inherit = ["hospital.medic.info"]

    name = fields.Char(
        string="Name",
        required=True,
    )

    specialty = fields.Char(
        string="Specialty",
        required=True,
    )

    category_id = fields.Many2one(
        comodel_name="hospital.doctor.category",
        string="Category",
    )

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="System User",
    )

    is_intern = fields.Boolean(
        string="Doctor Is Intern",
        compute="_compute_is_intern",
        store=True,
    )

    mentor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        string="Mentor",
        domain=[("is_intern", "=", False)],
    )

    email = fields.Char(
        string="Email",
        required=True,
    )

    phone = fields.Char(
        string="Phone",
        required=True,
    )

    @api.depends("category_id")
    def _compute_is_intern(self):
        intern_category = self.env.ref(
            "hr_hospital.doctor_category_intern",
            raise_if_not_found=False,
        )

        for doctor in self:
            doctor.is_intern = bool(
                doctor.category_id
                and intern_category
                and doctor.category_id == intern_category
            )

    @api.constrains("mentor_id")
    def _check_mentor_is_not_intern(self):
        for doctor in self:
            if doctor.mentor_id and doctor.mentor_id.is_intern:
                raise ValidationError("Mentor cannot be an intern.")