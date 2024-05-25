import streamlit as st

st.set_page_config(
     page_title="Text Analysis on 2020s Pop Music",
     page_icon="🎧",
     layout="centered",
     initial_sidebar_state="expanded",
     menu_items={
         "Get Help" : None,
         "Report a Bug" : None,
         "About" : None
     }
)

title = """
:rainbow[**Text Analysis on 2020s Pop Music**]  
:grey[**Group 5: Junwei DENG**]  
*2024 Spring Digital Humanities (HUMA 5630)*
"""

text0 = """
**Hello and welcome to the homepage of my project! 
In this project, I explored the 2020s pop music (with emphasis on the lyrics).**
"""

text1 = """
**To implement this project, I [scraped](https://github.com/dbeley/rymscraper) part of 
the top 2020s pop albums chart (2 pages/80 entries for each year in 2020s) from 
[Rate Your Music (RYM)](https://rateyourmusic.com), and I subsequently 
[scraped](https://github.com/johnwmillr/LyricsGenius) the metadata 
(containing the lyrics and other useful information) of these albums from 
[Genius](https://genius.com). After excluding all the tracks of which the lyrics were missing 
(pure instrumental tracks or the lyrics had not been contributed to Genius) 
or [the language was not English](https://github.com/pemistahl/lingua-py) 
(for the convenience of natural language processing and analysis), I got a sample 
containing more than 2800 pop singles in 2020s.**
"""

text2 = """
**RYM is a website where users can rate and write reviews for musical works, 
and visitors can customize music charts by user rating, genre, and release time. 
One thing I like about these charts is that when sorting by average rating score, 
the number of ratings will be also given weight to decide the ranks, which I believe 
can to some extent promote the representativeness of my sample in the sense of 
both music quality and music popularity.**
"""

text3 = """
**Pop may be the music genre with the most extensive global audience, which makes me 
believe that pop music lyrics can better reflect the various aspects of our society. 
Entering 2020s, the world has been more and more chaotic and obscure. 
Maybe this project can provide you with some insights about what is happening, 
especially about what people are concerned with and how people are feeling.**
"""

st.image(r"database/banner.png", use_column_width=True)

st.title(body=title, anchor=False)

st.divider()

with st.chat_message(name="intro", avatar="🧚‍♂️"):
    st.markdown(text0)

with st.chat_message(name="intro", avatar="🧚‍♂️"):
    st.markdown(text1)

with st.chat_message(name="intro", avatar="🧚‍♂️"):
    st.markdown(text2)

with st.chat_message(name="intro", avatar="🧚‍♂️"):
    st.markdown(text3)