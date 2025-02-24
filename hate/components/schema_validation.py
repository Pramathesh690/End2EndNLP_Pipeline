from hate.constants import RAW_FILE_SCHEMA , IMBALANCE_SCHEMA
from dataclasses import dataclass
import numpy as np

@dataclass
class validate_schema:
    def __init__(self , rf_columns , id_columns ):
        self.rf_columns = rf_columns
        self.id_columns = id_columns
        
    @dataclass
    def validateschema(self , rf_columns , id_columns ) -> bool:
        if np.array_equal(rf_columns , id_columns):
            return True
        else:
            return False

    

