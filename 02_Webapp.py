#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# Sample image URLs (replace these with your own image URLs)
image_urls = [
    "https://lh3.googleusercontent.com/cMrIuo2PQ7bFuEA2LyoXN_-eYVBl1ErczKh3YXD7kjXOYNcaMO8FhkYqj149oDwvGQL8y7cAX77v9PH_iHVq7QmKqtmLAC65zJsWVmunLOtzamg=w960-rj-nu-e365",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnobTkkdIo8625wgyG0M1Y9uwBatStpG1IRA&usqp=CAU",
    "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/68/b4/bc/kakao-travellers-inn.jpg?w=700&h=-1&s=1",
    # Add more image URLs as needed
]

st.title("Image Safety Comparison")

# Iterate through pairs of images
for i in range(len(image_urls)):
    for j in range(i + 1, len(image_urls)):
        st.write(f"**Pair {i}-{j}:**")
        
        col1, col2 = st.columns(2)
        
        # Display the first image on the left
        with col1:
            st.image(image_urls[i], use_column_width=True, caption=f"Image {i}")
            choice_1 = st.checkbox("Safer - Image {i}", key=f"choice_{i}_{j}_1")
            
        # Display the second image on the right
        with col2:
            st.image(image_urls[j], use_column_width=True, caption=f"Image {j}")
            choice_2 = st.checkbox("Safer - Image {j}", key=f"choice_{i}_{j}_2")
        
        if choice_1 and not choice_2:
            st.write(f"Image {i} is considered safer.")
        elif choice_2 and not choice_1:
            st.write(f"Image {j} is considered safer.")
        elif choice_1 and choice_2:
            st.write("Both images are considered equally safe.")
        else:
            st.write("No selection made.")

st.write("Thank you for participating in the survey!")


# In[ ]:




