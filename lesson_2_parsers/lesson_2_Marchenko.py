from lxml import html
import requests
from openpyxl import Workbook


wb = Workbook()
list = wb.active
list.append(("Вакансия", "Ссылка на сайт", "Ссылка на вакансию", "Минимальная зп рубли", "Максимальная зп рубли"))
page = 6
data_to_write = []

def append_elems(job_name, job_link, site_link, min_salary, max_salary):
    data_to_write.append([job_name, job_link, site_link, min_salary, max_salary])

def salary_check(salary, salary_per_time):
    if '—' in salary:
        min_salary = salary[0] + " " + salary_per_time[0]
        max_salary = salary[4] + " " + salary_per_time[0]
        return [min_salary, max_salary]
    elif "от" in salary:
        min_salary = salary[2] + " " + salary_per_time[0]
        max_salary = "No Data"
        return [min_salary, max_salary]
    elif "до" in salary:
        min_salary = "No Data"
        max_salary = salary[2] + " " + salary_per_time[0]
        return [min_salary, max_salary]
    elif "По договорённости" in salary:
        min_salary = "Договорная"
        max_salary = "Договорная"
        return [min_salary, max_salary]
    else:
        min_salary = salary[0] + " " + salary_per_time[0]
        max_salary = "No Data"
        return [min_salary, max_salary]
        

text_check = ["next"]

while True:
    url = f"https://www.superjob.ru/vakansii/kurer.html?page={page}"
    response = requests.get(url)
    page += 1
    root = html.fromstring(response.content)
    jobs = root.xpath("//div[@class='_3-q4I zw6Ta _3ybL_']")
    value_check = root.xpath("//div[@class='_3-q4I _9mI07 oSSgx _3SNg7 _364xK _1ApxH _3ybL_']/a[@class = '_1IHWd _6Nb0L _37aW8 _17KD8 f-test-button-dalshe f-test-link-Dalshe']/@rel")
    if text_check != value_check:
        break
    for job in jobs:
        hrefs = job.xpath("//span[@class='_1c5Bu _1Yga1 _1QFf5 _2MAQA _1m76X _3UZoC _3zdq9 _1_71a']/a/@href")
        for el in hrefs:
            new_response = requests.get('https://www.superjob.ru' + el)
            new_root = html.fromstring(new_response.content)
            name = new_root.xpath("//h1[@class='_1c5Bu Qtbsi PZF7Y _2MAQA _1m76X _3UZoC _1_71a']/text()")
            site_link = new_root.xpath("//head/link[@rel='canonical']/@href")
            salary = new_root.xpath("//span[@class='_4Gt5t _3Kq5N']/span[@class='_2eYAG _1m76X _3UZoC _3iH_l']/text()")
            salary_per_time = new_root.xpath("//span[@class='_4Gt5t _3Kq5N']/span[@class='_1m76X _3UZoC _3iH_l']/text()")
            result = salary_check(salary, salary_per_time)
            append_elems(name[0], 'https://www.superjob.ru/', site_link[0], result[0], result[1])
                        

for el in data_to_write:
    list.append(el)


wb.save('output.xlsx')

    