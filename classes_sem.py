import math


class CountVectorizer:
    """
    A class for vectorizing text using the CountVectorizer algorithm.
    """

    def __init__(self) -> None:
        """
        Initialize the CountVectorizer.
        """
        self.vocab_ = {}
        self.feature_names_ = []

    def fit(self, documents: list[list[str]]) -> None:
        """
        Fit the CountVectorizer to the provided documents.

        Parameters:
        - documents: A list of strings representing the documents.

        Returns:
        - None
        """
        self.vocab_ = {}
        self.feature_names_ = []

        for doc in documents:
            for word in doc.split():
                word = word.lower()
                if word not in self.vocab_:
                    self.vocab_[word] = len(self.vocab_)
                    self.feature_names_.append(word)

    def transform(self, documents: list[str]) -> list[list[int]]:
        """
        Transform the provided documents to their count vector representation.

        Parameters:
        - documents: A list of strings representing the documents.

        Returns:
        - matrix: A matrix representing the count vector
        representation of the documents.
        """
        matrix = []
        for doc in documents:
            doc_vector = [0] * len(self.vocab_)
            for word in doc.split():
                word = word.lower()
                if word in self.vocab_:
                    doc_vector[self.vocab_[word]] += 1
            matrix.append(doc_vector)

        return matrix

    def fit_transform(self, documents: list[str]) -> list[list[int]]:
        """
        Fit the CountVectorizer to the provided documents and transform them.

        Parameters:
        - documents: A list of strings representing the documents.

        Returns:
        - matrix: A matrix representing the count vector
        representation of the documents.
        """
        self.fit(documents)
        return self.transform(documents)

    def get_feature_names(self) -> list[str]:
        """
        Get the feature names of the CountVectorizer.

        Returns:
        - feature_names: A list of strings representing the feature names.
        """
        return self.feature_names_

    def tf_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Transform the count matrix to its term frequency representation.

        Parameters:
        - count_matrix: A matrix representing the count vector
        representation of the documents.

        Returns:
        - tf_matrix: A matrix representing the term frequency representation.
        """
        tf_matrix = []
        for doc_vector in count_matrix:
            tf_matrix.append(
                [round(rep / sum(doc_vector), 3) for rep in doc_vector]
            )
        return tf_matrix

    def idf_transform(self, count_matrix: list[list[int]]) -> list[float]:
        """
        Transform the count matrix to its
        inverse document frequency representation.

        Parameters:
        - count_matrix: A matrix representing the count vector
        representation of the documents.

        Returns:
        - idf_matrix: A matrix representing the inverse document
        frequency representation.
        """
        docs_num = len(count_matrix)
        idf_matrix = []

        for word_counter in zip(*count_matrix):
            docs_with_word = sum(
                int(num_count > 0) for num_count in word_counter
            )
            idf_matrix.append(
                round(math.log((docs_num + 1) / (docs_with_word + 1)) + 1, 3)
            )

        return idf_matrix


class TfidfTransformer():
    """
    A class for transforming count matrices to their
    tf-idf representation.
    """

    def fit_transform(self,
                      count_mtrx: list[list[int]]) -> list[list[float]]:
        """
        Fit the TfidfTransformer to the provided count matrix
        and transform it to tf-idf representation.

        Parameters:

        - count_matrix: A matrix representing the count vector
        representation of the documents.

        Returns:
        - tfidf_matrix: A matrix representing the tf-idf representation.
        """
        tf_mtrx = []
        for doc_vector in count_mtrx:
            tf_mtrx.append(
                [round(rep / sum(doc_vector), 3) for rep in doc_vector]
            )

        docs_num = len(count_mtrx)
        wrd = len(count_mtrx[0])
        idf_mtrx = []

        for word_counter in zip(*count_mtrx):
            docs_with_word = sum(
                int(num_count > 0) for num_count in word_counter
            )
            idf_mtrx.append(
                round(math.log((docs_num + 1) / (docs_with_word + 1)) + 1, 3)
            )

        tfidf_mtrx = []

        for row in range(docs_num):
            tfidf_mtrx.append(
                [
                    round(tf_mtrx[row][w] * idf_mtrx[w], 3) for w in range(wrd)
                ]
            )

        return tfidf_mtrx


class TfidfVectorizer(CountVectorizer):
    """
    A class for vectorizing text using the TfidfVectorizer algorithm.
    """

    def __init__(self) -> None:
        """
        Initialize the TfidfVectorizer.
        """
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Fit the TfidfVectorizer to the provided corpus
        and transform it to tf-idf representation.

        Parameters:
        - corpus: A list of strings representing the documents.

        Returns:
        - tfidf_matrix: A matrix representing the tf-idf
        representation of the corpus.
        """
        count_matrix = super().fit_transform(corpus)

        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()

    count_matrix = vectorizer.fit_transform(corpus)
    print('\nTest for CountVectorizer:')
    print(vectorizer.get_feature_names())
    # Вывожу векторы через цикл для лучшей читаемости
    for doc_vector in count_matrix:
        print(doc_vector)
    print('------------------------------')

    print('\nTest for Tf/idf transform')
    print('tf_transform:')
    tf_matrix = vectorizer.tf_transform(count_matrix)
    print(tf_matrix)
    second_corpus = [
        'Pasta is a popular dish with pasta sauce',
        'Boil pasta in a large pot, then add sauce and Parmesan cheese',
        'Who is pasta'
    ]
    print('\nidf_transform')
    idf_matrix = vectorizer.idf_transform(count_matrix)
    print(idf_matrix)

    print('------------------------------')
    print('\nTest for TfidfTransformer')

    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print('tfidf matrix:')
    print(tfidf_matrix)

    print('------------------------------')
    print('\nTest for TfidfVectorizer')
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print('tfidf matrix')
    print(tfidf_matrix)
