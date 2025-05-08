# Sentiment Analysis Pipeline using Spark, BERT and FastAPI

## Overview
This project is a full-stack sentiment analysis pipeline built with:
- Apache Spark: large-scale preprocessing
- BERT (Hugging Face): deep learning model for classification
- FastAPI: real-time serving
- React frontend : for user interaction

## Workflow

1. **Data Preprocessing with Spark**  
   - Load Sentiment140 dataset using PySpark.
   - Clean and normalize text (remove URLs, mentions, non-alphabetic chars).
   - Map sentiment labels: 0 = negative, 2 = neutral, 4 = positive.

2. **Fine-tune BERT with HuggingFace Transformers**  
   - Load cleaned dataset into HuggingFace Datasets.
   - Tokenize using BERT tokenizer with truncation/padding.
   - Use Trainer API to fine-tune the model with early stopping and eval on validation set.

3. **Export Model for Serving**  
   - Save model and tokenizer to ./sentiment_model.
   - Supports inference on single-sentence text with label probabilities.

4. **Deploy Inference API with FastAPI**  
   - Load saved model in FastAPI.
   - Expose endpoint: POST /predict
   - Accepts JSON input like:
     ```json
     {"text": "I love this product!"}
     ```
   - Returns:
     ```json
     {"label": "positive", "confidence": 0.98}
     ```

5. **Frontend**  
   - React app for real-time sentiment analysis using the API.
   - Connect via cmd on the local machine