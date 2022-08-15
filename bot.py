from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from download_discord_file import download_discord_file
import time
import argparse

parser = argparse.ArgumentParser(
    description='Download Stable Diffusion Images From Discord')
parser.add_argument('-E', '--email', type=str, required=True,
                    help='Email Associated With Your Discord Account')
parser.add_argument('-P', '--password', type=str,
                    required=True, help='Your Discord Password')
parser.add_argument('-W', '--waittime', type=int, default=30,
                    help='Time to wait in seconds for you to load all your notifications')
args = parser.parse_args()


email = args.email
password = args.password

opts = Options()
opts.headless = False
browser = Chrome(options=opts)
browser.get('https://discord.com/login')
email_element = browser.find_element_by_name('email')
email_element.send_keys(email)

password_element = browser.find_element_by_name('password')

password_element.send_keys(password)

password_element.submit()

print('Successfully logged in')

time.sleep(5)

actions = ActionChains(browser)

buttons = browser.find_elements_by_class_name(
    'iconWrapper-2awDjA:nth-child(2)')

inbox = buttons[1]

actions.move_to_element(inbox
                        ).click().perform()

time.sleep(args.waittime)


mentions_list = browser.find_elements_by_class_name('container-iA3Qrz')

for mention in mentions_list:
    message = mention.find_element_by_class_name(
        'messageContent-2t3eCI')
    message = message.text
    if message.find('Dreamt') != 0 or message.find('Dreamt') == -1:
        continue
    first_quote = message.index('"')
    second_quote = message.index('"', first_quote + 1)
    prompt = message[first_quote +
                     1:second_quote].replace('.', '').replace('?', '').replace(',', '').replace('-', '').replace('_', '')

    try:
        seeds = message[message.index('[')+1:len(message)-1]
        seeds = [int(seed.strip()) for seed in seeds.split(',')]
    except:
        seeds = [message[message.index('-S')+2:len(message)]]

    images = mention.find_elements_by_class_name('originalLink-Azwuo9')
    for i, image in enumerate(images):
        download_discord_file(image.get_attribute('href'), prompt, seeds[i])
