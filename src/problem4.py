import os
from decimal import Decimal
import math

# ref site http://www.statisticshowto.com/how-to-compute-pearsons-correlation-coefficients/
file  = "/home/eskguptha/projects/pandas/yld_data/US_corn_grain_yield.txt"
us_cron_data = {}
with open(file) as fin:
	 rows = ( line.split('\t') for line in fin )
	 us_cron_data = { row[0]:row[1:][0].replace('\n','') for row in rows }

grain_data = {}
file  = "/home/eskguptha/projects/pandas/answers/YearlyAverages.out"
with open(file) as fin:
	 for each in fin:
		row =  each.split('\t')
		key = row[0]+'_'+row[1]
		if key in grain_data:
			v1 = float(grain_data[key][0])+float(row[2])
			v2 = float(grain_data[key][1])+float(row[3])
			v3 = float(grain_data[key][2])+float(row[4])
			grain_data[key] = [v1,v2,v3]
		else:
			grain_data[key] = [row[2],row[3],row[4]]

process_one_data = []
for i in range(0,3):
	for each in grain_data:
		x  = float(grain_data[each][0])
		y = int(us_cron_data[each.split('_')[1]])
		process_one_data.append({
			"subject":each.split('_')[1],
			"filename":each,
			"x":x,
			"y":y,
			"xy":round((x*y),2),
			"x2":round(x*x,2),
			"y2":round(y*y,2),
			})
result = {}
no_of_entries =  len(process_one_data)
for row in process_one_data:
	r = ((no_of_entries*(row['xy']))-(row['x']*row['y']))/math.sqrt((((no_of_entries*(row['x2']))-(row['x']*row['x']))*((no_of_entries*(row['y2']))-(row['y']*row['y']))))
	if row['filename'] in result:
		result[row['filename']].append(Decimal(r))
	else:
		result[row['filename']] = [Decimal(r)]

target = open('/home/eskguptha/projects/pandas/answers/Correlations.out', 'w')
for each in sorted(result.keys()):
	target.write(each.split('_')[0]+'\t'+str(math.floor(result[each][0] * 100)/100)+'\t'+str(math.floor(result[each][1] * 100)/100)+'\t'+str(math.floor(result[each][2] * 100)/100)+'\t')
	target.write("\n")
target.close()



