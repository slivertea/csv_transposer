## README
A basic tool for splitting a column in a csv to multiple columns in the row  
based on a given seperator.  This defaults to #.  Output is a longer csv.


#### input.csv
- Column 1 = Users
- Column 2 = Groups

#### output.csv
- Column 1 = Users
- Column 2+ = GroupName^n


#### Usage
 **python3 transpose.py**
 results: "output.csv"
