import pandas
import matplotlib.pyplot as plt
import json
import sys
import os

with open(sys.argv[1]) as f:
  config = json.load(f)

for chart in config['charts']:
    line_dfs = []
    for line in chart['lines']:
        d = line['directory']
        sum_df = None
        dirs = os.listdir(d)
        for fn in dirs:
            df = pandas.read_csv(
                os.path.join(d, fn),
                delimiter=r'\s+',
                names=['type', 'value', 'timestamp']
            )
            df = df[df['type'] == line['type']]
            df['type'] = line['title']
            df = df.sort_values('timestamp', ignore_index=True)
            df['timestamp'] -= df['timestamp'][0]
            if sum_df is None:
                sum_df = df
            else:
                sum_df['value'] += df['value']
        sum_df['value'] = sum_df['value'] / len(dirs)
        line_dfs.append(sum_df)
    plot_df = pandas.concat(line_dfs)
    print(plot_df)
    plot_df = plot_df.pivot(index='timestamp', columns='type', values='value')
    plot_df.plot()
    plt.show()