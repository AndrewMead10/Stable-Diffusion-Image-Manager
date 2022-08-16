from email.policy import default
import streamlit as st
import os

st.set_page_config(layout="wide")

prompts = os.listdir('images')

search = st.text_input('Search propmpts', '')
show_imgs = st.checkbox('Show all images/ disable dropdowns', value=False)

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
            col1, col2 = expander.columns(2)
        else:
            st.header(prompt)
            col1, col2 = st.columns(2)
        is_col1 = True
        for dir, _, imgs in folder:
            for img in imgs:
                if img == 'grid.png':
                    continue
                if is_col1:
                    col1.image(os.path.join(dir, img))
                    col1.write('Seed: {}'.format(img[:len(img)-4]))
                else:
                    col2.image(os.path.join(dir, img))
                    col2.write('Seed: {}'.format(img[:len(img)-4]))
                is_col1 = not is_col1
