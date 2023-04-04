import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# # Set up the input field for the ID
# options = ['FY', 'FY_PG', 'SY_PG','SY_UG','Final_UG']
# selected_options = st.multiselect('Select options:', options)


# # Set up the input field for the ID
# id_input = st.text_input("Enter the ID")

# # Set up the download button
# if st.button("Download Image"):
    
#     # Get the image file path from the local file system
#     image_path = f"FY/{id_input}.png"
#     # Load the image file using PIL
#     # image = Image.open(image_path)
#     with open(f"FY/{id_input}.png", "rb") as f:
#         image_data = BytesIO(f.read())
    
#     # Set up the file name for the downloaded image
#     file_name = f"{id_input}.png"
    
#     # Use Streamlit's "download_button" function to download the image
#     st.download_button(label="Download Image", data=image_data, file_name=file_name, mime="image/png")
option = st.radio("", ["FY", "SY_UG","SY_PG","TY_UG","TY_PG","Final_UG"],horizontal=True)
id_input = st.text_input("Enter the ID")

if id_input:
    if not st.session_state.get("downloaded", False):
        # Get the image data from local file
        try:
            with open(f"{option}/{id_input}.png", "rb") as f:
                image_data = BytesIO(f.read())

            # Set up the file name for the downloaded image
            file_name = f"{id_input}.png"
            
            # Use Streamlit's "download_button" function to download the image
            st.download_button(label="Download Image", data=image_data, file_name=file_name, mime="image/png")
            
            # Set the flag variable to True to indicate that the download has occurred
            st.session_state.downloaded = True
        except:
            st.write("Enter valid ID")
    else:
        st.warning("You have already downloaded the image.")