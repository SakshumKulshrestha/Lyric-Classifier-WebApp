
import _pickle as pickle
import numpy

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif

class preprocess:

    def vectorize(words_file = "songs_pickle.pkl", authors_file="rapper_pickle.pkl"):

        authors_file_handler = open(authors_file, "rb")
        authors = pickle.load(authors_file_handler)
        authors_file_handler.close()

        words_file_handler = open(words_file, "rb")
        word_data = pickle.load(words_file_handler)
        words_file_handler.close()


        features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

        vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words=None)
        features_train_transformed = vectorizer.fit_transform(features_train)
        features_test_transformed  = vectorizer.transform(features_test)


        selector = SelectPercentile(f_classif, percentile=10)
        selector.fit(features_train_transformed, labels_train)
        features_train_transformed = selector.transform(features_train_transformed).toarray()
        features_test_transformed  = selector.transform(features_test_transformed).toarray()

        return features_train_transformed, features_test_transformed, labels_train, labels_test, vectorizer, selector