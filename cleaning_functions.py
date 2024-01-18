#THIS MODULE CONTAINS ALL FUNCTIONS TO PROCESS AND CLEAN TEXT

from unidecode import unidecode
import re
import spacy

def clean_tweet (tweet):
    #FIND AND CLEAN NON-DESIRED CONTENT
    link=r"http[s]?:\/\/[\w.\/]+"
    mentions=r"@[^\s]+"
    hashtag=r"#[^\s]+"
    text_without_link=re.sub(link,"",remove_emoji(tweet))
    text_without_mentions=re.sub(mentions,"",text_without_link)
    text_without_hashtag=unidecode(re.sub(hashtag,"",text_without_mentions))
    text_without_hashtag=re.sub(r"[^A-Za-z\u00F1\s\d,!?]+","",text_without_hashtag)
    processed_text=re.sub(r"RT","",text_without_hashtag).lower()
    return processed_text

def tokenize_text (cleaned_text):
    nlp=spacy.load("es_core_news_md")
    doc=nlp(cleaned_text)
    processed_tweet_list=[token.lemma_.lower() for token in doc if (not token.is_stop and len(token.text)>2 and token.is_alpha) ]
    return processed_tweet_list #RETURNS A LIST OF THE RELEVANT WORDS OF A TWEET

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001F923"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)







