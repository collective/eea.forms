""" EEA Base Schema
"""

from Products.Archetypes.Schema import Schema

from datetime import datetime
from eea.forms.fields.ManagementPlanField import ManagementPlanField
from eea.forms.widgets.ManagementPlanWidget import ManagementPlanWidget


schema = Schema((

    ManagementPlanField(
        name='eeaManagementPlan',
        schemata='categorization',
        languageIndependent=True,
        required_for_published=True,
        required=False,
        default=(datetime.now().year, ''),
        validators = ('management_plan_code_validator',),
        vocabulary_factory="Temporal coverage",
        widget = ManagementPlanWidget(
            format="select",
            label="EEA Management Plan",
            description=("EEA Management plan code. Internal EEA project "
                         "line code, used to assign an EEA product output to "
                         "a specific EEA project number in the "
                         "management plan."),
            label_msgid='dataservice_label_eea_mp',
            description_msgid='dataservice_help_eea_mp',
            i18n_domain='eea.dataservice',
            )
    ),
))

