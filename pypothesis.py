# A Python module for more simply interacting with the hypothes.is API.

import requests
import json

class Annotation():

    def __init__(self, jsondata):
        self.jsondata = jsondata

        # title of annotated article
        self.title = self.jsondata['document']['title'][0].replace('\n', '').replace('\r', '')

        # uri of annotated article
        self.uri = self.jsondata['uri']

        # highlighted text in annotated article
        if 'selector' in self.jsondata['target'][0].keys():
            selector = self.jsondata['target'][0]['selector']
            for entry in selector:
                if 'exact' in entry.keys():
                    self.highlight = entry['exact'].replace('\n', ' ').replace('\r', ' ')
                else:
                    self.highlight = 'No highlighted text found.'
        else:
            self.highlight = 'No highlighted text found.'

        # annotation comment
        if self.jsondata['text']:
            self.comment = self.jsondata['text']
        else:
            self.comment = 'No comment found.'

        # user that generated the annotation
        self.user = self.jsondata['user'].split(':')[1].split('@')[0]

        # date/time created and updated
        self.created = self.jsondata['created']
        self.updated = self.jsondata['updated']

        # hypothesis ID & annotation URL
        self.id = self.jsondata['id']
        self.hypothesisurl = 'https://hyp.is/' + self.jsondata['id']

def retrieve(apiurl):
    # takes the hypothes.is API URL for an annotation and returns JSON data
    h = requests.get(apiurl)
    d = json.loads(h.text)
    return d

def apiurl(hypurl):
    # takes the hyp.is URL provided in an annotation and returns the API URL (for use elsewhere in this module)
    hypid = hypurl.split('.is/')[1].split('/')[0]
    url = 'https://hypothes.is/api/annotations/' + hypid
    return url

def searchurl(user = '', tag = '', tags = []):
    """
    Returns a well-formed URL for querying the hypothes.is API.
    A hypothes.is username is optional.
    Use *either* tag or tags, not both. You can also use neither if a username is provided.
    Use tag for a single tag, and put the tag in quotes.
    Use tags for multiple tags, and enclose them in a list: ['tag1', 'tag2', 'tag3'].
    searchurl() only works if at least once term (user, tag, or tags) is provided.
    """

    source = 'https://hypothes.is/api/search?'
    conn = '&'
    usercall = 'user='
    tagcall = 'tags='
    if tags == []:
        if user != '' and tag != '':
            return source + usercall + user + conn + tagcall + tag
        if user == '' and tag != '':
            return source + tagcall + tag
        if user != '' and tag == '':
            return source + usercall + user
        if user == '' and tag == '':
            print('No search parameters included.')
    if tags != []:
        if user != '':
            sourcestring = source + usercall + user
            for entry in tags:
                sourcestring += (conn + tagcall + entry)
            return sourcestring
        if user == '':
            sourcestring = source + tagcall + tags.pop(0)
            while tags != []:
                sourcestring += (conn + tagcall + tags.pop(0))
            return sourcestring

# test

"""
s = searchurl('kris.shaffer@hypothes.is', tags = ['#IndieEdTech', 'writing'])
print(s)
"""

"""
# using the hyothes.is annotation share URL, retrieve and parse the JSON data
t = Annotation(retrieve(apiurl('https://hyp.is/AVOP5R06H9ZO4OKSlTrY/hackeducation.com/2016/03/18/i-love-my-label')))
print(t.title)
print(t.uri)
print(t.highlight)
print(t.comment)
print(t.user)
print(t.created)
print(t.updated)
print(t.id)
print(t.hypothesisurl)
"""
