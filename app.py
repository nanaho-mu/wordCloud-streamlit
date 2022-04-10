import streamlit as st
from PIL import Image
from wordcloud import WordCloud

def create_task(count=3):
    texts=[]
    for i in range(count):
        text=[]
        text.append(st.sidebar.text_input("task"+str(i+1), "task"+str(i+1)))
        slider=st.sidebar.slider("task"+str(i+1)+"の脳内比率", 0, 10, 5)
        text=text*slider
        text=" ".join(text)
        texts.append(text)
    return texts

def add_task(count):
    add_texts=[]
    for i in range(3, count+3):
        text=[]
        text.append(st.sidebar.text_input("task"+str(i+1), "task"+str(i+1)))
        slider=st.sidebar.slider("task"+str(i+1)+"の脳内比率", 0, 10, 5)
        text=text*slider
        text=" ".join(text)
        add_texts.append(text)
    return add_texts


st.title("脳内のタスクを整理しよう!")
st.sidebar.write("""脳内比率が大きいtaskほど  
画像に強調されて表示されるよ!""")
st.sidebar.write("taskを入力してね")

texts=create_task()
texts=" ".join(texts)

input_count=st.sidebar.number_input("追加するtaskの数を入力してください", 0, 20)
if input_count:
    add_texts=add_task(input_count)
    add_texts=" ".join(add_texts)
    texts+=" "+add_texts

font_path="/Library/Fonts/Arial Unicode.ttf"
wc=WordCloud(width=1280, height=720, background_color="white", font_path=font_path)
wc.generate(texts)
wc.to_file("wc.png")

image = Image.open('wc.png')

st.image(image, caption="""あなたの脳内のタスクを可視化しました。画像はpng形式で保存できます。待ち受け画面にしていつでも思い出せるようにしましょう!!""")