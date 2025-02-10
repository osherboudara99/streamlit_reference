import time
import streamlit as st
import pandas as pd
import numpy as np

# Test Element 
st.text("This is a text")
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")

st.write("This is a writer function")
def return_sentence():
    return "This is the writer function returning a value"
st.write(return_sentence())

st.markdown("""This is **markdown** _markdown_""")

st.latex("\int12xdx")

st.json("""{"data": "This is JSON Element"}""")

st.code("""
print("hello streamlit")
do = 4
                
""", line_numbers=True)

st.code("""
cout << "hello streamlit" << endl;
""", language='cpp')


# Error Element
st.success("Success")
st.error("Wrong!")
st.exception("TypeError")
st.warning("Warning")

# Input Widget
first_name = st.text_input("Enter First Name")
password = st.text_input("Enter password", type='password')
message = st.text_area('Some message')
date = st.date_input('Date Input')
appointment_time = st.time_input("Appointment Time")
age = st.number_input('value', min_value=12, max_value=120)
gender = st.radio("Gender",["Male", "Female", "Decline"])
enable = st.toggle("Enable Print Out Below")
level = st.checkbox("Are you a veteran?")


# Sliders
countries = st.selectbox("Countries", ['US', "UK", "India", "Israel"])
p_lang = st.multiselect("Programming Languages", ["Python", "C++", "Julia", "Golang"])
rating = st.slider("Rating", min_value = 0, max_value = 5)
ranking = st.select_slider("Ranking",["Intern", 'Entry', 'Junior', 'Associate', 'Senior'])


st.divider() # Adds line in app
if enable:
    st.write(f"Details: {first_name}, {password}")
    color = st.color_picker("Pick a color")
    st.write(color)



# Data Element
def load_data(data) -> pd.DataFrame:
    return pd.read_csv(data)

df = load_data('dumb.csv')
st.dataframe(df) # Can Search
st.table(df.head(2)) # Cannot

edited_df = st.data_editor(df) # Allows you to modify dataframe in app

st.json(df.to_json())


# Connection to DB
# st.connection()

# Media Element
img = st.image("serj.png", caption="SERJ TANKIAN!")
audio_file = open("Carousel.mp3", 'rb')
st.audio(audio_file.read())
# st.video()


if st.button("Take a Picture"):
    pic = st.camera_input('Take a photo below!' )
    if pic:
        with open("camera_image.png", 'wb') as f:
            f.write(pic.getbuffer()) # save picture 


# Downloads and Uploads
file_upload = st.file_uploader("Upload CSV", type="csv")
if file_upload:
    st.write(pd.read_csv(file_upload))

st.download_button("Download Text File", "hello user!")


# Status Elements
if st.button("Compute"):
    with st.spinner("Thinking"):
        time.sleep(3)
        st.write("Hello")
    

    progress_bar = st.progress(0)
    for i in range(1, 100):
        time.sleep(0.03)
        progress_bar.progress(i, text='Progressing')
    progress_bar.empty()
    st.write("Done")

    # Popup element
    st.toast("This is a toast")


# Chat Elements (LLM UI)
def stream_data(data,delay:float=0.5):
    for word in data.split():
        yield word + " "
        time.sleep(delay)

prompt = st.chat_input("Ask something")
if prompt: 
    with st.chat_message("user"):
        st.write(f"You typed {prompt}")


if st.button("Stream"):
    with st.spinner("Thinking..."):
        time.sleep(2)
        response = 'some random text to display'
        st.write_stream(stream_data(response))

# Streaming response
# Generator
# Some text or data

st.divider()
## Layouts
# Tabs
home_tab, about_tab = st.tabs(["Home", "About"])

with home_tab:
    st.subheader("This is the Home Tab")

with about_tab:
    st.subheader("This is the About Tab")
    st.dataframe(df)


# Columns
col1, col2, col3 = st.columns(3)
# Context Manager approach for columns
with col1:
    st.title("Columns 1")

col2.dataframe(df)
col2.write("this is column 2")
col3.image("serj.png", use_container_width=True)

# Container
container = st.container(border=True)
container.write("My first container")

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")


# Expander and Popover 
with st.expander("Expand"):
    st.dataframe(df)

with st.popover("Popover"):
    st.image("serj.png")

### Plots
st.area_chart(data=df, x='number', y='letter')

st.line_chart(data=df, x='number', y='letter')

st.bar_chart(data=df, x='number', y='letter')

st.scatter_chart(data=df, x='number', y='letter')

# Matplotlib
# st.pyplot(df["number"].value_counts().plot(kind="bar"))

#Plotly
# st.plotly_chart() 

#st.altair_chart()
#st.map()
#st.bokeh_chart()

st.help(st.cache_data)
st.write(dir(st))

with st.form("Form"):
    first_name = st.text_input("Enter First Name")
    password = st.text_input("Enter password", type='password')
    message = st.text_area('Some message')
    button = st.form_submit_button("Submit")


import streamlit.components.v1 as stc 

stc.html("<p> hello </p>")
# stc.iframe()

st.link_button("visit", url="https://Google.com")


# Helps process large data
# Stores copy of resource
# If you are downloaded data from elsewhere or performing lots
# Calculations, to avoid rerun, use cache
# Functions rerun if function arguments change or if code changes (while developing) 


# st.cache_data, used for anything else (calculations, loading data)

@st.cache_data
def inference(data, random = 0):
    st.write(f"{data} time:", time.time())

inference('cached')

inference("non-cached", np.random.randn(1, 2))


# st.cache_resource, used for loading a model (DL, ML, LLM)

# #Example loading pretrained model
# @st.cache_resource
# def load_model(data):
#     # Model contained in another file
#     from full_model import Net
#     st.write(time.time())
#     model = Net()
#     checkpoints = torch.load("model_path")
#     model.load_state_dict(checkpoints["model_state"])
#     return model

# model = load_model(np.random.randn(1,2)) # since random, always changing, function rerun each time



# st.session_state
# Dictionary that Retains values across reruns

st.write(st.session_state)
if "key" not in st.session_state:
    st.session_state["key"] = 1
st.write(st.session_state)

if "key" in st.session_state:
    st.session_state["key"] = 2
st.write(st.session_state)

if st.session_state["key"] == 2:
    del st.session_state["key"]
st.write(st.session_state)


st.text_input('Name', key='name_from_text_input')
st.session_state

# Slider/checbox value will cause rerun since no submit button
st.slider("My slider", 0, 10, 1, key='my_slider')
st.checkbox("Yes or No", key="my checkbox")

def form_callback():
    st.write(st.session_state['my_slider_form'])
    st.write(st.session_state['my_checkbox_form'])

# Rerun halted until submit
with st.form(key = 'my_form'):
    st.slider("My slider", 0, 10, 1, key='my_slider_form')
    st.checkbox("Yes or No", key="my_checkbox_form")
    st.form_submit_button("Submit", on_click = form_callback)


