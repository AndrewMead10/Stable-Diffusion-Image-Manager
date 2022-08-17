import argparse
import os
import re
import sys
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
parser.add_argument('-C', '--captcha', type=bool, nargs='?', default=True, const=False,
                    required=False, help='Use if there is a captcha detected during login')
args = parser.parse_args()


email = args.email
password = args.password

opts = Options()
opts.headless = args.captcha
opts.add_argument("--log-level=3")
print('Loading Chrome Driver')
print('')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
browser.get('https://discord.com/login')
email_element = browser.find_element_by_name('email')
email_element.send_keys(email)

password_element = browser.find_element_by_name('password')

password_element.send_keys(password)

password_element.submit()

time.sleep(2)
should_exit = False

if args.captcha:
    try:
        captcha = browser.find_element_by_xpath("//iframe[@title='widget containing checkbox for hCaptcha security challenge']")
        print('Captcha Found, rerun using the --captcha flag to solve and continue')
        browser.quit()
        should_exit = True
    except:
        pass

if not args.captcha:
    print('Solve captcha in browser')
    input('Press Enter once submitted')

if should_exit:
    sys.exit()

# check if login was not valid
try:
    erorr = browser.find_element_by_class_name('errorMessage-1kMqS5')
    print(erorr.text[1:])
    browser.quit()
    should_exit = True
except:
    pass

if should_exit:
    sys.exit()

print('Successfully logged in')

# wait for discord profile to load
time.sleep(8)

actions = ActionChains(browser)

buttons = browser.find_elements_by_class_name(
    'iconWrapper-2awDjA:nth-child(2)')

inbox = buttons[1]

actions.move_to_element(inbox
                        ).click().perform()

# wait for inbox to load
time.sleep(2)

# load all messages in inbox
while True:
    try:
        load_more = browser.find_element_by_class_name('lookFilled-yCfaCM')
        load_more.click()
        time.sleep(2)
    except:
        break

# get all notification messages
mentions_list = browser.find_elements_by_class_name('container-iA3Qrz')

previous = open('previous.txt', 'r').read()
is_first = True

for mention in mentions_list:
    message = mention.find_element_by_class_name(
        'messageContent-2t3eCI')
    message = message.text

    # get only messages from the bot
    if message.find('Dreamt') != 0 or message.find('Dreamt') == -1:
        continue
    # check to see if we have parsed this message before, if so, we can stop
    if message == previous:
        break
    # save the first inbox message to compare against later
    if is_first:
        f = open('previous.txt', 'w')
        f.write(message)
        f.close()
        is_first = False

    # extract the prompt and remove any characters that are not allowed in folder names
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
            download_discord_file(
                image.get_attribute('href'), prompt, seeds[i])
    else:
        seeds = [message[match.start() + 3: match.end()]
                for match in re.finditer("-S [0-9]*", message)]
        seeds = seeds[1:]
        try:
            n = int(message[message.find('-n') + 3])
        except:
            n = 1
        assert len(seeds) == n

        download_discord_file(images[0].get_attribute('href'), prompt, 'grid')
        split_image(os.path.join(
            'images', prompt.strip(), 'grid.png'), n, seeds)

print('Downloads sucessfuly finished')

browser.quit()
