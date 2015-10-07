import sys
from pprint import pprint
import json
import re
from collections import Counter
from collections import defaultdict

def main():
    outputfile = open(sys.argv[1],'r')
    lines = outputfile.readlines()

    all_hashtags = []
    for line in lines:
        line_dict = json.loads(line)
        try:
            hashtags_dict = line_dict['entities']['hashtags']
            # pprint(tweet_hashtags)
        except KeyError:
            continue

        for dict in hashtags_dict: 
            # print dict['text']
            all_hashtags.append(dict['text'])

    # print len(all_hashtags)

    hashtag_counter = Counter(all_hashtags)
    top_ten_tuples = hashtag_counter.most_common(10)

    for tag, count in top_ten_tuples:
        print "%s %d" % (tag, count)
    
    # top_ten_hashtags = defaultdict()
    # for key, value in top_ten_tuples:
    #     top_ten_hashtags[key] = value

    # print top_ten_hashtags
    # for tag, count in top_ten_hashtags.iteritems():
    #     print tag, count

if __name__ == '__main__':
    main()