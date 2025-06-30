from data_gathering import df
from pandasql import sqldf

# First query: What percentage of genders are correctly predicted?
print(sqldf(
    '''
    SELECT 
    (SUM(CASE WHEN gender_x = gender_y THEN 1 ELSE 0 END) * 100.00 / COUNT(*)) AS pct_correct 
    FROM df
    '''
    ))