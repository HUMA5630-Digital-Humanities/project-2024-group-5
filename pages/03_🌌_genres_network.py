import streamlit as st
import streamlit.components.v1 as components

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

text0 = """
**In this section, I want to show you the network of music genres appearing in my sample. 
It will take a few seconds to render the figure. This network figure is a little bit messy 
in its initial state, but it is actually interactive and can be dragged and zoomed in/out. 
You can also click on a certain node to focus on it. Please check the 
[documentation of ipysigma](https://github.com/medialab/ipysigma?tab=readme-ov-file#sigma) 
to take full advantage of the functions within this network figure.**
"""

text1 = """
**You may have realized that :rainbow[pop] is a broad concept. Currently, there are around 150 
sub-genres under :rainbow[pop] recognized by RYM, and RYM exactly tends to define musical works 
with sub-genres, rather than the major ones. It is so common that the tracks within an album come 
from different sub-genres belonging to one or even several major genres, and maybe the network 
figure below can help you better perceive the fusion within the feild of :rainbow[pop] as well as 
between :rainbow[pop] and the other music genres in 2020s.**
"""

text2 = """
**For your information, each node stands for a unique music genre, and the curve edge 
between 2 nodes means that at least 1 album in my sample has been defined by the conjunction 
of the 2 corresponding genres. Genres with larger node connect with more other genres, 
and conjunctions with thicker edge have higher frequency.**
"""

text3 = """
**I was planning to add an attribute to each genre in my sample telling whether or not 
it is :rainbow['pop-ish'] according to the genre list from RYM, but it seems that this list 
is often updated, which makes this work kind of tricky. Then I decided to adopt another way 
to accomplish this task. I first obtained the 
[word embedding vectors](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html#) 
of all the genres with 'text-embedding-ada-002' model (provided by HKUST Azure OpenAI API Service), 
and then conducted 
[KMeans clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) 
on these vectors to sort the genres into 2 categories. The genre :rainbow[pop] fell into cluster 1, 
which is now indicated with blue nodes, and those genres in the same cluster can be considered 
relatively closer to :rainbow[pop], at least in respect of connotation.**
"""

file = open(r"database/genre_network.html", "r", encoding="utf-8")

st.subheader(":rainbow[Section 3: Genres Network]", anchor=False, divider="rainbow")

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text0)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text1)

components.html(file.read(), height=500)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text2)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text3)
