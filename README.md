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
