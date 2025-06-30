from data_gathering import df
from pandasql import sqldf

# Fifth query: Which gender is harder to predict?
# For this query, "harder" is defined as predictions where the probability of correctness is lower than average
print(sqldf(
    '''
    WITH avgs AS 
        (SELECT 
        AVG(probability) AS avg_probability 
        FROM df) 
    SELECT 
    SUM(CASE WHEN(gender_x = 'male') THEN 1 ELSE 0 END) AS Male, 
    SUM(CASE WHEN(gender_x = 'female') THEN 1 ELSE 0 END) AS Female 
    FROM df, avgs 
    WHERE df.probability < avgs.avg_probability
    '''
    ))