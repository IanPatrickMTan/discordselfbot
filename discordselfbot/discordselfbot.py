'''EPIC SELF BOTTING MODULE BY YOURS TRULY'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class discordMessage:
    def __init__(self, message, user, time, id):
        self.message = message
        self.user = user
        self.time = time
        self.id = id

class bot:

    def __init__(self, username, password, **more):
        options = webdriver.ChromeOptions()
        if 'driverPath' in more:
            driverPath = more['driverPath']
        else:
            driverPath = '/HDD1/iantitor/Downloads/chromedriver'
        if 'chromePath' in more:
            options.binary_location = more['chromePath']
        else:
            options.binary_location = '/usr/bin/brave'
        self.driver = webdriver.Chrome(driverPath, chrome_options=options)
        self.driver.get('https://discord.com/login')
        while 1:
            try:
                self.driver.find_element_by_name('email').send_keys(username)
                break
            except:
                pass
        self.driver.find_element_by_name('password').send_keys(f'{password}\n')

    def goto(self, id):
        self.driver.get(f'https://discord.com/channels/@me/{id}')
    
    def send(self, message):
        self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div[2]/div').send_keys(f'{message}\n')
    
    def read(self, t = -1):
        return discordMessage(self.driver.find_elements_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')[t].get_attribute('innerHTML'), self.driver.find_elements_by_xpath('//*[@class="username-1A8OIy clickable-1bVtEA"]')[t].get_attribute('innerHTML'), self.driver.find_elements_by_xpath('//*[@class="timestamp-3ZCmNB"]//span')[t].get_attribute('innerHTML'), self.driver.find_elements_by_xpath('//*[@class="message-2qnXI6 cozyMessage-3V1Y8y wrapper-2a6GCs cozy-3raOZG zalgo-jN1Ica"]')[t].get_attribute('id').replace('chat-messages-', ''))
    
    def getMyName(self):
        return self.driver.find_element_by_xpath('//div[@class="size14-e6ZScH title-eS5yk3"]').get_attribute('innerHTML') + self.driver.find_element_by_xpath('//div[@class="hovered-d5PMVU"]').get_attribute('innerHTML')
    
    def addUser(self, user):
        self.driver.find_element_by_xpath('//*[@aria-label="Add Friends to DM"]').click()
        while 1:
            try:
                self.driver.find_element_by_xpath('//*[@class="input-1Rv96N"]').send_keys(f'{user}')
                break
            except:
                pass
        self.driver.find_element_by_xpath('//*[@class="input-1Rv96N"]').send_keys(f'\n')
        try:
            self.driver.find_element_by_xpath('//*[@class="button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN"]').click()
        except:
            self.driver.find_element_by_xpath('//*[@class="button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeMedium-1AC_Sl fullWidth-1orjjo grow-q77ONN"]').click()
    
    def removeUser(self, user):
        ActionChains(self.driver).context_click(self.driver.find_elements_by_xpath('//*[@class="members-1998pB thin-1ybCId scrollerBase-289Jih fade-2kXiP2"]//*')[1:-1][user]).perform()
        self.driver.find_element_by_xpath('//*[@class="item-1tOPte labelContainer-1BLJti colorDanger-2qLCe1 colorDefault-2K3EoJ"]').click()
    
    def leaveDm(self):
        href = self.driver.current_url.replace('https://discord.com/', '')
        ActionChains(self.driver).context_click(self.driver.find_element_by_xpath(f'//*[@href="{href}"]')).perform()
        self.driver.find_element_by_class_name('item-1tOPte labelContainer-1BLJti colorDanger-2qLCe1 colorDefault-2K3EoJ').click()