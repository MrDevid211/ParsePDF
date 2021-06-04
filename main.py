import pdfplumber

def pdf_read(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()


    f = open("text.txt", "w")
    f.write(text)


        # print(text)
    url = get_url(text)
    year = get_year(text)
    name = get_name(text)
    sales = get_sales(text)
    ex = get_ex(text)
    city = get_city(text)
    get_oper(text)

def get_url(text):
    url_text = text.split("Website:")
    url_text = text.split(" ")
    url_text = text.split("\n")

    for i in url_text:
        if "Website:" in i:
           
            url_text = i.split(":")
            url_text = url_text[1]

    return url_text


def get_year(text):

    year_text = text.split("Started:")
    year_text = text.split(" ")
    year_text = text.split("\n")

    for i in year_text:
        if "Started:" in i:
           
            year_text = i.split(":")
            year_text = year_text[1]

    return year_text


def get_name(text):
    name_text = list(text)
    name_text = text.split("\n")
    name_text = name_text[1]
    return name_text


def get_sales(text):
    sales_text = text.split("Volume:")
    sales_text = text.split(" ")
    sales_text = text.split("\n")

    for i in sales_text:
        if "Volume:" in i:
           
            sales_text = i.split(":")
            sales_text = sales_text[1]

    return sales_text


def get_ex(text):
    ex_text = text.split("Executive:")
    ex_text = text.split(" ")
    ex_text = text.split("\n")

    for i in ex_text:
        if "Executive:" in i:
           
            ex_text = i.split(":")
            ex_text = ex_text[1]


def get_city(text):
    city_text = text.split("\n")
    city_text = city_text[7]
    return city_text


def get_oper(text):
    oper_text = text.split("Activities Description")
    oper_text = oper_text[1].split("Territory")
    oper_text = oper_text[0].split("\n")
    oper = ""
    for i in oper_text:
        
        if "Volume" in i or "Sales" in i or "Description:" in i or "History:" in i:
            continue 
        elif "ADDITIONAL TELEPHONE NUMBER" in i:
            break
        else:
            oper+=i


    print(oper)













pdf_read("Mergent Online - Reports _ BUDGET AUTO PARTS INC.pdf")