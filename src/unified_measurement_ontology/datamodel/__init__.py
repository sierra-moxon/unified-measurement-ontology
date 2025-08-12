from pathlib import Path
from .unified_measurement_ontology import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "unified_measurement_ontology.yaml"
