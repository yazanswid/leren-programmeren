from test_libe import *


def get_value(data: str, separator: str, position: int) -> str:
    """
    Haalt de waarde op uit de gegeven string data op basis van de opgegeven separator en positie.

    Parameters:
    data (str): De string met gegevens gescheiden door de separator.
    separator (str): Het karakter dat gebruikt wordt als scheidingsteken.
    position (int): De positie van de te retourneren waarde.

    Returns:
    str: De waarde op de opgegeven positie, of None als de positie ongeldig is.
    """
    splitted_strings = data.split(separator)  
    if 0 <= position < len(splitted_strings):  
        return splitted_strings[position]  
    else:
        return None  


test_data = [
    
    ('Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7', ',', 8, 'Bram:6'),
    ('Sofie:8,Emma:7,Ahmed:9', ',', 1, 'Emma:7'),
    ('muis,kat,hond', ',', 1, 'kat'),
    ('a,b,c,d', ',', 0, 'a'),
    ('1:2,3:4,5:6', ':', 1 , '3:4'),
    ('a,b,c', ',', 5, None),  
]


for data, separator, position, expected in test_data:
    result = get_value(data, separator, position)
    test(f'Test met data: {data}, separator: {separator}, position: {position}', expected, result)

report()