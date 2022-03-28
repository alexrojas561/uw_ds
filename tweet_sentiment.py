import sys
import json


def hw():
    print('Hello, world!')

def lines(file):
    print(str(len(file.readlines())))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    lines(tweet_file)

    afinnfile = open('AFINN-111.txt')

    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweets = []
    with open('output.json', 'r') as myfile:
        for line in myfile:
            tweets.append(json.loads(line))

    total_sent = []

    for i in tweets:
        words = i['data']['text'].split(' ')
        sent = [scores.get(j) for j in words]
        total_sent.append(sum(filter(None, sent)))

    print(total_sent) 

if __name__ == '__main__':
    main()
