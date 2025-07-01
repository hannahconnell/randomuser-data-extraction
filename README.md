# randomuser-data-extraction

This project was completed for the purpose of interviewing for the Jr. Data Engineer job with the Detroit Lions. 

## Installation

After pulling down the repo and navigating to the directory, you will need to create a [virtual environment](https://docs.python.org/3/library/venv.html). The following outlines the commands to do so in a Mac or Linux environment:

```bash
python3 -m venv env
```
```bash
source env/bin/activate
```
This will activate your virtual environment. From there, install the required packages:

```bash
pip install -r requirements.txt
```
You are now equipped to run my code!

## Makefile

The project contains a Makefile for your ease. There are several different ways you can use it.

### Run the entire project
Simply run the command:
```Make
Make 
```

### Run just the data gathering
Run the command:
```Make
Make data
```

### Run a particular SQL query:
Run the following, but replace # with the number of the desired query to run.

```Make
Make sql-query#
```

### Reset
To reset the project, run:
```Make
Make clean
```
## APIs used
- [https://randomuser.me/](https://randomuser.me/)
- [https://genderize.io](https://genderize.io/documentation)

## Python packages used
- [requests](https://pypi.org/project/requests/)
- [pandas](https://pandas.pydata.org/)
- [json](https://docs.python.org/3/library/json.html)
- [pandasql](https://pypi.org/project/pandasql/)

## Approach
- Gather and store 250 user objects from the RandomAPI
- From the user objects, gather a list of the names to be sent to GenderizeAPI
- Batch the names into groups of 10 before sending to Genderize
- As responses come in, add them to the gender_predictions dictionary
- Once all responses are in, convert gender_predictions to a Pandas DataFrame in order to merge it with the RandomAPI data
- Drop unnecessary columns in merged DataFrame
- Use merged DataFrame in SQL queries

## SQL Query 1
- Find the percentage of correct gender predictions across the entire dataset by comparing the actual vs. predicted gender
- Insights: Most of the time, the percentage is between 90 and 95 percent

## SQL Query 2
- Find out on average which gender has more correct gender predictions by comparing the average of correct male to correct female predictions.
- Insights: While both are often close, males do tend to be more accurate

## SQL Query 3
- Find the 5 names with the lowest probability score (where probability is the certainty of correctness in the prediction)
- Insights: As expected, uncommon and traditionally non-western names tend to have the lowest probability scores

## SQL Query 4
- Does low probability mean more data was searched before making a prediction?
- Insights: This was a tricky one, and my one query certainly did not provide the depth needed in order to provide an answer. My goal was to see if there was correlation between uncertainty in predictions and how much data the model needed to look through in order to make a prediction. For this, I calculated the average number of rows searched and the average probability, then looked at cases where the probability was lower than average, and the number of rows was higher than average. Ultimately this yielded very few rows, which means either the model is very certain in itself, my dataset is too small, or my approach needs to be refined. Likely a combination of all three.

## SQL Query 5
- Which gender is harder to predict?
- Insights: I liked the idea of using average probability as a benchmark, so I continued to do so here. For this, I looked at the number of predictions (correct or incorrect) for male and female where the probability is lower than average, to see which gender the model has less certainty with. It varies across each run, but all in all females seem to have more predictions with lower than average probabilities.

## Notes
- Due to the nature of pulling data from the RandomAPI, you may find that the outputs of the queries change from run to run. After all, they don't call it a "random user" for nothing :)
- All work in this repository is original and owned by me.
- For any questions or concerns, please contact me at [Hannah.Connell@lions.nfl.net](mailto:Hannah.Connell@lions.nfl.net) or [connellh@umich.edu](mailto:connellh@umich.edu).

