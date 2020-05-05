import pandas
import matplotlib.pyplot as plt
import json
import sys
import os

pandas.set_option("display.max_rows", 200)

with open(sys.argv[1]) as f:
    config = json.load(f)

for chart in config['charts']:
    plot_df = None

    for line in chart['lines']:
        d = line['directory']
        sum_df = None
        dirs = os.listdir(d)
        title = line['title']

        for fn in dirs:
            df = pandas.read_csv(
                os.path.join(d, fn),
                delimiter=r'\s+',
                names=['type', title, 'timestamp']
            )
            df = df[df['type'] == line['type']]
            df = df[['timestamp', title]]
            df = df.sort_values('timestamp', ignore_index=True)
            df['timestamp'] -= df['timestamp'][0]
            if sum_df is None:
                sum_df = df
            else:
                sum_df[title] += df[title]

        sum_df[title] = sum_df[title] / len(dirs)

        if plot_df is None:
            plot_df = sum_df
        else:
            plot_df = plot_df.merge(sum_df, on='timestamp', how='outer')
    
    plot_df.set_index('timestamp', inplace=True)
    plot_df.interpolate(inplace=True)
    axis = plot_df.plot.line(title=chart['title'])
    axis.set_xlabel(chart['xlabel'])
    axis.set_ylabel(chart['ylabel'])
    if 'ybottom' in chart:
        axis.set_ylim(bottom=chart['ybottom'])
    if 'ytop' in chart:
        axis.set_ylim(top=chart['ytop'])

for barchart in config['barcharts']:
    columns = {}
    for dataset in barchart['sets']:
        columns[dataset['name']] = dataset['data']

    df = pandas.DataFrame(columns, index=barchart['index'])
    df.plot.bar(title=barchart['title'], rot=0)

plt.show()