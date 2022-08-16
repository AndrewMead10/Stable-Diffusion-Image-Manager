# Stable Diffusion Image Manager

The Stable Diffusion Image Manager is a script that goes and downloads all of the images you have generated on discord, and then gives you the ability to view them using streamlit. 

# Install

You will need to have python installed on your computer to be able to run the program.

In your terminal, navigate to the directory you want to run your code, and then run the commands:

```bash
git clone https://github.com/AndrewMead10/Stable-Diffusion-Image-Manager
cd Stable-Diffusion-Image-Manager
pip install -r requirements.txt
```

You now should have all of the necessary files and libraries to run the code.

# Usage

To download all of your images run the command:
```bash
python bot.py --email {your discord email} --password {your discord password}
```

To run the streamlit image viewer, run the command:
```bash
streamlit run streamlit_viewer.py
```

# Limitations and issues

Your inbox only holds mentions for one week, which means that any images that you created more than 7 days ago will not be downloaded. If the script fails to download your images, it is most likely due to either a bad discord email/password (the ```Successfully logged in``` message always displays as long as the bot does not crash) or you have slow internet. If your internet is slow you can increase the page loading delays by increasing the time.sleep() in bot.py. I will hopefully be rolling out fixes for both of these issues in the next day or two.



