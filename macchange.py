import tkinter as tk
from threading import Timer

import time
import os
import csv
import win32api
import win32con
import random
import requests
import json
from selenium import webdriver
from tkinter.filedialog import askopenfilename
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


root = tk.Tk()
root.title("Welcome to You!")
root.geometry('340x320')


v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("One Minute"),
    ("Two Minutes"),
    ("Three Minutes"),
    ("Five Minutes"),
    ("Ten Minutes"),
    ("Fifteen Minutes"),
    ("No Minutes"),
]

def ShowChoice():
    print(v.get())

def rand_mac():
 return "%02x%02x%02x%02x%02x%02x" % (
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255)
 )

def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()

def eth():
    filename = askopenfilename()
    global selection
    selection = v.get()
    glCount = 0

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        # line_countdef = 0
        for row in csv_reader:
            if glCount == 0:
                print(f'Column names are {", ".join(row)}')
                glCount += 1
            else:
                print(f'\t{row[1]}, works in the {row[2]} department, and was born in {row[3]}.')

                # os.system('macshift.exe -i "Ethernet"')

                # strmac = rand_mac().upper()
                # os.system('macshift.exe -i "Ethernet" ' + strmac)
                # print (strmac)
                time.sleep(5)
                try:
                    driver = webdriver.Chrome("chromedriver.exe")
                    driver.set_page_load_timeout(20)
                    # driver.get("http://localhost/scrappy/")
                    # driver.get("http://wibox.net/")
                    driver.get("http://localhost/mymac1")
                except TimeoutException:
                    driver.quit()
                    continue
                print("a")
                timeout = 20
                try:
                    element_present = EC.presence_of_element_located((By.ID, 'nome'))
                    WebDriverWait(driver, timeout).until(element_present)
                    print("b")
                except TimeoutException:
                    # print ("Timed out waiting for page to load")
                    # win32api.MessageBox(0, 'The page could not be loaded.', 'Warning',
                    # win32con.MB_OK | win32con.MB_ICONINFORMATION)
                    driver.quit()
                    continue
                time.sleep(23)
                # driver.find_element_by_id("nome").clear()
                # time.sleep(5)

                # driver.find_element_by_id("telefone").send_keys(row[2])
                images = driver.find_elements_by_tag_name('img')
                pngPath = []
                realpngpath =""
                for image in images:
                    pngPath.append(image.get_attribute('src'))
                    #print(image.get_attribute('src'))
                realpngpath = pngPath[4]
                print(pngPath[4])

                test_url = ocr_space_url(url=realpngpath, overlay=False, api_key='4ae4c5519f88957',
                                         language='eng')

                z = json.loads(test_url)
                print(z.get('ParsedResults')[0].get('ParsedText'))
                driver.find_element_by_id("resposta").send_keys(z.get('ParsedResults')[0].get('ParsedText'))
                time.sleep(1)
                driver.find_element_by_id("btcon").click()
                time.sleep(1)
                #strpwdinvalid = driver.find_element_by_css_selector("#exibeErro")

                print("c")
                try:
                    print("d")
                    time.sleep(15)
                    driver.find_element_by_name("termos").click()
                    time.sleep(1)
                    driver.find_element_by_id("btFinal").click()
                    time.sleep(1)
                    print("e")
                    # driver.execute_script("window.open('https://www.google.com')")
                    # driver.execute_script("window.open('https://www.uol.com.br')")
                    # driver.execute_script("window.open('https://www.youtube.com')")

                except:
                    try:
                        time.sleep(10)
                        driver.find_element_by_name("termos").click()
                        time.sleep(1)
                        driver.find_element_by_id("btFinal").click()
                        print("f")
                        time.sleep(1)
                        # driver.execute_script("window.open('https://www.google.com')")
                        # driver.execute_script("window.open('https://www.uol.com.br')")
                        # driver.execute_script("window.open('https://www.youtube.com')")
                    except:
                        # os.system('macshift.exe -i "Ethernet"')
                        time.sleep(1)
                        print('z')
                        if selection == 2:
                            time.sleep(60 * (selection + 1))
                        if selection == 3:
                            time.sleep(60 * (selection + 2))
                        if selection == 4:
                            time.sleep(60 * (selection + 6))
                        if selection == 5:
                            time.sleep(60 * (selection + 10))
                        if selection == 6:
                            time.sleep(1)
                        else:
                            time.sleep(60 * (selection + 1))
                        driver.quit()
                        continue
                print("g")
                if selection == 2:
                    time.sleep(60 * (selection + 1))
                if selection == 3:
                    time.sleep(60 * (selection + 2))
                if selection == 4:
                    time.sleep(60 * (selection + 6))
                if selection == 5:
                    time.sleep(60 * (selection + 10))
                if selection == 6:
                    time.sleep(1)
                else:
                    time.sleep(60 * (selection + 1))
                glCount += 1
                print("h")
                # os.system('macshift.exe -i "Ethernet"')
                # time.sleep(5)
                driver.quit()
                # while True:
                # print(selection)
                # os.system('macshift.exe -i "Ethernet0"')


