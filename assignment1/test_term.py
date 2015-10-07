import sys
from pprint import pprint
import json
import re

def main():
    afinnfile = open(sys.argv[1])
    sent_scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        sent_scores[term] = int(score)

    outputfile = open(sys.argv[2],'r')
    lines = outputfile.readlines()

    
    tweet_score_dict = {}
    non_sent_words_tweet_scores = {}
    non_sent_words_list = []
    for line in lines:
        line_dict = json.loads(line)
        try:
            tweet = line_dict['text']
        except KeyError:
            continue
        # if line_dict['lang'] != u'en':
        #     continue
        # else:
            # print tweet
        clean_tweet = re.sub(r"[:/,!?*&@#$%_.-]", "", tweet.lower())
        tweet_words = re.findall(r"[\S]+", tweet)
        tweet_score = 0
        non_sent_words = {}
        for word in tweet_words:
            if word in sent_scores:
                tweet_score += sent_scores[word]
                # print "this is the sent word: %s and score: %d" % (clean_word, tweet_score)
            else:
                # print "this is the non sent word %s" % clean_word
                non_sent_words[word] = 0
                if word not in non_sent_words_list:
                    non_sent_words_list.append(word)

        tweet_score_dict[clean_tweet] = tweet_score
        for key in non_sent_words:
            non_sent_words_tweet_scores[key] = tweet_score

    # pprint(type(non_sent_words_tweet_scores))
    # print type(non_sent_words_tweet_scores.keys()[0])
    # pprint(non_sent_words_list)

    for word in non_sent_words_list:
        word_score = 0
        if word not in non_sent_words_tweet_scores:
            continue
        else:
            word_score += non_sent_words_tweet_scores[word]
            print word, word_score

    # for word in non_sent_words:
    #     non_sent_word_score = 0
    #     for tweet in tweet_score_dict:
    #         if word in tweet:
                # print "TWEET: %s , WORD: %s" % (tweet, word)
                # print clean_word
                # non_sent_word_score += tweet_score_dict[tweet]
                # print non_sent_word_score



if __name__ == '__main__':
    main()