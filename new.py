import streamlit as st
import requests
from PIL import Image
from io import BytesIO
# from ldap3 import Server, Connection, SAFE_SYNC
import ldap3

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
def authenticate(user_id,password):
    
    # l = ldap.initialize('ldap://10.1.101.41/auth')
    # username =  user_id #f"uid={id},ou=People,dc=mydotcom,dc=com" 
    # password = password
    # try:
    #     l.protocol_version = ldap.VERSION3
    #     l.simple_bind_s(username, password)
    #     valid = True
    #     st.write("True")
    # except:
    #     print("error occured!")
    #     st.write("False")

    server = ldap3.Server('ldap://10.1.101.41:6000')
    with ldap3.Connection(server, auto_bind=True) as conn:
        conn.search(search_base, search_filter, attributes=attrs)
        st.write(conn.entries)

    

    # server = Server('ldap://10.1.101.41/auth:6000',use_ssl=False)
    # conn = Connection(server, user_id, password, auto_bind=True)
    # st.write(conn)

def new_authentication(mis,password):
   url = "http://210.212.183.21/auth"
   myobj = {"MIS": mis,"Password": password}
   x = requests.post(url, json = myobj)
   if(x.text == "Error: Incorrect Credentials"):
    return False
   else:
    return True
#    st.write(x.text)

option = st.radio("", ["FY", "SY_UG","SY_PG","TY_UG","TY_PG","Final_UG"],horizontal=True)
id_input = st.text_input("Enter MIS")
password_input = st.text_input("Enter moodle Password")

if id_input and password_input:
    if new_authentication(id_input, password_input):
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
        st.warning("Invalid credentials.")
