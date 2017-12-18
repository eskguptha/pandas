import pandas as pd
input_file = "data.csv"
findings_csv = "findings.csv"
input_df = pd.read_csv(input_file)
find_df = pd.read_csv(findings_csv)
finder_list = find_df.userid.tolist()
matches_result_input_df = input_df[input_df['userid'].isin(finder_list)]
matches_result_input_df.to_csv('matches_result.csv', index=False)
matches_list = matches_result_input_df.userid.tolist()
unmatches_list_df = input_df[~input_df['userid'].isin(finder_list)]
unmatches_list_df = unmatches_list_df['userid']
unmatches_list_df.to_csv("unmatches_result.csv", index=False, header=['userid'])



