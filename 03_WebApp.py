#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st

# Sample image URLs (replace these with your own image URLs)
image_urls = [
    "https://lh3.googleusercontent.com/cMrIuo2PQ7bFuEA2LyoXN_-eYVBl1ErczKh3YXD7kjXOYNcaMO8FhkYqj149oDwvGQL8y7cAX77v9PH_iHVq7QmKqtmLAC65zJsWVmunLOtzamg=w960-rj-nu-e365",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnobTkkdIo8625wgyG0M1Y9uwBatStpG1IRA&usqp=CAU",
    "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/68/b4/bc/kakao-travellers-inn.jpg?w=700&h=-1&s=1",
    # Add more image URLs as needed
]

st.title("Image Safety Comparison")

# Function to display a pair of images and get user selection
def show_image_pair(image_url_1, image_url_2):
    col1, col2 = st.columns(2)
    
    # Display the first image on the left
    with col1:
        st.image(image_url_1, use_column_width=True, caption="Image 1")
        
    # Display the second image on the right
    with col2:
        st.image(image_url_2, use_column_width=True, caption="Image 2")
        
    return st.button("Next Pair")

# Initialize variables to keep track of image pairs and survey results
current_pair = 0
total_pairs = len(image_urls) * (len(image_urls) - 1) // 2
survey_results = []

# Show image pairs one by one
while current_pair < total_pairs:
    st.write(f"**Pair {current_pair + 1}/{total_pairs}:**")
    img_index_1 = current_pair // (len(image_urls) - 1)
    img_index_2 = current_pair % (len(image_urls) - 1) + img_index_1 + 1
    
    result = show_image_pair(image_urls[img_index_1], image_urls[img_index_2])
    survey_results.append(result)
    
    current_pair += 1

st.write("Thank you for participating in the survey!")

# Display the collected survey results
st.write("Survey Results:")
for i, result in enumerate(survey_results):
    st.write(f"Pair {i + 1}: {result}")


# In[ ]:




