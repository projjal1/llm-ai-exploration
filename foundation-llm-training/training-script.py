from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

# 1. Load model and tokenizer
model_name = "distilgpt2"  # or "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token 

# Load the pre-trained model
model = AutoModelForCausalLM.from_pretrained(model_name)
model.config.pad_token_id = model.config.eos_token_id

# 2. Load your data (text files, CSV, etc.)
dataset = load_dataset("text", data_files={"train": "my_data.txt"})

# 3. Tokenize
def tokenize(batch):
    tokens = tokenizer(batch["text"], truncation=True, padding="max_length", max_length=128)
    tokens["labels"] = tokens["input_ids"].copy()
    return tokens

# Apply the tokenize function to the dataset
dataset = dataset.map(tokenize, batched=True)

# 4. Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=10,
    save_steps=500,
    logging_steps=100,
    learning_rate=5e-5
)

# 5. Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
)

# 6. Train
trainer.train()

# 7. Save the model
trainer.save_model("./finetuned_model")
# 8. Save the tokenizer
tokenizer.save_pretrained("./finetuned_model")