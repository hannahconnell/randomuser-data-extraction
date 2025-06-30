from data_gathering import df
from pandasql import sqldf

# Fourth query: How many instances are there where the probability is lower than average, and the number of rows searched is higher than average?
print(sqldf(
    '''
    WITH avgs AS 
        (SELECT 
        AVG(probability) AS avg_probability, 
        AVG(count) AS avg_rows 
        FROM df) 
    SELECT 
    DISTINCT df.name, 
    df.probability, 
    df.count 
    FROM df, avgs 
    WHERE df.probability < avgs.avg_probability AND df.count > avgs.avg_rows
    '''
))