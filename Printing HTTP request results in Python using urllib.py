# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://docs.datacamp.com/teach/"

# This packages the request
request = Request("http://docs.datacamp.com/teach/")

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html=response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()
