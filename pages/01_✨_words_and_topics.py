import streamlit as st
import pandas as pd

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

topics = pd.read_csv(r"database/topics.csv")

text0 = """
**:rainbow[Topic 1: Senses and Perception]  
The words in this list are related to sensory experiences such as touch and taste. 
The topic could revolve around how these senses contribute to our understanding 
of the world and our memories.**
"""

text1 = """
**:rainbow[Topic 2: Time and Change]  
This list contains words related to time, such as today and tomorrow. 
It also includes words like round and wind, which can be associated with cyclical 
or changing patterns. The topic could explore themes of temporality, the passage of time, 
and the inevitability of change.**
"""

text2 = """
**:rainbow[Topic 3: Emotions and Places]  
The words in this list evoke emotions (sadness, heaven) and places (beach, city, town). 
The topic could focus on the emotional landscape of different locations or 
explore how places can shape our feelings and experiences.**
"""

text3 = """
**:rainbow[Topic 4: Power and Control]  
The words in this list suggest themes of power, control, and conflict. 
Words like fight, stage, and flight indicate struggles and the exercise of authority. 
The topic could delve into power dynamics, personal or societal control, 
and the consequences of seeking power.**
"""

text4 = """
**:rainbow[Topic 5: Existential Questions]  
This list contains words related to existential themes and introspection. 
Words like truth, silence, loneliness, and thought hint at philosophical inquiries 
and personal reflection. The topic could explore questions of existence, truth, 
and the search for meaning.**
"""

text5 = """
**:rainbow[Topic 6: Urban Life and Relationships]  
The words in this list are associated with urban settings, relationships, and emotions. 
The topic could focus on the complexities of city life, the dynamics of relationships, 
and the juxtaposition of light and darkness in urban environments.**
"""

text6 = """
**:rainbow[Topic 7: Desire and Temptation]  
The words in this list revolve around desire, temptation, and moral struggles. 
Words like sin, desire, and kiss suggest themes of longing and forbidden desires. 
The topic could explore the human experience of desire, 
the consequences of giving in to temptation, or the nature of sin.**
"""

text7 = """
**:rainbow[Topic 8: Passion and Obsession]  
This list includes words related to intense emotions, infatuation, and obsession. 
Words like crush, obsession, and infatuation point to themes of overwhelming passion. 
The topic could delve into the nature of obsession, the effects of intense emotions, 
or the blurred lines between love and obsession.**
"""

text8 = """
**:rainbow[Topic 9: Loss and Resilience]  
The words in this list evoke themes of loss, farewell, and strength. 
Words like goodbye, waste, and enemy suggest challenges and the need for resilience. 
The topic could explore the human capacity to cope with loss, the process of healing, 
or the strength found in adversity.**
"""

text9 = """
**:rainbow[Topic 10: Mystery and Intrigue]  
The words in this list hint at mystery, danger, and secrets. 
Words like dark, danger, and idea suggest a sense of intrigue and unknown. 
The topic could explore themes of mystery, hidden truths, or the allure of the unknown.**
"""

text10 = """
**Reading this section, you are going to gain some knowledge about what 2020s pop songs mainly talk about.**
"""

text11 = """
**I [generated a wordcloud](https://amueller.github.io/word_cloud/index.html) and conducted topic 
modeling with the lyrics I had scraped. To achieve better performance, I processed the lyrics 
beforehand. I first diced the lyrics into words, picked out all the nouns, and lemmatized these 
nouns with [Stanza](https://github.com/stanfordnlp/stanza). Then I eliminated all the 
[curse words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words). 
Finally, I counted the frequencies of all the remaining words and excluded those words of which 
the frequency z-scores were not between -3 and 3 (indicating these words occurred too few/many times).**
"""

text12 = """
**Please activate the toggle below to check the wordcloud of the 2020s pop songs' lyrics. 
Words with larger size occur more times in my sample. The shape and color of this wordcloud 
come from an [earth photo](https://en.wikipedia.org/wiki/File:Earth_Western_Hemisphere_transparent_background.png).**
"""

text13 = """
**I detected the topics of 2020s pop music with the 
[LDA model from Gensim](https://radimrehurek.com/gensim/models/ldamodel.html). 
To settle on a proper number of topics, I tried values from 2 to 10, and the coherence score 
hit the highest when the number of topics was 10. For each topic, the corresponding words were 
sorted by their possibilities of occurrence in descending order, 
and I kept the top 20 words for each topic.**
"""

text14 = """
**I sought help from [OpenAI](https://itsc.hkust.edu.hk/services/it-infrastructure/azure-openai-api-service) 
to interpret these 10 lists of words. You can activate the toggle below to check the model and prompt I used.**
"""

text15 = """
**Please check the 20 words for each of the 10 topics as well as the interpretations 
generated by LLM with the selectbox below. You may notice that some of the words are 
just nonsense, such as 't' in Topic 1 and 'ba' in Topic 4, which can result from the 
lemmatization and calls for further optimization.**
"""

code = """
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = 'https://hkust.azure-api.net',
  api_version = '2023-05-15',
  api_key = '<my key>'
)

def get_response(message, instruction):
    response = client.chat.completions.create(
		model = 'gpt-35-turbo',
        temperature = 0.5,
        messages = [
            {'role': 'system', 'content': instruction},
            {'role': 'user', 'content': message}
        ]
    )
    print(response.usage)
    return response.choices[0].message.content

message = f'''There are 10 lists and each of these lists contains 20 English words: {lists_words}.
Now, for each list of words, if the 20 words appear in one same piece of literature, what will the topic be?
Please remember, every topic should be a word or a phrase.
When giving topics, please be accurate, and distinguish each topic from the others as far as possible.
Please also explain your decisions. Thanks a lot!'''
instruction = 'You are a professor in contemporary literature and culture.'

print(get_response(message, instruction))
"""

st.subheader(":rainbow[Section 1: Words & Topics]", anchor=False, divider="rainbow")

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text10)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text11)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text12)

on0 = st.toggle(label=":grey[*Show the wordcloud.*]")

if on0:
    st.image(r"database/cloud.png", use_column_width=True)

st.divider()

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text13)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text14)

on1 = st.toggle(label=":grey[*Show the code block.*]")

if on1:
    st.code(code, language="python")

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text15)

option = st.selectbox(
    label="Select a topic to check the corresponding words and interpretation.",
    options=["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5",
             "Topic 6", "Topic 7", "Topic 8", "Topic 9", "Topic 10"]
)

words = list(topics[option].values)

rows = [words[0:5], words[5:10], words[10:15], words[15:20]]

target = pd.DataFrame(rows, columns=[option, "", " ", "  ", "   "])

st.dataframe(target, use_container_width=True, hide_index=True)

with st.container(border=True):

    if option == "Topic 1":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text0)

    elif option == "Topic 2":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text1)

    elif option == "Topic 3":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text2)

    elif option == "Topic 4":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text3)

    elif option == "Topic 5":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text4)

    elif option == "Topic 6":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text5)

    elif option == "Topic 7":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text6)

    elif option == "Topic 8":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text7)

    elif option == "Topic 9":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text8)

    elif option == "Topic 10":
        with st.chat_message(name="explanation", avatar="🤖"):
            st.markdown(text9)