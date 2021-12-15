# 08 - Export to Excel
# # XlsxWriter
# - https://xlsxwriter.readthedocs.io

import pandas as pd
remote_file = "https://raw.githubusercontent.com/LearnPythonWithRune/FinancialDataAnalysisWithPython/main/AAPL.csv"
data = pd.read_csv(remote_file, index_col=0, parse_dates=True)

print( data.head() )
### Moving Average
data['MA10'] = data['Close'].rolling(10).mean()

print( data.tail() )

### MACD
exp1 = data['Close'].ewm(span=12, adjust=False).mean()
exp2 = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = macd = exp1 - exp2
data['Signal line'] = exp3 = macd.ewm(span=9, adjust=False).mean()

print( data.tail() )

### Stochastic Oscillator

high14 = data['High'].rolling(14).max()
low14 = data['Low'].rolling(14).min()
data['%K'] = pct_k = (data['Close'] - low14)*100/(high14 - low14)
data['%D'] = pct_d = data['%K'].rolling(3).mean()

print( data.tail() )

### Time period

data = data.loc['2020-01-01':]
data = data.iloc[::-1]

print( data.head() )


###########################################
## Excel

writer = pd.ExcelWriter("technical.xlsx", 
                        engine='xlsxwriter', 
                        date_format = 'yyyy-mm-dd', 
                        datetime_format='yyyy-mm-dd')

workbook = writer.book

# Create a format for a green cell
green_cell = workbook.add_format({
    'bg_color': '#C6EFCE',
    'font_color': '#006100'
})

# Create a format for a red cell
red_cell = workbook.add_format({
    'bg_color': '#FFC7CE',                            
    'font_color': '#9C0006'
})

# **
# ** MA
# **
sheet_name = 'MA10'
data[['Close', 'MA10']].to_excel(writer, sheet_name=sheet_name)
worksheet = writer.sheets[sheet_name]

# Set column width of Date
worksheet.set_column(0, 0, 15)


for col in range(1, 3):
    # Create a conditional formatted of type formula
    worksheet.conditional_format(1, col, len(data), col, {
        'type': 'formula',                                    
        'criteria': '=B2>=C2',
        'format': green_cell
    })

    # Create a conditional formatted of type formula
    worksheet.conditional_format(1, col, len(data), col, {
        'type': 'formula',                                    
        'criteria': '=B2<C2',
        'format': red_cell
    })


# Create a new chart object.
chart1 = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart1.add_series({
        'name': 'AAPL',
        'categories': [sheet_name, 1, 0, len(data), 0],
        'values': [sheet_name, 1, 1, len(data), 1],
})

# Create a new chart object.
chart2 = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart2.add_series({
        'name': sheet_name,
        'categories': [sheet_name, 1, 0, len(data), 0],
        'values': [sheet_name, 1, 2, len(data), 2],
})

# Combine and insert title, axis names
chart1.combine(chart2)
chart1.set_title({'name': sheet_name + " AAPL"})
chart1.set_x_axis({'name': 'Date'})
chart1.set_y_axis({'name': 'Price'})

# Insert the chart into the worksheet.
worksheet.insert_chart('E2', chart1)


# **
# ** MACD
# **

sheet_name = 'MACD'
data[['Close', 'MACD', 'Signal line']].to_excel(writer, sheet_name=sheet_name)
worksheet = writer.sheets[sheet_name]

# Set column width of Date
worksheet.set_column(0, 0, 15)

for col in range(1, 4):
    # Create a conditional formatted of type formula
    worksheet.conditional_format(1, col, len(data), col, {
        'type': 'formula',                                    
        'criteria': '=C2>=D2',
        'format': green_cell
    })

    # Create a conditional formatted of type formula
    worksheet.conditional_format(1, col, len(data), col, {
        'type': 'formula',                                    
        'criteria': '=C2<D2',
        'format': red_cell
    })

# Create a new chart object.
chart1 = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart1.add_series({
        'name': 'MACD',
        'categories': [sheet_name, 1, 0, len(data), 0],
        'values': [sheet_name, 1, 2, len(data), 2],
})

# Create a new chart object.
chart2 = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart2.add_series({
        'name': 'Signal line',
        'categories': [sheet_name, 1, 0, len(data), 0],
        'values': [sheet_name, 1, 3, len(data), 3],
})

# Combine and insert title, axis names
chart1.combine(chart2)
chart1.set_title({'name': sheet_name + " AAPL"})
chart1.set_x_axis({'name': 'Date'})
chart1.set_y_axis({'name': 'Value'})

# To set the labels on x axis not on 0
chart1.set_x_axis({
    'label_position': 'low',
    'num_font':  {'rotation': 45}
})

# Insert the chart into the worksheet.
worksheet.insert_chart('F2', chart1)


# **
# ** Stochastic
# **

sheet_name = 'Stochastic'
data[['Close', '%K', '%D']].to_excel(writer, sheet_name=sheet_name)
worksheet = writer.sheets[sheet_name]

# Set column width of Date
worksheet.set_column(0, 0, 15)

for col in range(1, 4):
    # Create a conditional formatted of type formula
    worksheet.conditional_format(1, col, len(data), col, {
        'type': 'formula',                                    
        'criteria': '=C2>=D2',
        'format': green_cell
    })

    # Create a conditional formatted of type formula
    worksheet.conditional_format(1, col, len(data), col, {
        'type': 'formula',                                    
        'criteria': '=C2<D2',
        'format': red_cell
    })


# Create a new chart object.
chart1 = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart1.add_series({
        'name': '%K',
        'categories': [sheet_name, 1, 0, len(data), 0],
        'values': [sheet_name, 1, 2, len(data), 2],
})

# Create a new chart object.
chart2 = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart2.add_series({
        'name': '%D',
        'categories': [sheet_name, 1, 0, len(data), 0],
        'values': [sheet_name, 1, 3, len(data), 3],
})

# Combine and insert title, axis names
chart1.combine(chart2)
chart1.set_title({'name': sheet_name + " AAPL"})
chart1.set_x_axis({'name': 'Date'})
chart1.set_y_axis({'name': 'Value'})

# To set the labels on x axis not on 0
chart1.set_x_axis({
    'label_position': 'low',
    'num_font':  {'rotation': 45}
})

# Insert the chart into the worksheet.
worksheet.insert_chart('F2', chart1)

# End of sheets


# Close
writer.close()


