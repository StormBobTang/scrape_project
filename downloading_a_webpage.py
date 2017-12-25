from urllib.request import urlopen

url  = "http://www.7k7k.com/"

def get_webpage(url):

    print("Getting Request Object")
    request = urlopen(url)
    print("Reading Request Object")
    data = request.read()
    text = data.decode("utf-8")

    print("Web Page Downloaded")
    return text

text = get_webpage(url)

# Here's the new stuff! 
# We will save the file as
# under the name html_text.txt
with open('html_text.txt', 'w') as f:
    f.write(text)