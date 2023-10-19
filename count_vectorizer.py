class CountVectorizer:

    def __init__(self):
        self.vocab_ = {}
        self.feature_names_ = []

    def fit(self, documents):
        self.vocab_ = {}
        self.feature_names_ = []

        for doc in documents:
            for word in doc.split():
                word = word.lower()
                if word not in self.vocab_:
                    self.vocab_[word] = len(self.vocab_)
                    self.feature_names_.append(word)

    def transform(self, documents):
        matrix = []
        for doc in documents:
            doc_vector = [0] * len(self.vocab_)
            for word in doc.split():
                word = word.lower()
                if word in self.vocab_:
                    doc_vector[self.vocab_[word]] += 1
            matrix.append(doc_vector)

        return matrix

    def fit_transform(self, documents):
        self.fit(documents)
        return self.transform(documents)

    def get_feature_names(self):
        return self.feature_names_


if __name__ == '__main__':

    first_corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()

    first_count_matrix = vectorizer.fit_transform(first_corpus)
    print('\nTest #1:')
    print(vectorizer.get_feature_names())
    # Вывожу векторы через цикл для лучшей читаемости
    for doc_vector in first_count_matrix:
        print(doc_vector)

    second_corpus = [
        'Pasta is a popular dish with pasta sauce',
        'Boil pasta in a large pot, then add sauce and Parmesan cheese',
        'Who is pasta'
    ]

    second_count_matrix = vectorizer.fit_transform(second_corpus)
    print('\nTest #2:')
    print(vectorizer.get_feature_names())
    for doc_vector in second_count_matrix:
        print(doc_vector)
