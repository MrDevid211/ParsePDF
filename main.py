import pdfplumber

def pdf_read(pdf_path): #открываем на чтение
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()


    # записываем полученные данные из функций в переменные
    name = get_name(text)
    sector = "WHOLESALES"
    city = get_city(text)
    sh_holders = ""
    ex = get_ex(text)
    url = get_url(text)
    year = get_year(text)
    sales = get_sales(text)
    oper = get_oper(text)
    
    

    exl_write(name, sector, city, sh_holders, ex, url, year, sales, oper)

def exl_write(name, sector, city, sh_holders, ex, url, year, sales, oper):
    print(name, sector, city, sh_holders, ex, url, year, sales, oper)



def get_url(text): 
    #получаем текст ссылки
    url_text = text.split("Website:")
    url_text = text.split(" ")
    url_text = text.split("\n")

    for i in url_text:
        if "Website:" in i:
           
            url_text = i.split(":")#разделям текст ссылки на 2 части
            url_text = url_text[1]

    if "www" in url_text:
        pass
    else:
        url_text = ""
    return url_text #возвращаем текст ссылки


def get_year(text):

    year_text = text.split("Founded:")
    year_text = text.split(" ")
    year_text = text.split("\n")

    for i in year_text:
        if "Founded:" in i:
           
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
    return ex_text


def get_city(text):
    city_text = text.split("\n")
    city_text = city_text[7]
    return city_text


def get_oper(text):
    #разделяем по ключевым словам
    oper_text = text.split("Activities Description")
    oper_text = oper_text[1].split("Primary")
    oper_text = oper_text[0].split("\n")
    oper = ""
    for i in oper_text:

        #если в строке есть эти слова, то продолжаем цикл (пропускаем итерацию)
        if "Volume" in i or "Sales Type" in i :
            
            continue 
        
        elif "Description:" in i or "History:" in i:
            i = i.split("Effective Date / Description:")
            i = i[0]
            i = i.split("Sales History:")
            i = i[0]
            oper+=i

        #если в строке есть эта штука, то цикл останавливается
        elif "ADDITIONAL TELEPHONE NUMBER" in i:
            break
        #добавляем по 1 элементу в список, которые прошли проверку
        else:

            oper+=i


    return oper


pdf_read("Mergent Online - Reports _ BUFFALO ENGINE COMPONENTS, INC_.pdf")

pdf_read("Mergent Online - Reports _ BUDGET AUTO PARTS INC.pdf")
