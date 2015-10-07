import sys
from pprint import pprint
import json
import re
from collections import Counter

def main():
    outputfile = open(sys.argv[1],'r')
    lines = outputfile.readlines()

    all_terms = []
    for line in lines:
        line_dict = json.loads(line)
        try:
            tweet = line_dict['text']
        except KeyError:
            continue
        if line_dict['lang'] != 'en':
            continue
        else:
            # print tweet
            tweet_words = re.findall(r"[\S]+", tweet)
            for word in tweet_words:
                clean_word = re.sub(r"[:/,!?*&@#$%_.-]", "", word.lower())
                all_terms.append(clean_word)
    term_count = Counter(all_terms)

    for term in all_terms:
        print term, float(term_count[term]) / float(len(all_terms))

if __name__ == '__main__':
    main()