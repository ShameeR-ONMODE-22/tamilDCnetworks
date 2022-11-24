import urllib.request
print(" Beginning file download ")
url = input("Enter valid url : ") 
urllib.request.urlretrieve(url, "./google.html")
