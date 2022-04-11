
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##

movie_table = soup.find("table")
#print(movie_table)

movie_rows = movie_table.findAll("tr")
#print(movie_rows[1])

for x in range(1,6):
    td = movie_rows[x].findAll("td")
    ranking = td[0].text
    title = td[1].text
    gross = td[5].text
    total_gross = td[7].text

    print(gross)
    input()


######################### WORK BOOK ########################################

#create a new excel document

wb = xl.Workbook()

ws = wb.active

ws.title = "Box Office Report

#write content to a call
ws["A1"] = "No."
ws["B1"] = "Movie Title"
ws["C1"] = "Release Date"
ws["D1"] = "Gross"
ws["E1"] = "Total Gross"
ws["F1"] = "% of Total Gross"

#change the font size and italicize
ws["A1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
ws["B1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
ws["C1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
ws["D1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
ws["E1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
ws["F1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)

for x in range(1,6):
        td = movie_rows[x].findAll