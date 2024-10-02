import pandas as pd
import re
import torch
from transformers import BertTokenizer, BertForSequenceClassification, BertForTokenClassification, pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load BioBERT for NER
bio_ner_model = BertForTokenClassification.from_pretrained('dmis-lab/biobert-v1.1', num_labels=28)
bio_ner_tokenizer = BertTokenizer.from_pretrained('dmis-lab/biobert-v1.1')
bio_ner_pipeline = pipeline("ner", model=bio_ner_model, tokenizer=bio_ner_tokenizer, aggregation_strategy="simple")

# Load BERT for pain intensity classification
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)  # Fine-tuned BERT model for pain intensity

# Sentiment analysis using VADER
sentiment_analyzer = SentimentIntensityAnalyzer()

# ------------------------------------
# Step 1: Training Data Preprocessing (Using Vignette Column)
# ------------------------------------

# Load the CSV files (adjust file paths as needed)
acute_cancer_data = pd.read_csv('data_acute_cancer.csv')
acute_non_cancer_data = pd.read_csv('data_acute_non_cancer.csv')
chronic_cancer_data = pd.read_csv('data_chronic_cancer.csv')
chronic_non_cancer_data = pd.read_csv('data_chronic_non_cancer.csv')
post_op_data = pd.read_csv('data_post_op.csv')

# Step 1.1: Consolidate the Data
all_data = pd.concat([acute_cancer_data, acute_non_cancer_data, chronic_cancer_data, chronic_non_cancer_data, post_op_data], ignore_index=True)

# Step 1.2: Preprocess the Vignette column
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# Apply the preprocessing to the 'Vignette' column
all_data['Vignette'] = all_data['Vignette'].apply(preprocess_text)

# Step 1.3: Feature Extraction from the Vignette Column

# Pain Intensity Extraction Using Pre-trained BERT
def classify_pain_intensity(text):
    inputs = bert_tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = bert_model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    
    if predicted_class == 0:
        return 'Mild'
    elif predicted_class == 1:
        return 'Moderate'
    elif predicted_class == 2:
        return 'Severe'
    return 'Unknown'

# Body Part Extraction Using BioBERT NER
def extract_body_part(text):
    ner_results = bio_ner_pipeline(text)
    body_parts = [entity['word'] for entity in ner_results if entity['entity_group'] == 'B-LOC']  # Assuming 'B-LOC' for anatomical parts
    if body_parts:
        return ', '.join(body_parts)
    return 'Unknown'

# Pain Type Extraction Using a Rule-Based Approach
# Expanded list of pain types
pain_type_keywords = [
    'throbbing', 'burning', 'sharp', 'dull', 'aching', 'stabbing', 'tingling', 'cramping', 'radiating', 
    'shooting', 'pulsing', 'sore', 'pressure', 'numbing', 'gnawing', 'piercing', 'tender', 'stinging',
    'electric', 'cold', 'hot', 'searing', 'prickling', 'itchy', 'tight', 'nagging', 'pins and needles'
]

def extract_pain_type(text):
    # Convert text to lowercase to make matching case-insensitive
    text = text.lower()
    
    # Loop through the pain type keywords
    for keyword in pain_type_keywords:
        if keyword in text:
            return keyword
    return 'Unknown'

# Duration Extraction Using Regular Expressions
duration_pattern = re.compile(r'for the past \d+ days|since last \w+')
def extract_duration(text):
    match = duration_pattern.search(text)
    if match:
        return match.group(0)
    return 'Unknown'

# Apply feature extraction to the Vignette column
all_data['Pain Intensity'] = all_data['Vignette'].apply(classify_pain_intensity)
all_data['Pain Type'] = all_data['Vignette'].apply(extract_pain_type)
all_data['Body Part'] = all_data['Vignette'].apply(extract_body_part)
all_data['Duration'] = all_data['Vignette'].apply(extract_duration)

# Step 1.4: Save the Preprocessed and Feature-Extracted Training Data
all_data.to_csv('preprocessed_pain_training_data.csv', index=False)
print("\nTraining data preprocessing and feature extraction completed and saved as 'preprocessed_pain_training_data.csv'")

# ------------------------------------
# Step 2: Real-Time User Input Processing (No changes)
# ------------------------------------

# Sentiment and Emotion Analysis Using VADER
def extract_sentiment(text):
    sentiment_score = sentiment_analyzer.polarity_scores(text)['compound']
    if sentiment_score >= 0.05:
        return 'Positive'
    elif sentiment_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Process user input (chat or transcribed voice)
def process_user_input(user_input):
    # Step 1: Preprocess the input text (real-time)
    cleaned_text = preprocess_text(user_input)

    # Step 2: Extract features from real-time input
    pain_intensity = classify_pain_intensity(cleaned_text)
    pain_type = extract_pain_type(cleaned_text)
    body_part = extract_body_part(cleaned_text)
    duration = extract_duration(cleaned_text)
    sentiment = extract_sentiment(user_input)  # Sentiment based on original input

    # Return the extracted features
    return {
        'Original Text': user_input,
        'Cleaned Text': cleaned_text,
        'Pain Intensity': pain_intensity,
        'Pain Type': pain_type,
        'Body Part': body_part,
        'Duration': duration,
        'Sentiment': sentiment
    }

# Example real-time user input (could be from chat or transcribed voice)
user_input_text = "I am a 45-year-old female with breast cancer, experiencing a dull ache in my left shoulder for the past week. I feel frustrated because the pain interferes with my daily activities. Despite taking my prescribed pain medication, it hasn't alleviated the discomfort"
processed_features = process_user_input(user_input_text)

# Output the extracted features for real-time input
print("\nExtracted Features from Real-Time Input:")
for key, value in processed_features.items():
    print(f"{key}: {value}")

# End of the full workflow
