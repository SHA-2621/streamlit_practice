import streamlit as st
import time

st.title('streamlit かんたん')

st.write('プログレスバーの表示')
start = st.button('Start!')

latest_iteration = st.empty()
bar = st.progress(0)

if start:
  for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column,right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラムです')

expander = st.expander('Q.料金はかかりますか？')
expander.write('トライアル期間中のため完全無料です')

# text = st.text_input('あなたの趣味を教えてください' )

# 'あなたの趣味は',text,'です'

# condition = st.slider('あなたのいまの調子は?',0,100,50)


# if st.button('Submit'):
#   st.write(condition)

# else:
#   st.write('コンディションを入力してください')

# options = st.multiselect(
#   '探したい内容を選んでください',
#   ['戦略','ミッション・ビジョン・バリュー','メンバー紹介'],
# )

# st.write('選択済み', options)

# # if st.checkbox('Show image'):
# #   img = Image.open('wellthnavi-29.jpg')
# #   st.image(img, caption='wellthnavi',use_column_width=True)


