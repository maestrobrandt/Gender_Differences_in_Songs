# Gender Differences in Songs: An Exploration of Best-Selling Song Lyrics

![Project Image](https://media-exp1.licdn.com/dms/image/C4D12AQHEdvo89pZSDw/article-cover_image-shrink_720_1280/0/1615841801803?e=1628121600&v=beta&t=hYqEzBAsPrlii1eYdUR7U2hkQ8CQ8t1DCt4Q3P3DNK8)

>Discover what different people sing about, and how to diverisfy your listening

___

### Table of Contents
- [Description](#description)
- [Introduction](#introduction)
- [Story](#story)
- [Application](#application)
- [Future Consideration](#future-consideration)
- [Author Info](#author-info)

___

## Description

This project aimed to investigate the topic differences between song lyrics written by male and female artists. The project involved using natural language processing to topic model on the song lyrics, and also included a web application that recommends songs based on lyrics written by an artist of the opposite gender.

#### Files
- The code for the project is in Gender Differences in Songs.ipynb
- The app runs in streamlit, and will requre the Spotify_API.py and Spotify_App.py files

#### Technologies
- Python
- Jupyter Notebooks
- Natural Language Processing Algorhythms
  - NMF
  - LDA
- Wordclouds
- Streamlit

___

## Introduction

It has been shown that one of the most significant factors in determining whether or not an individual will like a particular piece of music is their agency in choosing the music (Krause & North, 2017). The power to control the music we listen to is very much correlated with our enjoyment of music, and with ever-growing access to devices and streaming platforms, people are able to develop extremely personalized music tastes like never before. New genres of music emerge every year, and existing genres evolve and become increasingly complex. While exploring the musical characteristics, such as chord progressions, timbres, rhythms, and sounds, of different artists is unquestionably intriguing, I decided to investigate an element that I think often gets overlooked: lyrics. For this project, I performed topic modeling on the song lyrics from the 50 best-selling artists of all time.

Specifically, I wanted to focus on differences between male and female artists, if these differences indeed exist. Essentially, I wanted to know if men and women sing about different topics, and what those topics are. I mentioned above how people in the present day have developed more complex musical preferences than ever, but most people will still talk about their favorite music in terms of the sound; I understand that this is the essence of music, but lyrics also definitely play a role in making music what it is. Furthermore, so many people miss out on hearing new music that they would like because they are too stuck on the safe music that they already know. So, I set out to create an app that will recommend new music that has lyrics similar to those of a song you already like, but written by an artist of the opposite gender. I believe that since you will likely enjoy the recommended music, you might as well diversify your listening.

## Story

As with any data science project, I had to begin by gathering data. Of course, I needed to find a dataset with artist/band name and lyrics for each song, but, due to copyright issues, it is difficult to have a bunch of song lyrics collected in a singular public place. Still, I managed to discover a dataset from bigML. This dataset came as a big dataframe with hundreds of thousands of songs, along with the band/artist who wrote the song and the lyrics in raw text. I then focused it down to just the top 50 artists, which gave me about 15,000 songs. Once I had the data in a workable format, I ran Natural Language Processing analysis on the song lyrics. Specifically, I ran Non-Negative Matrix Factorization (NMF), which is an unsupervised machine learning technique that returns topics from the corpus of text (in this case, the song lyrics).

Since topic modeling is unsupervised, it was up to me to use my domain knowledge in music to interpret meaning from the generated topics. As this was an exploratory project, I spent a fair amount of time adjusting the number of generated topics and deciding when a topic made sense as a stand-alone idea or not. After careful consideration, I determined that song topics, at least within the top 50 best-selling artists, can be separated into just four topics: Love Songs, Heartbreak Songs, Party Songs, and Hip-hop Songs. To the right, I have given the top ten words for each topic as determined by the NMF model. For presentation purposes, I also created word clouds for each topic.

![Topics Image](https://media-exp1.licdn.com/dms/image/C4D12AQGzgwMCa6UrKw/article-inline_image-shrink_1000_1488/0/1615842642931?e=1628121600&v=beta&t=hYo55D7hsVt5N5PrKxzAonI7uFIi-bo1LBUl9vhqCQg)

![Word Clouds Image](https://media-exp1.licdn.com/dms/image/C4D12AQEcMoEtQ1nicw/article-inline_image-shrink_1000_1488/0/1615842783773?e=1628121600&v=beta&t=ausNmeDyS74O71yk1EqTLt-QE0_cznhjQtn6Mi7xp_k)

Beyond investigating the lyrical topics of songs at large, I was also interested in topical differences between genders. Therefore, I generated word clouds for lyrics written by males versus females. Interestingly, at the aggregate level, the top words were very similar, and no noticeable differences were found. When I considered the four topics, I saw that the most represented topic for males was hip-hop, while for females it was love songs. Still, other than these slight differences in the topics that were most represented for each gender, there were not any obvious differences between male and female artists. I think that this finding can largely be explained by taking into account that my dataset simply had more male than female songs overall. It can be seen that there are no clear biases one way or the other. Sure, we can see that hip hop is more common for male artists and that love songs are relatively more common for female artists (which perhaps warrants further analysis), but in general, there do not seem to be notable differences between the types of songs that males versus females sing. At first, this result was disappointing because I want to be able to show profound differences in my visualizations; however, this is actually a good finding and provides some important insights. If there is not much difference between the topics of songs written by males versus females, then there should not be such biased representation amongst the top-selling artists.

![Word Cloud Image](https://media-exp1.licdn.com/dms/image/C4D12AQENLbNwkWk1aw/article-inline_image-shrink_1000_1488/0/1615842847355?e=1628121600&v=beta&t=OTnVQ7_w4qT8v8yoMrzwsTv3BhAxe2zMq3-489dJyZo)

![Percentages Image](https://media-exp1.licdn.com/dms/image/C4D12AQGRC4nt0rWOpg/article-inline_image-shrink_1500_2232/0/1615842986331?e=1628121600&v=beta&t=wu8x2g9jBRxzozEmvVX9kZjh_j1fBE40YL65nPfTABs)

___


## Application

With my newfound insights, I set out to create a recommendation app that takes in a song you like, then gives you recommendations for similar songs, based on lyrics, written by someone of the opposite gender. In the app, there is a place to insert a song title; once a title is interested, the user is given recommendations of songs written by the opposite gender. So let us say that I like the song "Tiny Dancer": I type it in, click “recommend”, and then am provided with a table of three recommended songs. In this case, I see Gloria Estefan, Cher, and Barbara Streisand, the name of each song, and the lyrics. While designing the app, I also went ahead and added a feature that creates word clouds for the recommended songs; this reminds the user that these recommendations are based on lyrics alone. I hope that the app is helpful for people. Remember, the whole point is to try to expose yourself to new music that you probably would like! Maybe you do not listen to female artists very often, or you don’t listen to male artists, because you simply do not know what is out there or what you will like; this app is designed to help guide you to new experiences.

![App Demo](https://youtu.be/Whu-xZcvtQI)

___

## Future Consideration

My takeaways are threefold. First, the best-selling artists’ songs can be broken down into just four topics. This may not seem surprising for people who do not particularly enjoy pop music, but this is what my analysis revealed. Second, within the best-selling artist dataset, male and female lyrics were not notably different from each other; this surprised me a bit, but gave me more justification for creating my recommendation app. Lastly, for future consideration, I want to expand this study to a larger corpus of songs. This is challenging because lyrics are copyrighted, so it is difficult to collect them in one place, but I feel that looking at genres beyond just pop music will help me in trying to understand the differences in what people sing about. I encourage everyone to try to discover new music; since I have shown that male and female lyrics are largely similar, for example, you might as well diversify your listening.

## Author Info

- LinkedIn - [ZacharyMBrandt](https://www.linkedin.com/in/zacharymbrandt/)
- Website - [The Aspiring Music Psychologist](https://www.theaspiringmusicpsychologist.com)
- Podcast - [The Aspiring Music Psychologist](https://anchor.fm/zachary-brandt5)
