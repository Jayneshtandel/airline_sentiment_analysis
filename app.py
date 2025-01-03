# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lrulVvcjqqT7sdHH1aaQx73FvSn9U-RU
"""

import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the pretrained model and tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("path_to_your_model_directory")

# Define a function to predict sentiment
def predict_sentiment(text):
    inputs = tokenizer.encode_plus(
        text, max_length=512, truncation=True, padding="max_length", return_tensors="pt"
    )
    outputs = model(inputs["input_ids"])
    prediction = torch.argmax(outputs.logits, dim=1).item()
    labels = {0: "Negative", 1: "Neutral", 2: "Positive"}
    return labels[prediction]

# Streamlit app UI
st.title("Airline Sentiment Analysis")
st.write("Analyze the sentiment of airline customer feedback.")

# User input for text
user_input = st.text_input("Enter text to analyze:")

if st.button("Analyze"):
    if user_input:
        sentiment = predict_sentiment(user_input)
        st.success(f"Sentiment: {sentiment}")
    else:
        st.error("Please enter text to analyze.")