from webcolors import hex_to_name

def color_code_to_name(color_code):
    try:
        color_name = hex_to_name(color_code)
        return color_name
    except ValueError:
        return None
colorcode = input("enter color code: ")
result_name = color_code_to_name(colorcode)
print(result_name)