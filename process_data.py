import pandas as pd
import numpy as np
import utils

data = pd.read_excel(utils.extracted_filename)

## Data validation
### Check critical columns
data_check = data.loc[:,['Address','SoldDate', 'RedfinSoldDate', 'Tag_SoldDate','Date1', 'Date2', 'Date3']]
print(utils.status(data_check))