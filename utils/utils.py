from datetime import datetime

def converter_string_para_datetime(string_data, formato):
    data = datetime.strptime(string_data, formato)
    return data

def converter_datetime_para_string(data, formato):
    string_data = data.strftime(formato)
    return string_data

