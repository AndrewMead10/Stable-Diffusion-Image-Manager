from email.policy import default
import streamlit as st
import os

st.set_page_config(layout="wide")

prompts = os.listdir('images')

search = st.text_input('Search propmpts', '')
show_imgs = st.checkbox('Show all images/ disable dropdowns', value=False)
use_cols = st.checkbox('Use columns', value=True)

st.markdown(
    """
<style>
.streamlit-expanderHeader {
    font-size: large;
}
</style>
""",
    unsafe_allow_html=True,
)

for prompt in prompts:
    if search.lower() in prompt.lower() or search == '':
        folder = os.walk('images/' + prompt)
        if not show_imgs:
            expander = st.expander(prompt)
            if use_cols:
                col1, col2 = expander.columns(2)
        else:
            st.header(prompt)
            if use_cols:
                col1, col2 = st.columns(2)
        is_col1 = True
        for dir, _, imgs in folder:
            for img in imgs:
                if img == 'grid.png':
                    continue
                if use_cols:
                    if is_col1:
                        col1.image(os.path.join(dir, img))
                        col1.write('Seed: {}'.format(img[:len(img)-4]))
                        col1.download_button(label='Download', data = open(os.path.join(dir, img), 'rb').read(),
                                             file_name = prompt + '.png', mime='image/png')
                    else:
                        col2.image(os.path.join(dir, img))
                        col2.write('Seed: {}'.format(img[:len(img)-4]))
                        col2.download_button(label='Download', data = open(os.path.join(dir, img), 'rb').read(),
                                             file_name = prompt + '.png', mime='image/png')
                    is_col1 = not is_col1
                else:
                    st.image(os.path.join(dir, img))
                    st.write('Seed: {}'.format(img[:len(img)-4]))
                    st.download_button(label='Download', data = open(os.path.join(dir, img), 'rb').read(),
                                       file_name = prompt + '.png', mime='image/png')
