# import the necessary module
import streamlit as st

# set up the webpage
st.set_page_config(
     page_title="Pop Music Lyrics Analysis",
     page_icon="🎧",
     layout="centered",
     initial_sidebar_state="collapsed",
     menu_items={
         "Get Help" : None,
         "Report a Bug" : None,
         "About" : None
     }
)

# define the text contents with long strings
title = """
:rainbow[**Text Analysis on Pop Music Lyrics in 2020s**]  
Final Project for HUMA 5630 Digital Humanities  
:grey[Group 5]
"""

head1 = """
**:rainbow[Section 1: Topic Modeling]**
"""

head2 = """
**:rainbow[Section 2: Sentiment Analysis]**
"""

head3 = """
**:rainbow[Section 3: Word Embedding]**
"""

note0 = """🦉 *Notes:  
You can better understand this project by reading the supplementary materials  
which can be downloaded by clicking the button here* :orange[**:)**]
"""

note1 = """
🦉 *Notes:  
The words are sorted by the possibility of appearing in the corresponding topic in descending order.  
Top 20 words for each topic are listed here.*
"""

note2 = """
🦉 *Notes:  
Polarity ranges from -1 (negative sentiment) to 1 (positive sentiment).  
Subjectivity ranges from 0 (telling facts) to 1 (telling opinions).*
"""

text11 = """
🦉 **OpenAI read the words above, generated the topic names, and gave brief explanations.**  
📍 :red[Topic 1: Emotions and Sensations] - This list contains words that are associated with feelings and physical sensations such as love, heart, feel, body, skin, and cry.  
📍 :orange[Topic 2: Relationships and Intimacy] - This list contains words that are commonly associated with romantic relationships and intimacy such as love, heart, touch, home, and body.  
📍 :grey[Topic 3: Everyday Life] - This list contains words that are associated with daily life and routine such as way, home, life, care, and someone.  
📍 :green[Topic 4: Existentialism and Mortality] - This list contains words that are associated with the meaning of life and the inevitability of death such as life, world, hope, death, and feel.  
📍 :blue[Topic 5: Music and Movement] - This list contains words that are associated with music and movement such as dance, way, love, and show.  
📍 :violet[Topic 6: Social Dynamics] - This list contains words that are associated with social dynamics and interactions such as party, clique, room, and story.
"""

text21 = """
🦉 **My current findings on the basis of the figures above are:**  
📍 Generally, the sentiment expressed by 2020s pop music is slighly towards the positive end, 
and no significant difference is observed between before and after the onset of COVID-19.  
📍 In most of the included years, female artists expressed more positive sentiment in their music than male artists did.  
📍 On average, 2020s pop music stayed neutral between tell facts and expressing opinions, 
and no significant difference is observed between before and after the onset of COVID-19.  
📍 In most of the included years, female artists were more willing to express opinions in their music.  
📍 It seems that the onset of COVID-19 had made the pop music artists create more emotionally negative works 
and encouraged them to express more opinions with music.
"""

text31 = """
🦉 *Unfortunately, I have not found a proper way 
to display the visualized embeddings of music genres here. 
However, you can follow the steps as below to explore it by yourself.*  
"""

text32 = """
🦉 *A zip file will be downloaded and it consists of 2 tsv files, 
which respectively contains the vectors and the metadata of music genres.*
"""

text33 = """
🦉 *Click the 'load' button in the 'data' column 
which is on the left side of the webpage. 
I recommend using UMAP to reduce the embedding dimension 
but feel free to try the others. 
The webpage should look like the screenshots as below if successful.*
"""

# the tiltle
st.title(body=title, anchor=False)

st.markdown(note0)

with open("my_files/supp.pdf", "rb") as file:
    btn0 = st.download_button(
        label="Download the supplementary materials",
        data=file,
        file_name="project_details.pdf"
        )

st.divider()

# section 1: topic modeling
st.header(head1, anchor=False)

st.markdown(note1)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown("**:red[Topic I Words]**")
    st.markdown("**love**")
    st.markdown("**night**")
    st.markdown("**dream**")
    st.markdown("**heart**")
    st.markdown("**feel**")
    st.markdown("**world**")
    st.markdown("**body**")
    st.markdown("**water**")
    st.markdown("**way**")
    st.markdown("**ground**")
    st.markdown("**life**")
    st.markdown("**tell**")
    st.markdown("**place**")
    st.markdown("**need**")
    st.markdown("**mind**")
    st.markdown("**air**")
    st.markdown("**skin**")
    st.markdown("**cry**")
    st.markdown("**god**")
    st.markdown("**name**")
    
