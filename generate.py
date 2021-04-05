import preprocessing as prep
import en_core_web_lg
import spacy
import operator
import random
import wikipediaapi
from flickr import get_urls
from PIL import Image
import requests
from io import BytesIO

ques = prep.loadCorpora()[0]


def preprocess(sentence):  # preprocess the sentence using preprocessing model
    clean = prep.cleanPunctuationAndLower(sentence)
    stemm = prep.StemmingAndLemmatization(clean)
    spell = prep.cleanStopWordsAndSpelling(stemm)
    return spell


def wordEmbedding(question):  # change all questions in the corpora to vectors and store in a list
    embeddingList = []
    nlp = en_core_web_lg.load()

    for x in range(len(question)):
        doc = nlp(preprocess(question[x]))
        pre = [doc]
        pre.append(prep.findsenti(question[x]))  # also include the sentiment 
        embeddingList.append(pre)
    return embeddingList


def generate(intputSen, doc2, answer):
    index = 0
    nlp = en_core_web_lg.load()
    doc1 = nlp(preprocess(intputSen))
    inputsenti = prep.findsenti(intputSen)
    similarity = 0
    bestlist = []
    wiki_wiki = wikipediaapi.Wikipedia('en')
    ans_url = ''
    summary = ''
    img = None

    for x in range(len(doc2)):
        if doc2[x][0].vector_norm and doc1.vector_norm:
            similarity = doc1.similarity(doc2[x][0])  # compare the input sentence and questions stored in the list

        if similarity > 0.60:
            # this is the threshold, so if this value is too high, then your input must
            # have a higher degree of similarity to the questions in the corpora
            index = x
            bestlist.append([similarity, index, doc2[x][1]])

    # to determine whether the user's question from the question list is asking about definition of something
    if (ques[index].find("what is") or ques[index].find("What is")) and ques[index].find("good") == -1:
        toSearch = prep.cleanPunctuationAndLower(ques[index])
        toSearch = ' '.join(prep.cleanSW(toSearch))  # convert question to keyword

        page = wiki_wiki.page(toSearch)  # search for wiki page of the keyword

        if page.exists():  # check if the page exists if exists get its
            ans_url = page.fullurl  # link
            summary = page.summary.split(".", 1)[0]  # use summary of the page as proper definition

            url = get_urls(toSearch, 3)  # get the links of image of keyword from flickr
            response = requests.get(url[0])
            img = Image.open(BytesIO(response.content))  # get the image from link

    if len(bestlist) == 0:
        # at least 5 different  reasonable responses when the user enters something outside the two topics
        listReply = ['Sorry your question is not included in my database', 'Sorry, I do not know how to reply that',
                     'Whoops! my brain is dead, may be next question', 'Pass that bro, I cannot remember',
                     'This question is too difficult, next question please',
                     'Your question is hard for me, sorry about that']
        replyOutsideTopic = random.choice(listReply)
        print(replyOutsideTopic)
        return replyOutsideTopic
    sortedanswer = sorted(bestlist, key=operator.itemgetter(0))

    if len(sortedanswer) == 1:
        ans = answer[sortedanswer[0][1]]
        if ans_url != '':
            ans = (answer[sortedanswer[0][1]] + "Definition: " + summary
                   + ".\nHere is a link from wikipedia if you still confused: " + ans_url)
        print(ans)

        if img is not None:
            img.show()

        return ans
    else:
        if sortedanswer[-1][0] != sortedanswer[-2][0]:
            ans = answer[sortedanswer[-1][1]]
            if ans_url != '':
                ans = (answer[sortedanswer[-1][1]] + "Definition: " + summary
                       + ".\nHere is a link from wikipedia if you still confused: " + ans_url)
            print(ans)

            if img is not None:
                img.show()

            return ans
        else:
            if abs(sortedanswer[-1][2] - inputsenti) > abs(sortedanswer[-2][
                                                               2] - inputsenti):  # if top 2 answer have same similarity, then check the sentiment.
                ans = answer[sortedanswer[-2][1]]
                if ans_url != '':
                    ans = (answer[sortedanswer[-2][1]] + "Definition: " + summary
                           + ".\nHere is a link from wikipedia if you still confused: " + ans_url)
                print(ans)

                if img is not None:
                    img.show()

                return ans
            else:
                ans = answer[sortedanswer[-1][1]]
                if ans_url != '':
                    ans = (answer[sortedanswer[-1][1]] + "Definition: " + summary
                           + ".\nHere is a link from wikipedia if you still confused: " + ans_url)
                print(ans)

                if img is not None:
                    img.show()

                return ans
