# radqbank/pages/qsession.py
import streamlit as st, random, json
from radqbank.loaders import load_questions
from radqbank.state   import get_cfg

cfg = get_cfg()
df, _ = load_questions()

# Simple sidebar filters
topics = st.sidebar.multiselect(
    "Topic", sorted(df["primary_topic"].unique()),
    default=df["primary_topic"].unique())

filtered = df[df["primary_topic"].isin(topics)]
question = filtered.sample(1).iloc[0]  # random row

st.markdown(question["stem_md"])
if pd.notna(question["image_filename"]):
    st.image(f'{cfg["media_dir"]}/{question["image_filename"]}')

# MCQ rendering
opts = json.loads(question["options_json"])
choice = st.radio("Choose an answer:", opts, key=question["question_id"])

if st.button("Submit"):
    correct = question["correct_answer"]
    if choice == correct:
        st.success("Correct! 🎉")
    else:
        st.error(f"Incorrect.  Correct answer: **{correct}**")
    st.markdown(question["explanation_md"])
