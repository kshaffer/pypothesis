import requests
import json

source = 'https://hypothes.is/api/search?'
conn = '&'
usercall = 'user='
tagcall = 'tags='

# adjust these variables for different searches
# also be sure to adjust the page title in the markdown() function
user = 'kris.shaffer@hypothes.is'
tags = 'IndieEdTech'
searchstring = source + usercall + user + conn + tagcall + tags
filename = 'jekyllOutput.md'

# YAML header
headerinfo = '---\n'
headerinfo += 'layout: page\n'
headerinfo += 'title: "#IndieEdTech Annotations with hypothes.is from kris.shaffer"\n'
headerinfo += 'modified: 2016-05-31 13:37:00 -0500\n' # need to make this automatic
headerinfo += 'image: \n' # this is for adding a featured image, if desired and supported by theme
headerinfo += '---\n\n'

def writeMarkdown(header, data, filename):
    f = open(filename, 'w')
    f.write(header)
    for line in data:
        f.write(str(line) + '\n')

def markdown(annotation):
    # title of post with link to original post
    textout = '['
    textout += annotation['document']['title'][0].replace('\n', '').replace('\r', '')
    textout += ']('
    textout += annotation['uri']
    textout += ')\n\n'

    # grab highlighted portion of post
    selector = annotation['target'][0]['selector']
    for entry in selector:
        if 'exact' in entry.keys():
            targetInfo = entry['exact'].replace('\n', ' ').replace('\r', ' ')
        else:
            targetInfo = 'No highlighted text found.'

    # highlighted portion of post as blockquote
    textout += '> '
    textout += targetInfo
    textout += '\n\n'

    # annotation comment, with username and link to stream
    textout += annotation['text']
    textout += ' (['
    useracct = annotation['user'].split(':')[1].split('@')[0]
    textout += useracct
    textout += ']('
    textout += 'https://hypothes.is/stream?=user:'
    textout += useracct
    textout += '))\n\n<hr/>\n'
    return textout

# run
h = requests.get(searchstring)
d = json.loads(h.text)
dataToWrite = []
i = 0
for row in d['rows']:
    dataToWrite.append(markdown(d['rows'][i]))
    i += 1
writeMarkdown(headerinfo, dataToWrite, filename)
