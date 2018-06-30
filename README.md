# Python Scripts

This is a collection of few of the useful python scripts that I use every now and then between projects, to automate tasks and
make work easier. 

Some of these are solely by me, some have been modified from different sources. These are pretty useful to perform small 
operations to reduce workload.

Any updates are welcome!

### export_as_csv.py

This script saves all the tables in a mysql database as individual csv files. It is particularly useful for exporting data 
elsewhere, and reduces dependence on third-party applications.

It makes use of **mysql** and **pandas** libraries. 

```SHOW TABLES```
command queried with pandas gives the result in a dataframe with column named as *Tables_in_db* 
(db being the name of the database)

We iterate over the rows of this column, i.e., table names and extract all the data in a pandas dataframe. It, finally, is 
exported as .csv file.