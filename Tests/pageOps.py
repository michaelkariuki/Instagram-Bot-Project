from time import sleep

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def login(self, username, password):
        
        if self.check_loginPage(self.browser):
            #wait for page to load fully
            self.browser.implicitly_wait(5)

            #Finding the elements for logining in and password
            username_input = self.browser.find_element_by_css_selector("input[name='username']")
            password_input = self.browser.find_element_by_css_selector("input[name='password']")

            # using "send_keys" func to key in username and password
            username_input.send_keys(username)
            password_input.send_keys(password)

            # Telling the browser to wait for 2 secs for the browser to allow me to log in 
            self.browser.implicitly_wait(2)

            # Telling the browser to wait for 2 secs for the browser to allow me to log in 
            login_button = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
            login_button.click()
            sleep(5)
        else:
            print("Cant find elements/Aready logged in")

    def check_loginPage(self, browser):
        elements_list = ["input[name='username']", "input[name='password']"]
        result_list = []

        for element in elements_list:
            result_list.append(browser.find_elements_by_css_selector(element))

        return True if len(result_list) > 0 else False



