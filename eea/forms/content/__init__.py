""" EEA Forms base schema package
"""
from eea.forms.content.default import default_schema
from eea.forms.content.categorization import categorization_schema


eeaBaseSchema = categorization_schema.copy() + default_schema.copy()
