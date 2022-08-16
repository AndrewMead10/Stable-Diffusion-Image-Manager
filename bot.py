import argparse
import os
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from download_discord_file import download_discord_file
from split_image import split_image


parser = argparse.ArgumentParser(
    description='Download Stable Diffusion Images From Discord')
parser.add_argument('-E', '--email', type=str, required=True,
                    help='Email Associated With Your Discord Account')
parser.add_argument('-P', '--password', type=str,
                    required=True, help='Your Discord Password')
# to be added later
# parser.add_argument('-F', '--folder', type=str, const='images', help="Folder that the images will be saved to")
args = parser.parse_args()


email = args.email
password = args.password

opts = Options()
opts.headless = True
opts.add_argument("--log-level=3")
browser = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
browser.get('https://discord.com/login')
email_element = browser.find_element_by_name('email')
email_element.send_keys(email)

password_element = browser.find_element_by_name('password')

password_element.send_keys(password)

password_element.submit()

print('Successfully logged in')

time.sleep(10)

actions = ActionChains(browser)

buttons = browser.find_elements_by_class_name(
    'iconWrapper-2awDjA:nth-child(2)')

inbox = buttons[1]

actions.move_to_element(inbox
                        ).click().perform()

time.sleep(2)

while True:
    try:
        load_more = browser.find_element_by_class_name('lookFilled-yCfaCM')
        load_more.click()
        time.sleep(2)
    except:
        break


mentions_list = browser.find_elements_by_class_name('container-iA3Qrz')
previous = open('previous.txt', 'r').read()
is_first = True
for mention in mentions_list:
    message = mention.find_element_by_class_name(
        'messageContent-2t3eCI')
    message = message.text

    if message.find('Dreamt') != 0 or message.find('Dreamt') == -1:
        continue
    if message == previous:
        break
    if is_first:
        f = open('previous.txt', 'w')
        f.write(message)
        f.close()
        is_first = False

    first_quote = message.index('"')
    second_quote = message.index('"', first_quote + 1)
    prompt = message[first_quote +
                     1:second_quote].replace('.', '').replace('?', '').replace(',', '').replace('-', '').replace('_', '')



    images = mention.find_elements_by_class_name('originalLink-Azwuo9')
    print(f'Downloading {prompt}')
    if message.find('-g') == -1:
        try:
            seeds = message[message.index('[')+1:len(message)-1]
            seeds = [int(seed.strip()) for seed in seeds.split(',')]
        except:
            seeds = [message[message.index('-S')+2:len(message)]]
        for i, image in enumerate(images):
            download_discord_file(image.get_attribute('href'), prompt, seeds[i])
    else:
        print(message)
        seeds = [message[match.start() + 3: match.end()] for match in re.finditer("-S [0-9]*", message)]
        seeds = seeds[1:]
        try:
            n = int(message[message.find('-n') + 3])
        except:
            n = 1
        print(seeds)
        print(n)
        assert len(seeds) == n

        download_discord_file(images[0].get_attribute('href'), prompt, 'grid')
        split_image(os.path.join('images',prompt.strip(), 'grid.png'), n, seeds)

print('Downloads sucessfuly finished')

browser.quit()