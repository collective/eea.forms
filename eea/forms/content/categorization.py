""" EEA Base Schema
"""
from Products.Archetypes.Field import LinesField

from Products.Archetypes.Schema import Schema

from datetime import datetime
from Products.Archetypes.Widget import InAndOutWidget
from eea.forms.fields.ManagementPlanField import ManagementPlanField
from eea.forms.widgets.ManagementPlanWidget import ManagementPlanWidget

try:
    from eea.themecentre.content.ThemeTaggable import ThemesField
except ImportError:
    class ThemesField(LinesField):
        """ Archetypes default LinesField
        """
        pass

categorization_schema = Schema((

    ManagementPlanField(
        name='eeaManagementPlan',
        schemata='categorization',
        languageIndependent=True,
        required_for_published=True,
        required=False,
        default=(datetime.now().year, ''),
        validators=('management_plan_code_validator',),
        vocabulary_factory="Temporal coverage",
        widget=ManagementPlanWidget(
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

    ThemesField(
        name='themes',
        schemata='categorization',
        validators=('maxValues',),
        widget=InAndOutWidget(
            maxValues=3,
            label="Themes",
            description="Choose max 3 themes",
            label_msgid='EEAContentTypes_label_themes',
            description_msgid='EEAContentTypes_help_themes',
            i18n_domain='EEAContentTypes',
        ),
        languageIndependent=True,
        vocabulary='_getMergedThemes',
        index="KeywordIndex:brains",
        enforceVocabulary=1,
        default=[],
        accessor='getThemes',
        mutator='setThemes',
    ),
))

