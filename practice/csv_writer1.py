import csv
 
data = [[1, 'foo'], [2, 'bar'], [3, 'hoge']]
 
f = open('write1.csv', 'w')
writer = csv.writer(f)
writer.writerows(data)
f.close()