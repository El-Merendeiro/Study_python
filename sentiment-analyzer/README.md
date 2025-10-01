# Sentiment Analyzer

## 🇯🇵 日本語版
簡単なウェブアプリで、コメントやメモの感情分析ができます。  
- Flask + Transformers で動作  
- コメントに「note」を付けて分析  
- 保存されたコメントはグラフで表示  

### 使用方法
1. `note` と `comment` を入力  
2. 保存する場合はチェックボックスをON  
3. **Analyze** ボタンで結果表示  
4. コメント一覧ページで統計グラフを確認  

### 技術
- Python 3.13+
- Flask
- Hugging Face Transformers
- Chart.js

---

## 🇬🇧 English Version
Simple web app to analyze sentiment of comments or notes.  
- Works with Flask + Transformers  
- Attach a "note" to the comment for context  
- Saved comments shown in a chart  

### Usage
1. Enter `note` and `comment`  
2. Check the box to save (optional)  
3. Click **Analyze** to see sentiment  
4. View saved comments and chart statistics  

### Tech
- Python 3.13+
- Flask
- Hugging Face Transformers
- Chart.js
