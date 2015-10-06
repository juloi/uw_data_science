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
        # pprint(line_dict)
        try:
            tweet = line_dict['text']
        except KeyError:
            continue
        # if line_dict['lang'] != u'en':
        #     continue
        # else:
        #     # pprint(tweet)
        tweet_words = re.findall(r"[\S]+", tweet)

        tweet_score = 0
        for word in tweet_words:
            clean_word = re.sub(r"[:/,!?*&@#$%_.-]", "", word.lower())
            if clean_word in sent_scores:
                # print clean_word, sent_scores[clean_word]
                tweet_score += sent_scores[clean_word]
        print tweet_score


if __name__ == '__main__':
    main()