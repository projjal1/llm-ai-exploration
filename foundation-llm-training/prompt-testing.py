from transformers import pipeline, AutoTokenizer

# Define the model path
model_path = "./finetuned_model"

# Load the embeddings from the model
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Load the model into the pipelines
pipe = pipeline("text-generation", model=model_path, tokenizer=tokenizer, device="mps")

questions = ["Phishing in cybersecurity landscape", "Man in the middle is a type of"]

# Generate answers for the questions
for question in questions:
    answer = pipe(question)[0]['generated_text']
    print(f"question: {question} \nanswer: {answer}\n\n")