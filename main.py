try:
    import xlsxwriter
except NameError:
    pass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException , ElementClickInterceptedException
import time




options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options,executable_path=rf"D:\Yazilim\Python\PythonWritten\Instagram Bot 2023\chromedriver.exe")


question = ""
login = 0
# followercount = 0


def getfollower():
    users = []
    count = 0
    usersStatistics = []
    driver.get(f"https://www.instagram.com/{inputusername}/")
    driver.implicitly_wait(10)
    time.sleep(2)

    followercount = driver.find_elements(By.CLASS_NAME,'_ac2a')
    for i in followercount:
        usersStatistics.append(i.text)
                    
    print(f"Follower Count: {followercount}\n\n\n") 
    print(f"Group: {usersStatistics}")    
    
    driver.find_element(By.XPATH,f'//a[@href="/{inputusername}/followers/"]').click()
    driver.implicitly_wait(10) 
    time.sleep(5)
    
    # scrollheight = driver.find_element(By.CLASS_NAME,'_aano').get_attribute('scrollHeight')       
    userscount = 0
    scrollRate = 5000
    while userscount != int(usersStatistics[1]):
        scrollheight = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]').get_attribute('scrollTop') # Scrollun sonu. Eğer değişmezse sonu gelmiştir.
        time.sleep(2)
        userscount2 = int(driver.execute_script(f"return document.querySelector('body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(1) > div').childElementCount"))
        print(f" Child Element Count: {userscount}\n\n\n")
        driver.execute_script(f"document.querySelector('body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scrollTo(0,{str(float(scrollheight) +scrollRate) })")
        # driver.execute_script("window.scrollTo(0, 500)")  
        scrollheightSecond = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]').get_attribute('scrollTop')
        time.sleep(1.5)
        userscount = int(driver.execute_script(f"return document.querySelector('body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(1) > div').childElementCount"))
        print(scrollRate)
        print(f"54- User Count2: {userscount2}")
        print(f"55- User Count: {userscount}")
        print(f"\nScroll Height one: {scrollheight}")
        print(f"Scroll Height second: {scrollheightSecond}\n")

        if scrollheight == scrollheightSecond:
            scrollRate = scrollRate//2
            print(f"Scroll Rate: {scrollRate}\n\n")
        else:
            print("Pass")
            pass
        
        if userscount == userscount2:
            if count>=10:
                break
            else:
                count +=1
                print(f"68- Count: {count}")

        else:
            print(f"71- Count: {count}")
            print(f"72- Usercount2: {userscount2}")
    

    x=1
    print(f"userStatistic: {usersStatistics[1]}")
    while x != usersStatistics[1]:   
        print(f"x: {x}")
        try:                  
            users.append(driver.find_element(By.XPATH,f'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{x}]/div/div/div/div[2]/div/div/div/div[1]/div/a/div/div/span').text)
        except:
            print("Bozuldu")
            break
        x += 1

    with open(r"follower.txt","w", encoding = "UTF-8") as file:
      for i in users:
        file.write(i+"\n")
    
    print(f"Child Element Count: {userscount}\n\n")

