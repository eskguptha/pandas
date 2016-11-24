import os
import pandas as pd

target = open('/home/ubuntu/Desktop/Assign/coding-data-exam/answers/YearHistogram.out', 'w')
fileReader = pd.read_csv('/home/ubuntu/Desktop/Assign/coding-data-exam/answers/YearlyAverages.out', keep_default_na=False, sep='\t', header=None, error_bad_lines=False, names=["filename", "year", "maximum", "minimum",  "precipitation"])
max_dict = {}
min_dict = {}
per_dict = {}
maxi = fileReader.groupby(['filename'], sort=False)['maximum'].transform(max) == fileReader['maximum']
df = fileReader[maxi].groupby('year').count()['maximum']
for each in df.iteritems():
    max_dict[each[0]] = each[1].item()

mini = fileReader.groupby(['filename'], sort=False)['minimum'].transform(max) == fileReader['minimum']
df = fileReader[mini].groupby('year').count()['minimum']
for each in df.iteritems():
    min_dict[each[0]] = each[1].item()

per = fileReader.groupby(['filename'], sort=False)['precipitation'].transform(max) == fileReader['precipitation']
df = fileReader[per].groupby('year').count()['precipitation']
for each in df.iteritems():
    per_dict[each[0]] = each[1].item()

for each_year, value in max_dict.items():
    target.write(str(each_year.item())+'\t'+str(value)+'\t'+str(min_dict.get(each_year,0))+'\t'+str(per_dict.get(each_year,0)))
    target.write("\n")
target.close()



