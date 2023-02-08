# library import statements
import requests

def getPageRequests(url):
    # call to requests.get()
    try:
        myres = requests.get(url)
    except:
        print("Don't work")
        return ""
    return myres.text

# get url from user
url = input("Enter the URL: ")
webContent = getPageRequests(url)

# open file for writing
webFile = open("output.txt", "w")
# write getPageRequests(url)
webFile.write(webContent)
# close file
webFile.close()
