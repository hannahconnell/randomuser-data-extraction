.PHONY: all clean

all: sql-query1 sql-query2 sql-query3 sql-query4 sql-query5

data:
	python3 data_gathering.py

sql-query1: data
	python3 sql-query1.py

sql-query2: data
	python3 sql-query2.py

sql-query3: data
	python3 sql-query3.py

sql-query4: data
	python3 sql-query4.py

sql-query5: data
	python3 sql-query5.py

clean:
	rm -f *.pyc __pycache__/*
