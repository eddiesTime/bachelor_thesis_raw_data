import os, glob, json
folder_path = '/Users/eddie/Development/state management evaluation/collected data/performance metric/states rebuilder'

result = []
for filename in glob.glob(os.path.join(folder_path, '*_summary.json')):
    with open(filename, 'r') as infile:
        result.append(json.load(infile))

with open('merged_file.json', 'wb') as outfile:
    json.dump(result, outfile)