with col2:
    st.markdown("**:orange[Topic II Words]**")
    st.markdown("**night**")
    st.markdown("**heart**")
    st.markdown("**control**")
    st.markdown("**try**")
    st.markdown("**mine**")
    st.markdown("**boy**")
    st.markdown("**head**")
    st.markdown("**mind**")
    st.markdown("**love**")
    st.markdown("**tell**")
    st.markdown("**touch**")
    st.markdown("**show**")
    st.markdown("**home**")
    st.markdown("**feel**")
    st.markdown("**tip**")
    st.markdown("**watch**")
    st.markdown("**world**")
    st.markdown("**ride**")
    st.markdown("**body**")
    st.markdown("**way**")

with col3:
    st.markdown("**:grey[Topic III Words]**")
    st.markdown("**way**")
    st.markdown("**home**")
    st.markdown("**fall**")
    st.markdown("**life**")
    st.markdown("**feel**")
    st.markdown("**house**")
    st.markdown("**care**")
    st.markdown("**mind**")
    st.markdown("**girl**")
    st.markdown("**world**")
    st.markdown("**tell**")
    st.markdown("**call**")
    st.markdown("**someone**")
    st.markdown("**face**")
    st.markdown("**night**")
    st.markdown("**trouble**")
    st.markdown("**bottle**")
    st.markdown("**jam**")
    st.markdown("**sex**")
    st.markdown("**man**")

with col4:
    st.markdown("**:green[Topic IV Words]**")
    st.markdown("**life**")
    st.markdown("**world**")
    st.markdown("**love**")
    st.markdown("**hope**")
    st.markdown("**wish**")
    st.markdown("**honey**")
    st.markdown("**night**")
    st.markdown("**talk**")
    st.markdown("**mind**")
    st.markdown("**head**")
    st.markdown("**song**")
    st.markdown("**way**")
    st.markdown("**home**")
    st.markdown("**hair**")
    st.markdown("**end**")
    st.markdown("**eye**")
    st.markdown("**sun**")
    st.markdown("**death**")
    st.markdown("**feel**")
    st.markdown("**buttermilk**")

with col5:
    st.markdown("**:blue[Topic V Words]**")
    st.markdown("**dance**")
    st.markdown("**way**")
    st.markdown("**love**")
    st.markdown("**look**")
    st.markdown("**johnny**")
    st.markdown("**life**")
    st.markdown("**night**")
    st.markdown("**head**")
    st.markdown("**face**")
    st.markdown("**bounce**")
    st.markdown("**feel**")
    st.markdown("**guess**")
    st.markdown("**money**")
    st.markdown("**picture**")
    st.markdown("**show**")
    st.markdown("**man**")
    st.markdown("**stop**")
    st.markdown("**heal**")
    st.markdown("**street**")
    st.markdown("**mine**")

with col6:
    st.markdown("**:violet[Topic VI Words]**")
    st.markdown("**party**")
    st.markdown("**life**")
    st.markdown("**clique**")
    st.markdown("**way**")
    st.markdown("**man**")
    st.markdown("**move**")
    st.markdown("**someone**")
    st.markdown("**room**")
    st.markdown("**mind**")
    st.markdown("**change**")
    st.markdown("**hand**")
    st.markdown("**side**")
    st.markdown("**bit**")
    st.markdown("**tear**")
    st.markdown("**candy**")
    st.markdown("**story**")
    st.markdown("**girl**")
    st.markdown("**release**")
    st.markdown("**jolene**")
    st.markdown("**save**")

st.write(" ")
st.markdown(text11)

st.divider()

# section 2: sentiment analysis
st.header(head2, anchor=False)

st.markdown(note2)

st.image("my_files/plot1.png", caption="☝️ Figure 1: distribution of polarity. Bars stand for the average values.")

st.image("my_files/plot2.png", caption="☝️ Figure 2: distribution of subjectivity. Bars stand for the average values.")

st.image("my_files/plot3.png", caption="☝️ Figure 3: the map of sentiment. Xs stand for the average values.")

st.write(" ")
st.markdown(text21)

st.image("my_files/plot4.png", caption="☝️ Figure 4: variation of polarity within 20 selected albums.")

st.image("my_files/plot5.png", caption="☝️ Figure 5: variation of subjectivity within 20 selected albums.")

st.divider()

# section 3: word embedding
st.header(head3, anchor=False)

st.markdown(text31)

st.markdown("📍 **Step 1: click the buttons to download necessary files**")

st.markdown(text32)
    
with open("my_files/tsv_files.7z", "rb") as file:
    btn1 = st.download_button(
        label="Download the files for embedding visualization",
        data=file,
        file_name="emb_v.7z"
        )
    
st.markdown("📍 **Step 2: click this link and go to the embedding visualization website**")

st.page_link(
    page="https://projector.tensorflow.org/", 
    label="Embedding Projector",
    icon = "🌌"
    )

st.markdown("📍 **Step 3: upload the tsv files**")

st.markdown(text33)

st.image("my_files/screenshot0.png", caption="☝️ Screenshot 1")

st.image("my_files/screenshot1.png", caption="☝️ Screenshot 2")