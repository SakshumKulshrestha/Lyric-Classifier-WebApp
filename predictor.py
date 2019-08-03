from preprocess import preprocess as p
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.feature_extraction.text import TfidfVectorizer

def predict(lyrics_input):
    classifier = GaussianNB()
    f_train, f_test, l_train, l_test, vectorizer, selector = p.vectorize()
    classifier.fit(f_train, l_train)

    lyrics_input = stripString(lyrics_input)
    lyrics_input = [lyrics_input]

    features_input = vectorizer.transform(lyrics_input)
    features_input  = selector.transform(features_input).toarray()

    print(classifier.predict(features_input))



def stripString(str1):
        a = "!@#$%^&*()><:;,[]|\?/~`'."
        for b in a:
            str1 = str1.replace(b, '')

        return (str1.lower()).rstrip("\n")


s1 = "She's takin a little nap in the trunk Oh that smell (whew!) da-da musta runned over a skunkNow I know what you're thinkin - it's kind of late to go swimminBut you know your mama, she's one of those type of womenthat do crazy things, and if she don't get her way, she'll throw a fitDon't play with da-da's toy knife, honey, let go of it (no!)And don't look so upset, why you actin bashful?"
predict(s1)
