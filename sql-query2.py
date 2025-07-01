from data_gathering import df
from pandasql import sqldf

# Second query: On average, which gender is predicted more accurately?
print(sqldf(
    '''
    WITH male AS (
      SELECT COUNT(*) AS male_count FROM df WHERE gender_x = 'male'
    ),
    female AS (
      SELECT COUNT(*) AS female_count FROM df WHERE gender_x = 'female'
    )
    SELECT 
    SUM(CASE WHEN (gender_x = gender_y AND gender_x = 'male') THEN 1 ELSE 0 END) * 100.0 / male.male_count AS correct_male, 
    SUM(CASE WHEN (gender_x = gender_y AND gender_x = 'female') THEN 1 ELSE 0 END) * 100.0 / female.female_count AS correct_female
    FROM df, male, female
    GROUP BY male.male_count, female.female_count
    '''
    ))
