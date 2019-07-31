from preprocess import preprocess as p
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.feature_extraction.text import TfidfVectorizer


def predict(lyrics_input):
    classifier = GaussianNB()
    f_train, f_test, l_train, l_test = p.vectorize()
    classifier.fit(f_train, l_train)

    lyrics_input = stripString(lyrics_input)
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words=None)
    selector = SelectPercentile(f_classif, percentile=10)


    features_input = vectorizer.transform(lyrics_input)
    features_input  = selector.transform(features_input).toarray()

    print(classifier.predict(features_input))



def stripString(str1):
        a = "!@#$%^&*()><:;,[]|\?/~`'."
        for b in a:
            str1 = str1.replace(b, '')

        return (str1.lower()).rstrip("\n")

