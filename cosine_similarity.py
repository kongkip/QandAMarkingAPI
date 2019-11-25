import nltk
from flask import Flask, render_template, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

nltk.download("stopwords")
nltk.download("punkt")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        x = request.form["correct answer"]
        y = request.form["student answer"]

        x_list = word_tokenize(x)
        y_list = word_tokenize(y)
        all_list = [x_list + y_list]

        word = 0
        for i in all_list:
            if i == "Not" or "not":
                word = "sentence contains negativity"
                break
            else:
                sw = stopwords.words("english")

                l1 = []
                l2 = []

                x_set = {w for w in x_list if w not in sw}
                y_set = {w for w in y_list if w not in sw}

                r_vector = x_set.union(y_set)
                for w in r_vector:
                    if w in x_set:
                        l1.append(1)
                    else:
                        l1.append(0)
                    if w in y_set:
                        l2.append(1)
                    else:
                        l2.append(0)
                c = 0
                for j in range(len(r_vector)):
                    c += l1[j] * l2[j]
                cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
                word = cosine
        return jsonify(word)

            # elif request.method == "GET":
            #     query_parameters = request.args
            #     x = query_parameters.get("correct_answer")
            #     y = query_parameters.get("student_answer", )


            #
            #     x_list = word_tokenize(x)
            #     y_list = word_tokenize(y)
            #
            #     sw = stopwords.words("english")
            #
            #     l1 = []
            #     l2 = []
            #
            #     x_set = {w for w in x_list if w not in sw}
            #     y_set = {w for w in y_list if w not in sw}
            #
            #     r_vector = x_set.union(y_set)
            #     for w in r_vector:
            #         if w in x_set:
            #             l1.append(1)
            #         else:
            #             l1.append(0)
            #         if w in y_set:
            #             l2.append(1)
            #         else:
            #             l2.append(0)
            #     c = 0
            #     for i in range(len(r_vector)):
            #         c += l1[i] * l2[i]
            #     cosine = (c / float((sum(l1) * sum(l2)) ** 0.5)) * 100
            #     # return """<h1>The student answer is {} correct</h1>""".format(cosine * 100)
            #    return jsonify(cosine)
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
