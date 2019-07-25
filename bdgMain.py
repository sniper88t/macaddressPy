import tkinter as tk
import timer

import time
import os

import csv

from selenium import webdriver

global glCount
glCount = 0

root = tk.Tk()
root.title("Welcome to You!")
root.geometry('400x200')


v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("One Minute"),
    ("Two Minutes"),
    ("Three Minutes")
]

def ShowChoice():
    print(v.get())

tk.Label(root,
         text="""Please Choose the time!""",
         justify = tk.CENTER,
         font=("Arial Bold", 16),
         padx = 20,pady=20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                  text=language,
                  padx = 30,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)

    glCount = 0
    button_widget = tk.Button(root,
                              width=20,
                              text="Click TO ME!",
                              command=clicked)
    button_widget.pack()


    def clicked():
        glCount =3
        global selection
        selection = v.get()
        if selection == 0:
            while True:
                #print(selection)
                #os.system('macshift.exe -i "Ethernet0"')
                #glcount = glcount +1
                with open('exam.csv') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    # line_countdef = 0
                    for row in csv_reader:
                        if glCount == 0:
                            print('Column names are {", ".join(row)}')
                            glCount += 1
                        # else:
                        if row == glCount:
                            print('\t{row[0]}, works in the {row[1]} department, and was born in {row[2]}.')
                            glCount += 1

                            driver = webdriver.Chrome("chromedriver.exe")
                            driver.set_page_load_timeout(10)
                            driver.get("http://localhost/scrappy/")
                            time.sleep(15)
                            driver.find_element_by_id("nome").clear()
                            driver.find_element_by_id("nome").send_keys(row[0])
                            time.sleep(1)
                            driver.find_element_by_id("email").clear()
                            driver.find_element_by_id("email").send_keys(row[1])
                            time.sleep(1)
                            driver.find_element_by_id("telefone").clear()
                            driver.find_element_by_id("telefone").send_keys(row[2])
                            time.sleep(1)
                            driver.find_element_by_id("btcon").click()
                            time.sleep(2)
                            driver.find_element_by_name("termos").click()
                            driver.find_element_by_id("btFinal").click()
                            time.sleep(20)

                            time.sleep(60)
                            os.system('macshift.exe -i "Ethernet0"')
                            driver.quit()
        elif selection == 1:
            while True:
                #print(selection)
                #os.system('macshift.exe -i "Ethernet0"')
                #glcount = glcount +1
                with open('exam.csv') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    # line_countdef = 0
                    for row in csv_reader:
                        if glCount == 0:
                            print('Column names are {", ".join(row)}')
                            glCount += 1
                        # else:
                        if row == glCount:
                            print('\t{row[0]}, works in the {row[1]} department, and was born in {row[2]}.')
                            glCount += 1

                            driver = webdriver.Chrome("chromedriver.exe")
                            driver.set_page_load_timeout(10)
                            driver.get("http://localhost/scrappy/")
                            time.sleep(15)
                            driver.find_element_by_id("nome").clear()
                            driver.find_element_by_id("nome").send_keys(row[0])
                            time.sleep(1)
                            driver.find_element_by_id("email").clear()
                            driver.find_element_by_id("email").send_keys(row[1])
                            time.sleep(1)
                            driver.find_element_by_id("telefone").clear()
                            driver.find_element_by_id("telefone").send_keys(row[2])
                            time.sleep(1)
                            driver.find_element_by_id("btcon").click()
                            time.sleep(2)
                            driver.find_element_by_name("termos").click()
                            driver.find_element_by_id("btFinal").click()
                            time.sleep(20)

                            time.sleep(120)
                            os.system('macshift.exe -i "Ethernet0"')
                            driver.quit()

        elif selection == 2:
            while True:
                # print(selection)
                #os.system('macshift.exe -i "Ethernet0"')
                # glcount = glcount +1
                with open('exam.csv') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    # line_countdef = 0
                    for row in csv_reader:
                        if glCount == 0:
                            print('Column names are {", ".join(row)}')
                            glCount += 1
                        # else:
                        if row == glCount:
                            print('\t{row[0]}, works in the {row[1]} department, and was born in {row[2]}.')
                            glCount += 1

                            driver = webdriver.Chrome("chromedriver.exe")
                            driver.set_page_load_timeout(10)
                            driver.get("http://localhost/scrappy/")
                            time.sleep(15)
                            driver.find_element_by_id("nome").clear()
                            driver.find_element_by_id("nome").send_keys(row[0])
                            time.sleep(1)
                            driver.find_element_by_id("email").clear()
                            driver.find_element_by_id("email").send_keys(row[1])
                            time.sleep(1)
                            driver.find_element_by_id("telefone").clear()
                            driver.find_element_by_id("telefone").send_keys(row[2])
                            time.sleep(1)
                            driver.find_element_by_id("btcon").click()
                            time.sleep(2)
                            driver.find_element_by_name("termos").click()
                            driver.find_element_by_id("btFinal").click()
                            time.sleep(20)

                            time.sleep(180)
                            os.system('macshift.exe -i "Ethernet0"')
                            driver.quit()





root.mainloop()