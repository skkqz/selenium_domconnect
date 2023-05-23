import os

from dotenv import load_dotenv

load_dotenv()

email = os.getenv('email')
password = os.getenv('password')


sing_in_path = '/html/body/div[1]/header/div/ul[2]/li[2]/a'
input_email_xpath = '//*[@id="form-login"]/div[1]/div/input'
input_password_xpath = '//*[@id="login-password"]'
login_button_xpath = '//*[@id="form-login"]/div[7]/button'
