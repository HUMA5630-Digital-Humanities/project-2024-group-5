import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

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

senti0 = pd.read_csv(r"database/sentiment0.csv")
senti1 = pd.read_csv(r"database/sentiment1.csv")
heat = pd.read_csv(r"database/heat.csv")

def new_period(input):
    if input == "baseline":
        return "baseline"
    elif input == "2020":
        return "MMXX"
    elif input == "2021":
        return "MMXXI"
    elif input == "2022":
        return "MMXXII"
    elif input == "2023":
        return "MMXXIII"
    elif input == "2024":
        return "MMXXIV"
    
senti0["time"] = senti0["period"].apply(new_period)
senti1["time"] = senti1["period"].apply(new_period)

text0 = """
**I also explored the sentiment expressed by 2020s pop music lyrics. I specially added 
a baseline dataset which contains around 550 English pop songs releasd between 2017 and 2019 
to deliver more information.**
"""

text1 = """
**I employed [TextBlob](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis) 
to quantify the sentiment contained in the lyrics. The quantified sentiment by TextBlob consists 
of 2 dimensions: polarity and subjectivity. :orange[Polarity] ranges from -1 to 1, and -1 means 
'extremely negative' while 1 means 'extremely positive'. :green[Subjectivity] ranges from 0 to 1, 
and 0 means 'only telling facts' while 1 means 'only expressing opinions'.**
"""

text2 = """
**With the help of [plotly](https://plotly.com/python/), I then converted the quantified sentiment 
into interactive figures, which means for all the figures in this page, you can hover your mouse 
over a certain figure element and a text bubble will pop up, displaying some detailed information.**
"""

text3 = """
**With 17-19 pop songs as the reference, Figure 1 and 2 show the distribution of lyrics polarity 
and subjectivity scores of all the pop songs included in my sample from 2020 to 2024 ('X' marks 
indicate the median values), while Figure 3 maps the lyrics sentiment of 2020s pop music using 
average polarity and subjectivity scores.**
"""

text4 = """
**In respect of lyrics, it seems that more 2020s pop songs tend to be emotionally positive, 
while the proportions of 'more telling facts' and 'more expressing opinions' are basically 
equal, and these patterns can also be observed in the baseline group.**
"""

text5 = """
**Compared to the baseline group, the average polarity score fell significantly in 2020, and 
I believe COVID-19 depressed pop music artists is a strong hypothesis for this. In the subsequent 
years, a fluctuation of average polarity score can be observed, which may be associated with the 
uncertainty in the development of the global health emergency as well as the increasingly complex 
and tense world situation. These issues may have also led the pop music artists to lay more 
emphasis on the genuineness or reality when creating music in 2020s, since the average subjectivity 
scores for 2020s are all lower than that for the baseline group, although there is difference 
in degree.**
"""

text6 = """
**Figure 4 and 5 show the variation of polarity and subjectivity scores through all the tracks 
within 18 albums handpicked by me (3 albums for the baseline and each year in 2020s). These 
handpicked albums are all complete, which means not any tracks from them were excluded from my 
sample due to the reasons I mentioned in the home page.**
"""

st.subheader(":rainbow[Section 2: Sentiment Analysis]", anchor=False, divider="rainbow")

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text0)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text1)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text2)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text3)

fig0 = px.strip(
    data_frame=senti0,
    x="time",
    y="polarity",
    hover_name="track_title",
    hover_data={
        "period" : True,
        "album_info" : True,
        "time" : False
        },
    range_y=[-1.05, 1.05]
)
fig0.update_traces(
    marker=dict(
        color="crimson",
        opacity=0.3
    )
)
fig0.add_scatter(
    x=senti1["time"],
    y=senti1["pmedian"],
    line=dict(
        color="lightpink",
        dash="dash"),
    marker=dict(
        color="lightpink",
        size=9,
        symbol="x"
    ),
    mode="lines+markers",
    hoverinfo="skip"
)
fig0.update_layout(
    plot_bgcolor="snow",
    showlegend=False,
    title=dict(
        font=dict(color="grey"),
        text="Figure 1"
    )
)
st.plotly_chart(fig0, use_container_width=True)

