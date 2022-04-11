######################### WORK BOOK ########################################

#create a new excel document

wb = xl.Workbook()

MySheet = wb.active

MySheet.title = "First Sheet"



#create a new worksheet
wb.create_sheet(index=1,title="Movie Sheet")

#write content to a call
MySheet["A1"] = "No."
MySheet["B1"] = "Movie Title"
MySheet["C1"] = "Release Date"
MySheet["D1"] = "Gross"
MySheet["E1"] = "Total Gross"
MySheet["F1"] = "Percent of Total Gross"

#change the font size and italicize
MySheet["A1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
MySheet["B1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
MySheet["C1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
MySheet["D1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
MySheet["E1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)
MySheet["F1"].font = Font(name = "Time New Roman", size = 24, italic = True, bold = True)

#alternatively you can create a Font object and assign it 

fontobject = Font(name = "Time New Roman", size = 24, italic = True, bold = True)

MySheet["A1"].font = fontobject

#adding values to cells 
MySheet["A2"] = 1
MySheet["A3"] = 2
MySheet["A4"] = 3
MySheet["A5"] = 4
MySheet["A6"] = 5


MySheet["A6"] = "Total"
MySheet["A5"].font = Font(size=16, bold= True)

MySheet["B6"] = "=SUM(B2:B4)"

#change the column width
MySheet.column_dimensions["A"].width = 25 

wb.save("PythonToExcel.xlsx")