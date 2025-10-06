import streamlit as st
from data.dynamodb_loader import retrieve_all
from utils.colour import get_font_colour

data = retrieve_all()
st.set_page_config(layout="wide")
st.title("GitHub Language Colours")

columns = st.columns(4)
i = 0

for item in data['Items']:
    col = columns[i % 4]
    language = item['language']
    colour = item['colour']
    url = item['url']

    if colour == None:
        colour = "#CCCCCC"

    font_colour = get_font_colour(colour)
    tile_html = f"""
    <a href="{url}" target="_blank" style="text-decoration: none;">
        <div style="
            background-color: {colour};
            color: {font_colour};
            padding: 40px 10px;
            border-radius: 8px;
            margin: 8px 0;
            text-align: center;
            font-weight: bold;
            font-size: 30px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        ">
            {language}<br><span style="font-size: 24px;">{colour}</span>
        </div>
    </a>
    """
    col.markdown(tile_html, unsafe_allow_html=True)
    i += 1