fig1 = px.strip(
    data_frame=senti0,
    x="time",
    y="subjectivity",
    hover_name="track_title",
    hover_data={
        "period" : True,
        "album_info" : True,
        "time" : False
        },
    range_y=[-0.05, 1.05]
)
fig1.update_traces(
    marker=dict(
        color="royalblue",
        opacity=0.3
    )
)
fig1.add_scatter(
    x=senti1["time"],
    y=senti1["smedian"],
    line=dict(
        color="deepskyblue",
        dash="dash"),
    marker=dict(
        color="deepskyblue",
        size=9,
        symbol="x"
    ),
    mode="lines+markers",
    hoverinfo="skip"
)
fig1.update_layout(
    plot_bgcolor="snow",
    showlegend=False,
    title=dict(
        font=dict(color="grey"),
        text="Figure 2"
    ),
    yaxis=dict(
        tickmode="array",
        tickvals=[0, 0.25, 0.5, 0.75, 1]
    )
)
st.plotly_chart(fig1, use_container_width=True)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text4)

fig2 = px.scatter(
    data_frame=senti1,
    x="pmean",
    y="smean",
    color="period",
    hover_name="period",
    hover_data={"period" : False},
    labels={
        "pmean" : "average_polarity",
        "smean" : "average_subjectivity"
    }
)
fig2.update_traces(
    marker=dict(
        size=12,
        symbol="star-diamond"
    )
)
fig2.update_layout(
    plot_bgcolor="snow",
    title=dict(
        font=dict(color="grey"),
        text="Figure 3"
    ),
    xaxis=dict(showgrid=True)
)
st.plotly_chart(fig2, use_container_width=True)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text5)

with st.chat_message(name="message", avatar="🧚‍♂️"):
    st.markdown(text6)

fig6 = go.Figure(
    data=go.Heatmap(
        x=heat["track_order"],
        y=heat["album_info"],
        z=heat["polarity"],
        zmax=1,
        zmid=0,
        zmin=-1,
        colorscale="RdBu",
        reversescale=True,
        colorbar=dict(
            orientation="h",
            outlinecolor="white",
            thickness=15,
            title=dict(
                text="polarity",
                side="top"
            )
        ),
        customdata=np.stack((heat["period"], heat["track_title"]), axis=-1),
        hovertemplate=
            "<b>album_info</b>: %{y}<br>" +
            "<b>period</b>: %{customdata[0]}<br>" +
            "<b>track_order</b>: %{x}<br>" + 
            "<b>track_title</b>: %{customdata[1]}<br>" +
            "<b>polarity</b>: %{z}<br>" +
            "<extra></extra>",
        hoverongaps=False
    )
)
fig6.update_layout(
    plot_bgcolor="palevioletred",
    title=dict(
        font=dict(color="grey"),
        text="Figure 4"
    ),
    xaxis=dict(
        scaleanchor="y", 
        showticklabels=False,
        ticks=""
        ),
    yaxis=dict(showgrid=False)
)
st.plotly_chart(fig6, use_container_width=True)

fig9 = go.Figure(
    data=go.Heatmap(
        x=heat["track_order"],
        y=heat["album_info"],
        z=heat["subjectivity"],
        zmax=1,
        zmid=0.5,
        zmin=0,
        colorscale="Greens",
        reversescale=False,
        colorbar=dict(
            orientation="h",
            outlinecolor="white",
            thickness=15,
            title=dict(
                text="subjectivity",
                side="top"
                )
        ),
        customdata=np.stack((heat["period"], heat["track_title"]), axis=-1),
        hovertemplate=
            "<b>album_info</b>: %{y}<br>" +
            "<b>period</b>: %{customdata[0]}<br>" +
            "<b>track_order</b>: %{x}<br>" + 
            "<b>track_title</b>: %{customdata[1]}<br>" +
            "<b>subjectivity</b>: %{z}<br>" +
            "<extra></extra>",
        hoverongaps=False
    )
)
fig9.update_layout(
    plot_bgcolor="saddlebrown",
    title=dict(
        font=dict(color="grey"),
        text="Figure 5"
    ),
    xaxis=dict(
        scaleanchor="y", 
        showticklabels=False,
        ticks=""
        ),
    yaxis=dict(showgrid=False)
)
st.plotly_chart(fig9, use_container_width=True)