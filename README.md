# pypothesis

Python scripts for interacting with the [hypothes.is](https://hypothes.is/) API.

## hypothesisToJekyll.py

This script (still in progress) calls the hypothes.is API, searches for public annotations from a specific user with a specific hashtag, and writes the results to a markdown file that is Jekyll-friendly.

Simply open the script, change the variables at the top of the file to suit your needs, and run it. There are comments in the script to help you. Then place the 'jekyllOutput.md' file it creates into your Jekyll/GitHub blog. (I'd change the name.) Finally, add a link to the page.

You can see this script in action on my website: [http://kris.shaffermusic.com/hypothesis/](http://kris.shaffermusic.com/hypothesis/).

The downside to this script, which results from the way GitHub Pages works, is that you have to run it manually each time you want to fetch new annotations. To enhance that process, you could add the appropriate path to the output file name in this script, and write a shell script that runs this script and then commits/pushes to GitHub, and then schedule that script to run at regular intervals from your computer/server. I'm going to look into adding that functionality to this script, but it's not ready yet.

Enjoy!

## pypothesis.py

The beginnings of a Python module that will allow programmers a simpler interface for the hypothes.is API. See test (at end of script) for sample code.

Following is a list of classes and functions in this module that Python programmers can use to incorporate hypothes.is functionality in their scripts.

### Annotation()

An object class for a single hypothes.is annotation. Call Annotation(json_data_for_single_annotation) to create a new object. This object has the following attributes:

- title (the title of the annotated article)  
- uri (the uri of the annotated article)  
- highlight (the article text highlighted in the annotation)  
- comment (the annotation comment left by the annotator)  
- user (the hypothes.is user ID of the annotator)  
- created (the date and time the annotation was created)  
- updated (the date and time the annotation was updated)  
- id (the unique ID of the hypothes.is annotation; this ID is included in the URL for the annotation)  
- hypothesisurl (the URL for the annotation)  

### retrieve()

A function that retrieves the JSON data for a single hypothes.is annotation, given the annotation's API URL. Call retrieve(api_url_for_a_single_annotation) to retrieve the JSON data, for passing into the Annotation() class.

### retrievelist()

A function that retrieves the JSON data for a list of hypothes.is annotations, given a well-formed search URL for the hypothes.is API. Call retrievelist(search_url_for_the_hypthes.is_api) to retrieve the JSON data for all annotations in the search results. Each annotation's JSON data is an item in a list. Use a for loop to pass each item returned into the Annotation() class.

### apiurl()

A function that converts a *share* URL (easy to find in the hypothes.is user interface) into an API-friendly URL (difficult to find), for passing to retrieve(). Call apiurl(share_url_for_an_individual_annotation) to return the API-friendly URL.

### searchurl()

A function that takes a hypothes.is user name and/or a tag (or list of tags) and generates a well-formed search URL for the hypothes.is API. The format is:

~~~ Python
searchurl(user = '', tag = '', tags = [])
~~~

The searchurl() function requires at least one search term. It can be either a user name, a single tag, or a list of tags (as a well-formed Python list). Use *either* a single tag or a list of tags, not both. If you happen to send it both, it will take the list of tags and ignore the single tag.

Example searches:

~~~ Python
# all annotations from a single user
searchurl(user = 'kris.shaffer@hypothes.is')
# or
searchurl('kris.shaffer@hypothes.is')

# all annotations tagged IndieEdTech
searchurl(tag = 'IndieEdTech')

# all annotations from a single user tagged IndieEdTech
searchurl(user = 'kris.shaffer@hypothes.is', tag = 'IndieEdTech')
# or
searchurl('kris.shaffer@hypothes.is', 'IndieEdTech')

# all annotations tagged IndieEdTech AND EdTech (for an OR search, simply perform two searches and combine the results)
searchurl(tags = ['IndieEdTech', 'EdTech'])
~~~

### Example code

~~~ Python
# search for all annotations with the tag IndieEdTech and return them in json format.
s = searchurl(tag = 'IndieEdTech')
l = retrievelist(s)

# print the title of each article annotated.
for entry in l:
    e = Annotation(entry)
    print(e.title)
~~~

~~~ Python
# Using the hyothes.is annotation share URL, retrieve and parse the JSON data for that annotation, then print it.
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
~~~