def wifi():
    filename = askopenfilename()
    global selection
    selection = v.get()
    glCount = 0

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        # line_countdef = 0
        for row in csv_reader:
            if glCount == 0:
                print(f'Column names are {", ".join(row)}')
                glCount += 1
            else:
                print(f'\t{row[1]}, works in the {row[2]} department, and was born in {row[3]}.')

                # os.system('macshift.exe -i "Ethernet"')

                # strmac = rand_mac().upper()
                # os.system('macshift.exe -i "Ethernet" ' + strmac)
                # print (strmac)
                time.sleep(5)
                try:
                    driver = webdriver.Chrome("chromedriver.exe")
                    driver.set_page_load_timeout(20)
                    # driver.get("http://localhost/scrappy/")
                    # driver.get("http://wibox.net/")
                    driver.get("http://localhost/mymac1")
                except TimeoutException:
                    driver.quit()
                    continue
                print("a")
                timeout = 20
                try:
                    element_present = EC.presence_of_element_located((By.ID, 'nome'))
                    WebDriverWait(driver, timeout).until(element_present)
                    print("b")
                except TimeoutException:
                    # print ("Timed out waiting for page to load")
                    # win32api.MessageBox(0, 'The page could not be loaded.', 'Warning',
                    # win32con.MB_OK | win32con.MB_ICONINFORMATION)
                    driver.quit()
                    continue
                time.sleep(23)
                # driver.find_element_by_id("nome").clear()
                # time.sleep(5)

                # driver.find_element_by_id("telefone").send_keys(row[2])
                images = driver.find_elements_by_tag_name('img')
                pngPath = []
                realpngpath = ""
                for image in images:
                    pngPath.append(image.get_attribute('src'))
                    # print(image.get_attribute('src'))
                realpngpath = pngPath[4]
                print(pngPath[4])

                test_url = ocr_space_url(url=realpngpath, overlay=False, api_key='4ae4c5519f88957',
                                         language='eng')

                z = json.loads(test_url)
                print(z.get('ParsedResults')[0].get('ParsedText'))
                driver.find_element_by_id("resposta").send_keys(z.get('ParsedResults')[0].get('ParsedText'))
                time.sleep(1)
                driver.find_element_by_id("btcon").click()
                time.sleep(1)
                # strpwdinvalid = driver.find_element_by_css_selector("#exibeErro")

                print("c")
                try:
                    print("d")
                    time.sleep(15)
                    driver.find_element_by_name("termos").click()
                    time.sleep(1)
                    driver.find_element_by_id("btFinal").click()
                    time.sleep(1)
                    print("e")
                    # driver.execute_script("window.open('https://www.google.com')")
                    # driver.execute_script("window.open('https://www.uol.com.br')")
                    # driver.execute_script("window.open('https://www.youtube.com')")

                except:
                    try:
                        time.sleep(10)
                        driver.find_element_by_name("termos").click()
                        time.sleep(1)
                        driver.find_element_by_id("btFinal").click()
                        print("f")
                        time.sleep(1)
                        # driver.execute_script("window.open('https://www.google.com')")
                        # driver.execute_script("window.open('https://www.uol.com.br')")
                        # driver.execute_script("window.open('https://www.youtube.com')")
                    except:
                        # os.system('macshift.exe -i "Ethernet"')
                        time.sleep(1)
                        print('z')
                        if selection == 2:
                            time.sleep(60 * (selection + 1))
                        if selection == 3:
                            time.sleep(60 * (selection + 2))
                        if selection == 4:
                            time.sleep(60 * (selection + 6))
                        if selection == 5:
                            time.sleep(60 * (selection + 10))
                        if selection == 6:
                            time.sleep(1)
                        else:
                            time.sleep(60 * (selection + 1))
                        driver.quit()
                        continue
                print("g")
                if selection == 2:
                    time.sleep(60 * (selection + 1))
                if selection == 3:
                    time.sleep(60 * (selection + 2))
                if selection == 4:
                    time.sleep(60 * (selection + 6))
                if selection == 5:
                    time.sleep(60 * (selection + 10))
                if selection == 6:
                    time.sleep(1)
                else:
                    time.sleep(60 * (selection + 1))
                glCount += 1
                print("h")
                # os.system('macshift.exe -i "Ethernet"')
                # time.sleep(5)
                driver.quit()
                # while True:
                # print(selection)
                # os.system('macshift.exe -i "Ethernet0"')


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

slogan = tk.Button(root,
                width=20,
                text="Ethernet",
                command=eth)
slogan.pack()




wifi = tk.Button(root,
                width=20,
                text="Wi-Fi",
                command=wifi)

wifi.pack()




root.mainloop()