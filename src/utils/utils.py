def drop_row_without_value(arg, database):
    """
    delete row with empty value in df data
    arg = name of the columns
    """
    nan_value = float("NaN")
    database.replace("", nan_value, inplace=True)
    database.dropna(subset=[arg], inplace=True)


def replace_string_by_value(column, numbers, replaces, database="data"):
    """Replace String by int for machine learning training
    columns = name of the column
    number = int to replace the string
    replace = name of the string to replace
    inplace : True"""
    for number, replace in zip(numbers, replaces):
        database[column].replace(number, replace, inplace=True)


def change_to_province(postal_code):
    if postal_code >= 1000 and postal_code < 1300:
        return "Brussel","Brussel",1,1
    elif postal_code >= 1300 and postal_code < 1500:
        return "Brabant Wallon","Wallonia",2,2
    elif (postal_code >= 1500 and postal_code < 2000) or (postal_code >= 3000 and postal_code < 3500):
        return "Brabant Flamand","Flanders",3,3
    elif postal_code >= 2000 and postal_code < 3000:
        return "Anvers","Flanders",4,3
    elif postal_code >= 3500 and postal_code < 4000:
        return "Limbourg","Flanders",5,3
    elif postal_code >= 4000 and postal_code < 5000:
        return "Liège","Wallonia",6,2
    elif postal_code >= 5000 and postal_code < 6000:
        return "Namur","Wallonia",7,2
    elif (postal_code >= 6000 and postal_code < 6600) or (postal_code >= 7000 and postal_code < 8000):
        return "Hainaut","Wallonia",8,2
    elif postal_code >= 6600 and postal_code < 7000:
        return "Luxembourg","Wallonia",9,2
    elif postal_code >= 8000 and postal_code < 9000:
        return "Flandre Occidental","Flanders",10,3
    elif postal_code >= 9000:
        return "Flandre Oriental","Flanders",11,3