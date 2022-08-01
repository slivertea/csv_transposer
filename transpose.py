import csv

outRows=[]
# feed input of a two column csv, where:
# - column a is a list of indidivual usernames
# - column b is a list of 1 or more groups concatenated with a # delimeter

# output will concatenate column A to each found entry in column B, added as a

# requires a minimum of 1 item in column b.
input = 'input.csv'
output = 'output.csv'
# read the input

with open(input, 'r') as in_file:
    reader = csv.DictReader(in_file)

    # break out the rows
    for row in reader:
        groups = row["Groups"].split('#')

        # create a new pairing per group from the groups array (column b)
        for group in groups:
            usergroup = {}
            usergroup["Username"] = str(row["Username"])
            usergroup["Group"] = str(group)

            outRows.append(usergroup)


header = ["Username", "Group"]

with open (output, 'w') as out_file:
    writer = csv.DictWriter(out_file, fieldnames=header)
    writer.writeheader()
    for row in outRows:
        writer.writerow(row)
