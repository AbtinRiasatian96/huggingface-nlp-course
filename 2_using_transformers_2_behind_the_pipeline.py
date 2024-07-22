import torch
from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModel,
    AutoModelForSequenceClassification
)

raw_inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]

classifier = pipeline("sentiment-analysis")
pipeline_output = classifier(raw_inputs)
print(f"We are going to reconstruct this pipeline output step by step: {pipeline_output}")
print("-" * 40)

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
tokenized_inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")
print(f"Tokenized Inputs: {tokenized_inputs}")
print("-" * 40)

model = AutoModel.from_pretrained(checkpoint)
outputs = model(**tokenized_inputs)
print(f"Trasformer Mdel Output Feature Vectors: {outputs.last_hidden_state.shape}")
print("-" * 40)

model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
outputs = model(**tokenized_inputs)
print(f"Sentiment Analysis Logit Output: {outputs.logits}")
print("-" * 40)


predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
print(f"Softmax Probabilities: {predictions}")
print("-" * 40)

label_mapping = model.config.id2label
# Create the output in the desired format
result = []
for i, probs in enumerate(predictions):
    predicted_index = torch.argmax(probs).item()
    predicted_label = label_mapping[predicted_index]
    predicted_score = probs[predicted_index].item()
    result.append({'label': predicted_label, 'score': predicted_score})
print(f"Ta-Da!\n{result}")
print("-" * 40)