import os
import pandas as pd
rootdir = '/home/eskguptha/projects/pandas/wx_data/'
target = open('/home/eskguptha/projects/pandas/answers/MissingPrcpData.out', 'w')
for subdir, dirs, files in os.walk(rootdir):
	for file in sorted(files):
		fpath = os.path.join(subdir, file)
		fileReader = pd.read_csv(fpath, keep_default_na=False, sep='\t', header=None, error_bad_lines=False, names=["date", "maximum", "minimum", "precipitation"])
		count = fileReader[(fileReader["precipitation"] == -9999) & (fileReader["maximum"] != -9999) & (fileReader["minimum"] != -9999)]['date'].count()
		target.write(file+'\t'+str(count))
		target.write("\n")
	target.close()
		
