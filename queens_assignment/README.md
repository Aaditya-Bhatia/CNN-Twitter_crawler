###CNN Crawler and Tweets Provider:

#CNN Crawler
For finding a particular keyword in a dynamic website, not all sites provide API keys. Performing crude spider operations can be scalable to different use-cases of web crawling. In the module (cnn_crawler.py), a particular keyword has been searched in the dynamic content of the website. The URL of the found content is extracted and displayed in a custom html page for a visually palatable experience.

#Twitter:
Twitter provides infinite scrolling in its pages. To extract the public tweets of a user, only a few number of the top tweets can be extracted. To combat this issue, twitter API has been used to extract any given number of tweets in for a public profile.


##Installation:

The following python libraries are to be installed in python:

pip install flask
pip install tweepy
pip install bs
pip install selenium

Steps for resolving Chrome Driver Issue in cnn_crawler.py:
1.Download chrome driver for your OS from the website: https://sites.google.com/a/chromium.org/chromedriver/downloads
2.Unzip the file to a specific location Eg. ‘/var/chromeDriver’
3.Edit the location in chromedriver in line.27 Of cnn_crawler.py module.
