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
        tweet_words = re.findall(r"[\S]+", tweet)
        tweet_score = 0
        non_sent_words = {}
        for word in tweet_words:
            clean_word = re.sub(r"[:/,!?*&@#$%_.-]", "", word.lower())
            if clean_word in sent_scores:
                tweet_score += sent_scores[clean_word]
                # print "this is the sent word: %s and score: %d" % (clean_word, tweet_score)
            else:
                # print "this is the non sent word %s" % clean_word
                non_sent_words[clean_word] = tweet_score

        for clean_word, tweet_score in non_sent_words.iteritems():
            print clean_word, tweet_score


if __name__ == '__main__':
    main()