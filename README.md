# randomuser-data-extraction
# randomuser-data-extraction

This project was completed for the purpose of interviewing for the Jr. Data Engineer job with the Detroit Lions. 

## Installation

After pulling down the repo and navigating to the directory, you will need to create a [virtual environment](https://docs.python.org/3/library/venv.html). The following outlines the commands to do so:

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

## Notes
- Due to the nature of pulling data from the randomuser API, you may find that the outputs of the queries change from run to run. After all, they don't call it "random user" for nothing :)
- All work in this repository is original and owned by me.
- For any questions or concerns, please contact me at [Hannah.Connell@lions.nfl.net](mailto:Hannah.Connell@lions.nfl.net) or [connellh@umich.edu](mailto:connellh@umich.edu).

