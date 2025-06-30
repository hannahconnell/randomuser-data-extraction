from data_gathering import df
from pandasql import sqldf

# Second query: On average, which gender is predicted more accurately?
print(sqldf(
    '''
    SELECT 
    AVG(CASE WHEN (gender_x = gender_y AND gender_x = 'male') THEN 1 ELSE 0 END) AS Male, 
    AVG(CASE WHEN (gender_x = gender_y AND gender_x = 'female') THEN 1 ELSE 0 END) AS Female 
    FROM df
    '''
    ))