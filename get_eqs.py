# Import Pandas and pull csv data into dataframe
import pandas as pd
filename='query.csv'
outfile = 'eqs.csv'

# Need to read in times which require special formatting
dateparse = lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')

# Read in dataframe
eq_df = pd.read_csv(filename, parse_dates=['time'], date_parser=dateparse)

reduced_eq = eq_df[['time', 'latitude', 'longitude', 'depth', 'mag']]
reduced_eq.to_csv(outfile, header=True, sep = ',', index=False, date_format= '%Y-%m-%dT%H:%M:%S.%f')
