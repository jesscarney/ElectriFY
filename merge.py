import pandas as pd

df=pd.concat(map(pd.read_csv,[
'_results_pareto_emitlimit1.0.csv',
'_results_pareto_emitlimit0.9.csv',
'_results_pareto_emitlimit0.8.csv',
'_results_pareto_emitlimit0.7.csv',
'_results_pareto_emitlimit0.6.csv',
'_results_pareto_emitlimit0.5.csv',
'_results_pareto_emitlimit0.4.csv',
'_results_pareto_emitlimit0.3.csv',
'_results_pareto_emitlimit0.2.csv',
'_results_pareto_emitlimit0.1.csv',
'_results_pareto_emitlimit0.0.csv',]),ignore_index=True)

df.to_csv('_results_pareto_merged.csv')