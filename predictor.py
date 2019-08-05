from preprocess import preprocess as p
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.feature_extraction.text import TfidfVectorizer

class predictor:

    def predict(lyrics_input):
        classifier = GaussianNB()
        f_train, f_test, l_train, l_test, vectorizer, selector = p.vectorize()
        classifier.fit(f_train, l_train)

        lyrics_input = predictor.stripString(lyrics_input)
        lyrics_input = [lyrics_input]


        features_input = vectorizer.transform(lyrics_input)
        features_input  = selector.transform(features_input).toarray()

        results_list = classifier.predict(features_input)
        result_digit = results_list[0]

        if result_digit == '0':
            return "Eminem"
        elif result_digit == '1':
            return "Drake"
        else:
            return "Inconclusive"


    def stripString(str1):
            a = "!@#$%^&*()><:;,[]|\?/~`'."
            for b in a:
                str1 = str1.replace(b, '')

            return (str1.lower()).rstrip("\n")


    # s1 = """Staying in big six-six with woes
    # Man start dissin' and doin' reposts
    # They do anything except road
    # Still can't see them after it snows
    # I don't have time for the wasteman jokes
    # Personal ting if I'm gettin' up close
    # Loyal to O 'cause I've taken a oath
    # Versace hotel and I'm takin' the robes
    # Seen 'em in person, I'm seein' a ghost
    # They told me relax 'cause they're takin' control
    # Take all that shit up with P and his bro
    # I wish you the best, let me know how it goes
    # Wanna be free and I wanna let go
    # We came around and you showed us the most"""

    # predict(s1)
