import os

import csv

csvpath = os.path.join("Resources", "election_data.csv")
csvpath_out = os.path.join("Resources", "election_data.txt")

#creating lists
voting_percentage = []
voting_count = []
count_total = 0
candidates = []
candidates_unique = []

#reading the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
#assigning the candidates to the proper row, append method which adds item to the end of list
    for row in csvreader:
        count_total = count_total + 1
        candidates.append(row[2])
#gathering individual candidate names
    for x in set(candidates):
        candidates_unique.append(x)
        z = candidates.count(x)
        voting_count.append(z)
        voting_percentage.append(z/ count_total)

    Winner = candidates_unique[voting_count.index(max(voting_count))]

#if you uncomment line 37 and 38, you can see i get the correct candidate answers. 
#unfortunately, i do not know how to add the for i loop in txt


    #for i in range(len(set(candidates_unique))):
        #print(f'{candidates_unique[i]}  : {str(round(voting_percentage[i]*100,1))} % {str(voting_count[i])}')

with open ('election_data_results.txt', 'w') as text:
    text.write('Election Results\n')
    text.write('----------------------')
    text.write('Total Votes: ' + str(count_total) + '\n')
    text.write('-------------------------\n')
    #for i in range(len(set(candidates_unique))):
        #text.write('{candidates_unique[i]}  : {str(round(voting_percentage[i]*100,1))} % {str(voting_count[i])}')
    text.write('-------------------------\n')
    text.write('Winner!: ' + Winner + '\n')
    text.write('-------------------------\n')



#the results, output
#output = (f'Election Results\n'
         #f'-------------------------\n'
         #f'Total Votes: ' + str(count_total) + '\n'
         #f'-------------------------\n'
         #f'-------------------------\n'
         #f'Winner!: ' + Winner + '\n'
         #f'-------------------------\n')

# print(output)

#with open(csvpath_out, "w") as text_file:
     #text_file.write(output)
     #for i in range(len(set(candidates_unique))):
        #print(f'{candidates_unique[i]}  : {str(round(voting_percentage[i]*100,1))} % {str(voting_count[i])}')
     #text_file.close()

