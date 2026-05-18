#you have a sales report in a dictionary format you are expected to change the 
#the format by filtering out the sold items and report them
#goal: is to format the ssales report for the sold and unsold item
#let me demonestrate this using the standard way
#def format_sales_report(data: list[dict]) -> dict:
#    report = {}
#    for item in data:
#        if item["sold"] == True:
#            name_in_caps = item["item_name"].upper()
#            report[name_in_caps] = item["price"]
#    return report

sales_data = [{"item_name":"paper","price":200,"sold":True},
              {"item_name":"pen","price":50,"sold":False},
              {"item_name":"Highlighter","price":100,"sold":True},
              {"item_name":"stamp","price":40,"sold":False}]
#print(format_sales_report(sales_data))
#now i will demonestrate in comprehension way

def format_sales_report(data: list[dict]) -> dict:
    return {item["item_name"].upper():item["price"] for item in data if item["sold"]}

print(format_sales_report(sales_data))

#Lesson learnt
#Standard Loop: "Start with an empty box. For every item, if it's sold, put a label in the box."
#Comprehension: "Create a box containing labels for every sold item in the data."
