'''
Webscrapping Project:
Go to Google Finance
Print out top moving industry
Print out the biggest gaining stock and biggest losing stock
from said industry
'''
import urllib.request as ur
from bs4 import BeautifulSoup
import re
import pandas as pd


url = "https://www.google.com/finance"
url_response = ur.urlopen(url,timeout=5) #opens that url
soup = BeautifulSoup(url_response)

def string_to_abs_float(string):
    string = string.strip('%')
    absFloat = float(string [1:])
    return absFloat

def sectorMover(soup):
    '''
    returns data frame consisting of the biggest moving industry
    '''
    #initiate arrays
    links = list()
    sectors= list()
    movements = list()
    movementValues = list()

    #grab sectors table
    table = soup.find('div', {'id':'secperf'})

    #get links and sector names
    for link in table.find_all('a'):
        sectors.append(link.string)
        links.append(link.get('href'))

    #get movement
    for move in table.find_all('span'):
        movementValues.append(string_to_abs_float(move.string))
        movements.append(move.string)

    #return a DataFrame
    sector_dict = {"Sectors":sectors,
                  "Movements":movements,
                  "MovementVals":movementValues,
                  "URLs":links}
    sectorsDF = pd.DataFrame(sector_dict)
    biggestMover = sectorsDF.max()
    return biggestMover

def stocks(url):
    #open url and soup it
    url = "https://www.google.com"+url
    url_response = ur.urlopen(url,timeout=5) #opens that url
    soup = BeautifulSoup(url_response)

    #Get table
    table = soup.find("table", { "class" : "topmovers" })

    #Find position in table by finding gainer or loser
    rows = table.find_all("tr")
    for i in range(0,len(rows)):
        cells = rows[i].find_all("td")
        for cell in cells:
            if "Gainers" in cell.get_text():
                gainer = rows[i+1]
            if "Losers" in cell.get_text():
                loser = rows[i+1]

    #first td is name, second is symbol, third is trade, fourth is change
    gainerName = gainer.find('a').string
    gainerCHG = gainer.find("span", {'class' : 'chg'}).get_text()
    
    loserCHG = loser.find("span", {'class' : 'chr'}).get_text()
    loserName = loser.find('a').string
    return gainerName, gainerCHG, loserName, loserCHG

#pass in data frame to get the top stock movers
biggestMover = sectorMover(soup)
stocks = stocks(biggestMover.URLs)

print ("The biggest industry mover is " + biggestMover.Sectors + " (" + biggestMover.Movements + "). The biggest gainer was "
      + str(stocks[0]) + " with a gain of " +str(stocks[1])+ " and the biggest loser was "+str(stocks[2])
       +" with a loss of "+str(stocks[3]))
