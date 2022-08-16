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



