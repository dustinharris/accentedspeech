# Accented Speech
Accented speech processing for machine learning models.

# Table of Contents
1. [Project Idea](README.md#project-idea)
2. [Tech Stack](README.md#tech-stack)
3. [Data Source](README.md#data-source)
4. [Engineering Challenges](README.md#engineering-challenges)
5. [Business Value](README.md#business-value)
6. [System Architecture](README.md#system-architecture)
7. [MVP](README.md#mvp)
8. [Stretch Goals](README.md#stretch-goals)
9. [Contact](README.md#contact)

# Project Idea

Accented speech processing for machine learning models.

# Tech Stack

1. Stream data from input sources through Kafka
2. Store raw input in S3
3. Process data in Spark (standardize bitrate, sampling)
4. Store processed audio data in S3
5. Pass samples to Mechanical Turk for transcription
6. Retrieve responses from Mech Turk with Kafka
7. Relate transcription to audio in Spark
8. Store as audio/transcription pair in S3

# Data Source

Mozilla Common Voice Dataset
* https://voice.mozilla.org/en/datasets
* 22GB, 803 hours, 33, 541 voices

English speech recognition training corpus from TED talks
* http://www.openslr.org/7/
* 21G, TED-LIU: Transcription of all ted talk audio

Large-scale (1000 hours) corpus of read English speech 
* www.openslr.org/12/
* 60 GB, 1000 hours of speech based on read audiobooks

Recordings of African Accented French speech
* http://www.openslr.org/57/
* 1.8 G, Recordings of African Accented French, 22 hours

# Engineering Challenges

* Audio sampling and standardization
* Conversion from binary to ML dataset

# Business Value

* "To learn different ways of speaking, the AI needs a diverse range of voices--and experts say it's not getting them because too many of the people training, testing and working with the systems all sound the same. That means accents that are less common or prestigious end up more likely to be misunderstood, met with silence or the dreaded, "Sorry, I didn't get that."
* "In one study that compared what Alexa thought it heard versus what the test group actually said, the system showed that [non-native accented] speech...showed about 30 percent more inaccuracies."
* "That language divide could present a huge and hidden barrier to the systems that may one day form the bedrock of modern life. Now run-of-the-mill in kitchens and living rooms, the speakers are increasingly being used for relaying information, controlling devices and completing tasks in workplaces, schools, banks, hotels and hospitals."

Source: [Alexa does not understand your accent](https://www.washingtonpost.com/graphics/2018/business/alexa-does-not-understand-your-accent/?noredirect=on&utm_term=.5982731d9770)

# System Architecture

![System Architecture Diagram](https://github.com/dustinharris/accentedspeech/blob/master/img/sys-architecture.PNG)

# MVP

1. Stream data from input sources through Kafka
2. Store raw input in S3
3. Process data in Spark (standardize bitrate, sampling, unstrutctured dataset)
4. Store processed audio data in S3

# Stretch Goals

1. Mechanical turk integration
2. Structured dataset creation
3. User-submitted audio

# Contact
Reach out to dustin.harris@outlook.com with any questions.