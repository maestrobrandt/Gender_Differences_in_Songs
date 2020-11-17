 #!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 1600px;
        padding-top: 5rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 10rem;
    }}
    .reportview-container .main {{
        color: blue;
        background-color: white;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

import numpy as np
import pandas as pd

plot_topic_df = pd.read_csv('plot_topic_df.csv')
copy = plot_topic_df.copy()
copy.Song.drop_duplicates(inplace = True)
Songs = copy['Song']


Numbers = range(1,6)

st.title("Different Gender Song Recommender App")
Name_of_Song = st.selectbox("Song Title", Songs)
N_of_Recs = st.selectbox("Number of Recommended Songs", Numbers)

button_clicked = st.button("Recommend Songs")


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import pairwise_distances
from sklearn.decomposition import PCA
pca = PCA()

import nltk
nltk.download('stopwords')

stop_words = set(nltk.corpus.stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '/']) 
stop_words.update(['oh', 'la', 'na', 'ooh', 'doo', 'dee', 'hoo', 'hee', 'wah', 'di', 'da', 'yeah']) 



def recommend_artist(given_song, num_recs = 3, metric='euclidean'):
    if plot_topic_df[plot_topic_df.Song == str(given_song[0])].Gender.item() == 'Male':
        to_recommend = plot_topic_df[plot_topic_df.Gender == 'Female']
    else:
        to_recommend = plot_topic_df[plot_topic_df.Gender == 'Male']
        
    to_recommend = pd.concat([to_recommend, plot_topic_df[plot_topic_df.Song == str(given_song[0])]], ignore_index = True)
    
    to_recommend.drop_duplicates(subset=['Lyrics'], inplace = True)
    
    cv = CountVectorizer(stop_words = stop_words, min_df = 0.01, ngram_range = (1, 2))
    lyrics = to_recommend.Lyrics
    to_recommend_cv_lyrics = cv.fit_transform(lyrics)
    lyrics_df = pd.DataFrame(to_recommend_cv_lyrics.toarray(), columns = cv.get_feature_names())
    lyrics_df_pca = pca.fit_transform(lyrics_df)
    
    dists = pairwise_distances(lyrics_df_pca, metric=metric)
    dists = pd.DataFrame(data=dists, index=to_recommend.Song, columns=to_recommend.Song)
    
    songs_summed = dists[given_song].sum(axis=1)
    songs_summed = songs_summed.sort_values(ascending=True)
    
    ranked_songs = songs_summed.index[~songs_summed.index.isin(given_song)]
    ranked_songs = ranked_songs.tolist()
    
    recommendations = ranked_songs[:num_recs]

    
    df_eval = to_recommend.copy()

    df_eval['rec_label'] = np.where(df_eval.Song.isin(given_song), 'Like',
                                    np.where(df_eval.Song.isin(recommendations), 'Recommended',
                                             'Other'))
    
        
    df_eval = df_eval[df_eval.rec_label.isin(['Recommended'])]
    
    return df_eval



Table = recommend_artist([Name_of_Song], N_of_Recs)
Table.reset_index(inplace = True)

Final_table = Table[['Band', 'Song', 'Lyrics']] 

st.header("Table of Recommended Songs")
st.table(Final_table)


from wordcloud import WordCloud
import matplotlib.pyplot as plt

fig = plt.figure( figsize= (20, 10))
for index, row in Table.iterrows():
    lyrics = row['Lyrics']
    ax = fig.add_subplot(1, N_of_Recs,index+1)
    wordcloud = WordCloud(background_color="white",mask=None,\
                        max_font_size=70,min_font_size=1,prefer_horizontal=0.9,
                        contour_width=5,contour_color='black').generate(lyrics)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    ax.set_title(row['Band'] + ' - ' + row['Song'], fontsize = 14)
plt.show()

st.header("WordClouds of Recommended Songs")
st.pyplot(fig)





