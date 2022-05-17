import logging
import csv
from pathlib import Path
from typing import Any,Dict, List, Tuple

JsonDict = Dict[str, Any]
logger = logging.getLogger(__name__)

class CsvData():
    """ Class for csv data, loads the csv file and path. If path is not provide it will
    load from '.data/data.csv' file. If a Path is provided it loads from th path
    """
    def __init__(self, path=None) -> None:
        self.result = []
        if path == None:
            try:
                self.csvFile = open('./data/data.csv', newline='')
            except Exception as err:
                print(f"Can't open the data csv file. Error : {err}")
        else:
            if Path(path).exists():
                try:
                    self.csvFile = open(Path(path))
                except Exception as err:
                    print(f"Cannot open file at {path} with error : {err}")
            else:
                print(f" Path {path} doesn't exists. Please verify")
        
    def filter_by_col(self, column:str, filter_value:str) -> List[Dict]:
        """ filter the data with column and value provided"""

        print("*"*88)
        print(f" Search with \
            column = \"{column}\", \
            filter_value = \"{filter_value}\"")
        print("*"*88)
        with self.csvFile:
            data = csv.DictReader(self.csvFile)
            for row in data:
                if row[f"{column}"] == filter_value:
                    self.result.append(row)

        return self.result

    
    def filter_city_state(self, city:str, state:str) -> List[Dict]:
        """ filter csv data with city and state. Value are provided from command line
            @param city : name of the city to filter data
            @param state : name of the state to filter data
        """
        city_col = "City"
        state_col = "State"
        with self.csvFile:
            data = csv.DictReader(self.csvFile)
            for row in data:
                if row[city_col] == city \
                        and row[state_col] == state:
                    self.result.append(row)
        
        return self.result

        

