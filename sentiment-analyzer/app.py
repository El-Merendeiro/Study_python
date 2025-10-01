##Sentiment-analyzer　2025/9/29
##アイフォン１７について、Redditから口コミを集めて、ポジティブかネガティブか確認

from flask import Flask, request, render_template
from transformers import pipeline

# Variabile
comments_list = []
sentiment_label_list = []
sentiment_score_list = []
sentiment_analyzer = pipeline("sentiment-analysis")

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def home_page():
  sentiment_label = None
  sentiment_score = None

  if request.method == "POST":
    note = request.form.get("note", "")
    comment = request.form.get("comment", "")
    save = "save" in request.form

    if comment:
      text_to_analyze = f"{note} - {comment}" if note else comment
      result = sentiment_analyzer(text_to_analyze)[0]
      sentiment_label = result['label']
      sentiment_score = result['score']
      if save:
        comments_list.append(text_to_analyze)
        sentiment_label_list.append(sentiment_label)
        sentiment_score_list.append(sentiment_score)
  return render_template('home.html', sentiment_label=sentiment_label, sentiment_score=sentiment_score)

@app.route('/comments')
def comments_page():
  return render_template('comments.html', comments_list=comments_list, sentiment_label_list=sentiment_label_list, sentiment_score_list=sentiment_score_list)

if __name__ == '__main__':
    app.run(debug=True)



