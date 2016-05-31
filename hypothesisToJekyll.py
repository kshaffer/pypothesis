import requests
import json

source = 'https://hypothes.is/api/search?'
conn = '&'
usercall = 'user='
tagcall = 'tags='
user = 'kris.shaffer@hypothes.is'
tags = 'IndieEdTech'
filename = 'jekyllOutput.md'

def writeMarkdown(data, filename):
    f = open(filename, 'w')
    for line in data:
        f.write(str(line) + '\n')

# run

searchstring = source + usercall + user + conn + tagcall + tags

h = requests.get(searchstring)
d = json.loads(h.text)

dataToWrite = []
i = 0
for row in d['rows']:
    dataToWrite.append('User:' + ' ' + d['rows'][i]['user'].split(':')[1])
    dataToWrite.append('Title:' + ' ' + d['rows'][i]['document']['title'][0].replace('\n', '').replace('\r', ''))
    selector = d['rows'][i]['target'][0]['selector']
    for entry in selector:
        if 'exact' in entry.keys():
            targetInfo = entry['exact'].replace('\n', ' ').replace('\r', ' ')
        else:
            targetInfo = 'no highlighted text found'
    dataToWrite.append('Highlighted text:' + ' ' + targetInfo)
    dataToWrite.append('URI:' + ' ' + d['rows'][i]['uri'])
    dataToWrite.append('')
    i += 1

writeMarkdown(dataToWrite, filename)
