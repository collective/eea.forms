""" EEA Base Schema
"""
from Products.Archetypes.Field import LinesField

from Products.Archetypes.Schema import Schema

from Products.Archetypes.Widget import InAndOutWidget, MultiSelectionWidget

try:
    from eea.themecentre.content.ThemeTaggable import ThemesField
except ImportError:
    class ThemesField(LinesField):
        """ Archetypes default LinesField
        """
        pass

categorization_schema = Schema((
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
        vocabulary_factory=u"Allowed themes for edit",
        default=[],
        accessor='getThemes',
        mutator='setThemes',
    ),

    LinesField(name='temporalCoverage',
               languageIndependent=True,
               schemata='categorization',
               required=False,
               multiValued=1,
               vocabulary_factory=u"Temporal coverage",
               widget=MultiSelectionWidget(
                   macro="temporal_widget",
                   helper_js=("temporal_widget.js",),
                   size=15,
                   label="Temporal coverage",
                   description=("The temporal scope of the content of the data "
                                "resource. Temporal coverage will typically "
                                "include a set of years or time ranges."),
                   label_msgid='dataservice_label_coverage',
                   description_msgid='dataservice_help_coverage',
                   i18n_domain='eea',
               )
    )
))

