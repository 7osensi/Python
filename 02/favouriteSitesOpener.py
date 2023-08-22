import webbrowser

sitesList = ["http://youtube.com", "http://google.com", "https://www.w3schools.com/python/"]

def openBrowser(site):#function definition
    webbrowser.open(site) 

ChosenSite = int(input("Choose a site :  (youtube :> [1] || google :> [2] || and w3schools_pyhton :> [3]): "))

openBrowser(sitesList[ChosenSite - 1]) #funciton call