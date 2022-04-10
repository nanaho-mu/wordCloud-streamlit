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