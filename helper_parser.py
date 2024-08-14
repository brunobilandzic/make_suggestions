def percentage_to_float(percentage):
    return float(percentage.replace("%", ""))


def  parse_int_input(inpuit_text, callback):
    while True:
        input_string = input(inpuit_text)
        if input_string == "b" or input_string ==  "B":
            callback()
            return 
        else:
            try:
                return int(input_string)
            except ValueError:
                print("Please input valid numver")
                continue
            
            
def parse_regular_input(input_text, callback):
    input_string = input(input_text)
    if input_string == "b" or input_string == "B":
        callback()
        return
    else:
        return input_string
    

def excel_float_to_float(float_number_string):
    try:
        float_number =  float(float_number_string.replace(",", ""))
        return float_number / 1000
    except:
        return 0
    
    
def float_to_string(float_number):
    float_string = str(float_number)
    return float_string[:3] if float_number > 99.999 else float_string[:2] if float_number > 9.9999 else float_string[:1]


def translate_croatian_letters(string_to_translate):
    return string_to_translate.replace("?", "c")


def make_string_withoute_whitespace(string_to_manipulate):
    return string_to_manipulate.replace(" ", "")