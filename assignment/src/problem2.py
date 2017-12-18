import os
import pandas as pd
rootdir = '/home/eskguptha/projects/pandas/wx_data/'
target = open('/home/eskguptha/projects/pandas/answers/YearlyAverages.out', 'w')
for subdir, dirs, files in os.walk(rootdir):
    for file in sorted(files):
        fpath = os.path.join(subdir, file)
        fileReader = pd.read_csv(fpath, keep_default_na=False, sep='\t', header=None, error_bad_lines=False, names=["date", "maximum", "minimum", "precipitation"])
        fileReader['year'] = pd.DatetimeIndex(fileReader['date'].apply(pd.to_datetime, format='%Y%m%d')).year
        max = fileReader[(fileReader["maximum"] != -9999)].groupby(['year'])['maximum'].mean()/10
        min = fileReader[(fileReader["minimum"] != -9999)].groupby(['year'])['minimum'].mean()/10
        per = fileReader[(fileReader["precipitation"] != -9999)].groupby(['year'])['precipitation'].sum()/100
        avg_max = max.round(2)
        avg_min = min.round(2)
        avg_per = per.round(2)
        df = fileReader.set_index(['year'])
        df = pd.concat([avg_max,avg_min, avg_per], axis=1, join='inner')
        df['year'] = df.index
        for each in df.iterrows():
            target.write(file+'\t'+str(int(each[1]['year']))+'\t'+str(each[1]['maximum'])+'\t'+str(each[1]['minimum'])+'\t'+str(each[1]['precipitation']))
            target.write("\n")
    target.close()
