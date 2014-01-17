""" EEA Base Schema
"""
from Products.Archetypes.Field import LinesField

from Products.Archetypes.Schema import Schema

from Products.Archetypes.Widget import InAndOutWidget

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
        vocabulary='_getMergedThemes',
        index="KeywordIndex:brains",
        enforceVocabulary=1,
        default=[],
        accessor='getThemes',
        mutator='setThemes',
    ),
))

