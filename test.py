import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.write('show progressbar')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    #time.sleep(0.1)

'Done!'

st.title('streamlit 超入門')
st.write('Display Image')
#st.write('data frame')

df = pd.DataFrame({
   '１列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)

df2 =pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

#st.bar_chart(df2)

df3 =pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ['lat','lon']
)

#st.dataframe(df3)
#st.map(df3)

if st.checkbox('show image'):
    img = Image.open('sample.JPG')
    st.image(img,caption='sample',use_column_width=True)


option = st.selectbox(
    'please teach me what is your favorite number',
    list(range(1,11))
)

'あなたの好きな数字は、', option,'です。'

st.write('Interactive Widgets')

text = st.sidebar.text_input('What is your hobby?')
'Your hobby:',text

condition = st.sidebar.slider('what is your condition?',0,100,50)
'your condition:',condition

left_column,right_colum = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_colum.write('here is right column')

expander = st.expander('inquery')
expander.write('result of inquery')