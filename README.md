# Python Scripts
Some useful python scripts to automate tasks and make things easier.

### export_as_csv.py

This script saves all the tables in a mysql database as individual csv files. It is particularly useful for exporting data 
elsewhere, and reduces dependence on third-party applications.

It makes use of **mysql** and **pandas** libraries. 

```SHOW TABLES```
command queried with pandas gives the result in a dataframe with column named as *Tables_in_db* 
(db being the name of the database)

We iterate over the rows of this column, i.e., table names and extract all the data in a pandas dataframe. It, finally, is 
exported as .csv file.

### obscenity_check.py

This script checks for any obscene, profane or swear words in a document(.txt). Though, not much useful, but can come in handy to analyse text documents and mark them fit for appropriate audiences.

It makes use of **requests** library.

External resource used - http://www.wdylike.appspot.com/

### word_counter.py

This script counts the number of words and lines in a document (.txt). It is useful for keeping a track of the word limits in a document.

It does not use any external library.
