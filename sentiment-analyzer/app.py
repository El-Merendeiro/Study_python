##Sentiment-analyzer　2025/9/29
##アイフォン１７について、Redditから口コミを集めて、ポジティブかネガティブか確認

from flask import Flask, request, render_template
from transformers import pipeline
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
import praw

# Variabile
comments_list = []
sentiment_label_list = []
sentiment_score_list = []
sentiment_analyzer = pipeline("sentiment-analysis")

reddit = praw.Reddit(\
client_id=REDDIT_CLIENT_ID,\
client_secret=REDDIT_CLIENT_SECRET,\
user_agent=REDDIT_USER_AGENT)

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def home_page():
    sentiment_label = None
    sentiment_score = None

    if request.method == "POST":
        comment = request.form["comment"]
        save = "save" in request.form
        result = sentiment_analyzer(comment)[0]
        sentiment_label = result['label']
        sentiment_score = result['score']

        if save:
            comments_list.append(comment)
            sentiment_label_list.append(sentiment_label)
            sentiment_score_list.append(sentiment_score)

    return render_template('home.html', sentiment_label=sentiment_label, sentiment_score=sentiment_score)


@app.route('/comments')
def comments_page():
    return render_template('comments.html',
                           comments_list=comments_list,
                           sentiment_label_list=sentiment_label_list,
                           sentiment_score_list=sentiment_score_list)


def get_top_comments(product_name, limit=100):
  query = product_name
  reddit_comment = []


  for submission in reddit.subreddit("all").search(query, limit=10, sort="top"):
    submission.comments.replace_more(limit=0)  # evita placeholder
    for comment in submission.comments.list():
      reddit_comment.append({"body": comment.body, "score": comment.score})
  reddit_comment = sorted(reddit_comment, key=lambda x: x["score"], reverse=True)


  return reddit_comment[:limit]



if __name__ == '__main__':
    app.run(debug=True)



