import streamlit as st
import pandas as pd

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