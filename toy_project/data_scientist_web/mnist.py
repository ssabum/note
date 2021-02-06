import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np

# streamlit이 웹페이지를 갱신하는 과정을 멈춤
# 최초 1회만 로드하고 그 후에는 로드하지 않음
@st.cache(allow_output_mutation=True)
def load():
    return load_model('model.h5')
model = load()

st.write('# MNIST Recognizer')

CANVAS_SIZE = 192

# 레이아웃을 2개로 설정
col1, col2 = st.beta_columns(2)

# 그림을 그릴 바탕을 설정
with col1:
    canvas = st_canvas(
        fill_color='#000000',
        stroke_width=20,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas'
    )

# 데이터가 있을 경우 리사이즈를 통해 preview이미지를 출력
if canvas.image_data is not None:
    img = canvas.image_data.astype(np.uint8)
    img = cv2.resize(img, dsize=(28, 28))
    preview_img = cv2.resize(img, dsize=(CANVAS_SIZE, CANVAS_SIZE), interpolation=cv2.INTER_NEAREST)

    col2.image(preview_img)

    # 모델의 input설정
    x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x = x.reshape((-1, 28, 28, 1))
    # 모델의 예측값 저장
    y = model.predict(x).squeeze()

    # 차트출력
    st.write('## Result: %d' % np.argmax(y))
    st.bar_chart(y)