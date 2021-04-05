# COSC310-Friend-Chatbot 2.0
![ChatbotImage](https://s3-eu-west-1.amazonaws.com/userlike-cdn-blog/do-i-need-a-chatbot/header-chat-box.png)

## About the project
This repository contains a programming project code for a chatbot that simulates a conversation between friends. 
A specific topic about soccer and some scattered topics are covered.

## Prepare stage
before we start running this code we need to download several libraries
```bash
pip install nltk
pip install -U spacy
python -m spacy download en_core_web_lg
pip install pyspellchecker
pip install -U textblob
```

## How to run the code
run server first at the meantime run client

## Some features
1. the system can clean all punctuations in the sentence and convert sentence to lower case

2. the system can remove suffixes (e.g.playing and play) and 
convert all the words back to root form (e.g. apples and apple)

3. the system can clean all the words with not much meaning in the sentence (e.g. 'a', 'is')

4. The system can perform sentiment analysis (e.g. good and bad)

5. a simple GUI so that the user is typing into a nicer interface and can view a recent history of the conversation

6. new topics about basketball is added to improve the conversation of agent

7. a feature enables agent to give at least 5 different reasonable responses when the user enters something beyond the two topics

8. a feature enables the system to handle spelling mistakes of the words to improve the fluency of conversation

9. a feature that can show user about definition on wikipedia page of question asking about something and give a link of 
wikipedia page of it.

10. a feature that can show user the most relavent picture about the topic asking about definition from flickr

## Sample output
```bash
Input:what is chemistry??  
the science of mixing chemicals.
Definition: Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions: their composition, structure, properties, behavior and the changes they undergo during a reaction with other substances.
Here is a link from wikipedia if you still confused: https://en.wikipedia.org/wiki/Chemistry
```
```bash
Input:tell me about chemistry  
the science of mixing chemicals.
Definition: Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions: their composition, structure, properties, behavior and the changes they undergo during a reaction with other substances.
Here is a link from wikipedia if you still confused: https://en.wikipedia.org/wiki/Chemistry
```
```bash
Input:what is chemitry
the science of mixing chemicals.
```
```bash
Input:you are a good robot
Thank you!!!
```
```bash
Input:you are not a good robot
I'm sorry QAQ!
```
```bash
...
```

## GUI and Examples
<img src="https://github.com/wuyasan/COSC--310-Individual-Project/blob/cb724fd2c929107a7da6af0a3177ca4a80f565cd/avogardro.png" width="1000" height="1000">
<img src="https://github.com/wuyasan/COSC--310-Individual-Project/blob/2933320119eed1bfa2c69b96ebec595909f6adfe/chemistry.png" width="1000" height="1000">
<img src="https://github.com/wuyasan/COSC--310-Individual-Project/blob/2933320119eed1bfa2c69b96ebec595909f6adfe/computer.png" width="1000" height="1000">
