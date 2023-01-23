#import selenium dan time
from selenium import webdriver
import time

try:
    # membuka browser yang digunakan
    driver = webdriver.Firefox()
    driver.get('https://www.instagram.com/')

    # membuka file teks yang di isi user
    f = open("credential_login.txt", "r")
    baca = f.readline()
    baca1 = f.readline()

    # mengubah input user pada file teks berupa list ke string(teks)
    user = baca.split("'")[1::2]
    toStr_user = "{}".format(*user)
    pas = baca1.split("'")[1::2]
    toStr_pas = "{}".format(*pas)

    # waktu delay agar bisa input
    time.sleep(10)

    # input string ke dalam element user dan password serta login pada web
    username = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
    password = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
    username.send_keys(toStr_user)
    password.send_keys(toStr_pas)
    login_tombol = driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
    login_tombol.click()

    # Mengecek berhasil masuk atau gagal
    time.sleep(5)
    if 'accounts' in driver.current_url:
        print("Login berhasil")
    else:
        print("Login gagal")

except Exception as e:
    print("An error occurred:", e)
    driver.close()