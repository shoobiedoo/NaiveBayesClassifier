import string


class DataPoint:
    def __init__(self, data):
        self.category = data.split(' ')[0]
        self.sentiment = data.split(' ')[1]
        self.doc_id = data.split(' ')[2]
        self.words = self.get_unique_words(data)
        self.remove_punctuation()
        self.data = data

    def __repr__(self):
        return self.doc_id

    def __str__(self):
        return self.doc_id

    @staticmethod
    def get_unique_words(data):
        words = data.split(' ')
        return list(set(words[3:]))

    def remove_punctuation(self):
        self.words = [''.join(c for c in s if c not in string.punctuation) for s in self.words]
        for word in self.words:
            if word is '':
                self.words.remove('')
