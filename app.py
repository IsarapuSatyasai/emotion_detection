# Core Packages
import streamlit as st
import altair as alt

# EDA Packages
import pandas as pd
import numpy as np

# Utils
import joblib

pipe_lr = joblib.load(open("models/emotion_classifier_pipe_lr.pkl","rb"))

def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]

def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results
emotions_emoji_dict = {"anger":"😠","disgust":"🤮", "fear":"😨😱", "happy":"🤗", "joy":"😂", "neutral":"😐", "sad":"😔", "sadness":"😔", "shame":"😳", "surprise":"😮"}
def main():
        st.title("Emotion Classifier App")
        # menu = ["Home", "Monitor", "About"]


        # choice = st.sidebar.selectbox("Menu",menu)

        st.subheader("Detect-Emotion In Text")

        with st.form(key='emotion_clf_form'):
           raw_text = st.text_area("Type Here")
           submit_text = st.form_submit_button(label='Submit')
        if submit_text:
            col1,col2 = st.columns(2)

            prediction = predict_emotions(raw_text)
            probability = get_prediction_proba(raw_text)
            with col1:
                st.success("Original Text")
                st.write(raw_text)

                st.success("Prediction")
                emoji_icon=emotions_emoji_dict[prediction]
                st.write("{}:{}".format(prediction,emoji_icon))
                st.write("Confidence:{}".format(np.max(probability)))
            with col2:
               st.success("Prediction Probability")
               # st.write(probability)
               proba_df = pd.DataFrame(probability,columns=pipe_lr.classes_)
               # st.write(proba_df)
               proba_df_clean = proba_df.T.reset_index()
               proba_df_clean.columns = ["Emotions","Probability"]

               fig = alt.Chart(proba_df_clean).mark_bar().encode(x='Emotions',y='Probability',color='Emotions')
               st.altair_chart(fig,use_container_width=True)
if __name__ == '__main__':
    main()