def getfollow():
    count = 0
    users = []
    usersStatistics = []
    driver.get(f"https://www.instagram.com/{inputusername}/")
    driver.implicitly_wait(10)
    time.sleep(2)

    followercount = driver.find_elements(By.CLASS_NAME,'_ac2a')
    for i in followercount:
        usersStatistics.append(i.text)
                    
    print(f"Follow Count: {followercount}\n\n\n") 
    print(f"Group: {usersStatistics}")    
    driver.find_element(By.XPATH,f'//a[@href="/{inputusername}/following/"]').click()
    driver.implicitly_wait(10)
    time.sleep(5)
    
    # scrollheight = driver.find_element(By.CLASS_NAME,'_aano').get_attribute('scrollHeight')       
    userscount = 0
    scrollRate = 5000
    while userscount != int(usersStatistics[2]):
        scrollheight = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]').get_attribute('scrollTop')
        time.sleep(2)                                   
        userscount2 = int(driver.execute_script(f"return document.querySelector('body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(1) > div').childElementCount"))
        
        print(f"User Count2: {userscount2}")
        print(f"Child Element Count: {userscount}\n\n\n")
        # driver.execute_script(f"return document.querySelector('body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1)').scrollTo(0,{str(int(scrollheight) +scrollRate) })")
        # driver.execute_script(f"return document.querySelector('body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div').scrollTo(0,{str(int(scrollheight) +scrollRate) })")
        driver.execute_script(f"document.querySelector('body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scrollTo(0,{str(float(scrollheight) +scrollRate) })")
        # driver.execute_script("window.scrollTo(0, 500)")
        scrollheightSecond = driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]').get_attribute('scrollTop')
        time.sleep(1.5)
        userscount = int(driver.execute_script(f"return document.querySelector('body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(1) > div').childElementCount"))
        if scrollheight == scrollheightSecond:
            scrollRate = scrollRate//2
            print(f"Scroll Rate: {scrollRate}\n\n")
        else:
            pass

        if userscount == userscount2:
            if count>=10:
                break
            else:
                count +=1
                print(f"68- Count: {count}")
        else:
            print(f"120- Count: {count}")
            print(f"121- Usercount2: {userscount2}")
    x=1
    while x != usersStatistics[2]:      
        print(f"x: {x}")   
        try:               
            users.append(driver.find_element(By.XPATH,f'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div/div/div[{x}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span').text)
        except:
            print("Bozuldu")
            break
        x += 1
    print(f"LEN: {len(users)}, x: {x}")

    with open(r"follow.txt","w", encoding = "UTF-8") as file:
      for i in users:
        file.write(i+"\n")


def compare():
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet()
    follow  = []
    follower = []
    result_Following = []
    result_NotFollowing = []

    with open(r"follow.txt", "r", encoding="utf-8") as file:
        text = file.readlines()
        col = 1
        worksheet.write(0,0,"Takip Edilen")
        for i in text:
            worksheet.write(col,0,i)
            col+=1
            i = i[:-1]
            follow.append(i)


    with open(r"follower.txt", "r", encoding="utf-8") as file:
        text = file.readlines()
        col = 1
        worksheet.write(0,1,"Takip Edilen")
        for i in text:
            worksheet.write(col,1,i)
            col += 1
            i=i[:-1]
            follower.append(i)
    

    kp = 0
    for i in follow:                     # Takip ettiklerin resfollowdaysa geç değilse resnotfollowa ekle             
        print(i)
        kp+=1
        j = 0
        if i in follower:
            print("155")
        else:
            print("158")
            print(i)
            result_NotFollowing.append(i)
        print("313131")


    print(follow)
    with open(r"result.txt","w",encoding="utf-8") as file:
        col = 1
        worksheet.write(0,2,"Kıyaslama")

        for i in result_NotFollowing:
            worksheet.write(col,2,f"{i} adlı kişi {inputusername} adlı kişiyi takip etmiyor. X\n")
            col+=1
    print(result_Following)
    print(result_NotFollowing)
    workbook.close()


while login == 0:
    print("while")
    print("dön")
    driver.get("https://www.instagram.com")
    driver.implicitly_wait(10)

    loginusername = ""
    loginpassword = ""
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(loginusername)
    driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(loginpassword)
    time.sleep(1)
    driver.execute_script('document.querySelector("#loginForm > div > div:nth-child(3) > button").click()')
    driver.implicitly_wait(10)
    time.sleep(4)
    login = 1


while True:
    process = input("Please write a process number.\n1- Get a followers names.\n2- Get names you followed.\n3- See who doesn't follow you. (Firstly you need to do first and second process.)\n")
    inputusername = input("Please write a username you want to do process: ")

    if process == "1":
        getfollower()
    elif process == "2":
        getfollow()
    elif process == "3":
        compare()