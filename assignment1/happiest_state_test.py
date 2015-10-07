import sys
from pprint import pprint
import json
import re
from collections import Counter


def main():

    afinnfile = open(sys.argv[1])
    sent_scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        sent_scores[term] = int(score)

    outputfile = open(sys.argv[2],'r')
    lines = outputfile.readlines()

    states_in_tweets = []
    state_tweet_scores = {}
    for line in lines:
        line_dict = json.loads(line)
        try:
            tweet = line_dict['text']
            country = line_dict['place']['country']
        except (KeyError, TypeError):
            continue

        clean_tweet = re.sub(r"[:/,!?*&@#$%_.-]", "", tweet.lower())
        tweet_words = re.findall(r"[\S]+", tweet)
        tweet_score = 0
        # states_in_tweets = []

        # pprint(line_dict)

        if line_dict['place']['country'] != u'United States': # and tweet['place']['full_name'] is None:
            # print line_dict['place']['country']
            continue
        else:
            if line_dict['place']['country'][-2:] not in states_in_tweets:
                states_in_tweets.append(line_dict['place']['full_name'][-2:])
            for word in tweet_words:
                if word in sent_scores:
                    tweet_score += sent_scores[word]

        tweet_state = line_dict['place']['full_name'][-2:]
        state_tweet_scores[tweet_state] = tweet_score

    # pprint(state_tweet_scores)
    state_score_dict = {}
    for state in states_in_tweets:
        state_score = 0
        if state not in state_tweet_scores:
            continue
        else:
            state_score += state_tweet_scores[state]
            # print state, state_score
        state_score_dict[state] = state_score

    print max(state_score_dict.iterkeys(), key = (lambda key: state_score_dict[key]))


if __name__ == '__main__':
    main()