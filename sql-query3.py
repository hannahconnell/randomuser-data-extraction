from data_gathering import df
from pandasql import sqldf

# Third query: What are the 5 names with the lowest probability score?
print(sqldf(
    '''
    SELECT name 
    FROM df 
    ORDER BY probability ASC 
    LIMIT 5
    '''
    ))