# Stable Diffusion Image Manager

The Stable Diffusion Image Manager is a script that goes and downloads all of the images you have generated in the Stable Diffusion discord, split them out of their grid if needed, and then gives you the ability to view them using streamlit. 

# Install

You will need to have Chrome and python 3 installed on your computer to be able to run the program.

In your terminal, navigate to the directory you want to run your code, and then run the commands:

```bash
git clone https://github.com/AndrewMead10/Stable-Diffusion-Image-Manager
cd Stable-Diffusion-Image-Manager
pip install -r requirements.txt
```

You now should have all of the necessary files and libraries to run the code.

# Basic Usage

To download all of your images run the command:
```bash
python bot.py --email {your discord email} --password {your discord password}
```

Once the previous command has finished executing, you can view all of your images in streamlit using the command:
```bash
streamlit run streamlit_viewer.py
```

![streamlit image viewer](/demo/streamlit.PNG)

# Captcha

If there is a captcha detected, the bot will let you know. You can then rerun the command using the ```--captcha``` flag to solve the captcha yourself and then press enter in your terminal and then the bot will continue to work. Note that this will increase the loading times of pages, so you may need to increase the delay to compensate for this. *Note that you have to solve the captcha yourself, the bot cannot do it for you.*

# Other features

If you would like to see what the program is executing in the browser, run the bot with the ```--show_browser``` flag.

To increase the delay to allow for more time for pages to load, use the ```--delay {seconds}``` flag

The bot keeps track of what images you downloaded before (as long as the program does not crash/ is stopped midway through execution), so if you run it multiple times it will only download the new images for you. If you would like to redownload all of your images, all you need to do is delete eveything in the ```previous.txt``` file.

# Example

Run the program with captcha solve on, and have an extra 5 second delay
```bash
python bot.py --email example@email.com --password examplePassword --captcha --delay 5
```


# Limitations and issues

Your inbox only holds mentions for one week, which means that any images that you created more than 7 days ago will not be downloaded. If the script is giving element not found errors, this is most likely due to the page not fully loading, so increase the time the program waits for each page to load with the --delay flag. There currently is no support for grids that have 5,7, or 8 images in them, but this functionality should be added in the future. You should be able to use your phone number as a login method, but this method has not been tested so use at your own aggravation.



