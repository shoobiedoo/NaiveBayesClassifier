import datapoint
from random import shuffle


class NaiveBayes:
    def __init__(self, filename):
        self.points = list()
        f = open(filename, encoding='utf-8', errors='ignore')
        lines = f.readlines()
        for line in lines:
            self.points.append(datapoint.DataPoint(line))

        shuffle(self.points)
        self.training_points = self.points[:int(len(self.points)*0.8)]
        self.test_points = self.points[int(len(self.points)*0.8):]

        self.positive_sentiment = dict()
        self.negative_sentiment = dict()
        self.count_ps = 0
        self.count_ns = 0

        self.tp = list()
        self.tn = list()
        self.fp = list()
        self.fn = list()

    def train(self):
        for point in self.training_points:
            if point.sentiment == 'pos':
                self.count_ps += 1
                for word in point.words:
                    try:
                        self.positive_sentiment[word] += 1
                    except:
                        self.positive_sentiment[word] = 1
            else:
                self.count_ns += 1
                for word in point.words:
                    try:
                        self.negative_sentiment[word] += 1
                    except:
                        self.negative_sentiment[word] = 1

        for word, count in self.positive_sentiment.items():
            count /= self.count_ps
        for word, count in self.negative_sentiment.items():
            count /= self.count_ns
        self.count_ps /= (self.count_ns + self.count_ps)
        self.count_ns /= (self.count_ns + self.count_ps)

    def test(self):
        for point in self.test_points:
            score_p = self.count_ps
            score_n = self.count_ns
            for word in point.words:
                try:
                    score_p *= self.positive_sentiment[word]
                except:
                    pass
                try:
                    score_n *= self.negative_sentiment[word]
                except:
                    pass
            if score_p > score_n:
                if point.sentiment == 'pos':
                    self.tp.append(point)
                else:
                    self.fp.append(point)
            else:
                if score_p == score_n:
                    if point.sentiment == 'pos':
                        self.tp.append(point)
                    else:
                        self.tn.append(point)
                else:
                    if point.sentiment == 'pos':
                        self.fn.append(point)
                    else:
                        self.tn.append(point)
