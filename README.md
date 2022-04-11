# タイトルと概要、URL
## タイトル
脳内のタスクを整理しよう!
## 概要
taskを入力し、そのtaskが占める脳内比率を0-10で入力することで、0に近づくほど小さく、10に近づくほど大きく画像に表示できます。  
そのため、自分の頭の中のtaskの種類と数、大きさを可視化することで、taskを整理し、優先順位をつけて消化する上での手助けになります。

## URL
**https://share.streamlit.io/nanaho-mu/wordcloud-streamlit/main/app.py**
## THE VIEW
![wordcloud-streamlit](https://user-images.githubusercontent.com/72216137/162662570-cb859a97-d55c-4c64-9ae7-f8f1b8c3a659.gif)


# 目指した課題解決
これまで私自身todoアプリを利用してきて感じてきたのは、個々todoリストが並列で表示してあるため、パッと見でtaskの重さや優先度がわからず効率的に片付けるための頭の中の整理ができない、ということでした。  
そこでユーザの頭の中にあるtaskを可視化することで、その課題を解決できるのではないかと考えました。
<!-- 人間は消化すべきtaskが多すぎるとその事実が強く頭から離れず、何をしているときでも何かに追われている感じがして、大きなストレスになります。それは、やるべきtaskをうまく整理できていないからであり、何から手を付けていけばいいかわからなくなっています。 -->
<!-- そこで重要なのが、taskに優先順位をつけて、できるだけすぐできるものから消化してくことだと考えています。それによって多くのやるべきことに追われているというストレスから解放され、今何をやるべきかということにフォーカスできるようになります。 -->
# 使用技術
- python
- streamlit
- streamlit cloud
- wordcloud
- matplotlib
- pillow
# 機能一覧
- taskを入力フォームから入力できる
- taskの占める脳内比率を0-10で選択できる
- 入力されたデータからワードクラウドが生成される
- taskの入力フォームは20個追加できる
- 日本語でも英語でも入力可能
- 画像はpngで保存可能

