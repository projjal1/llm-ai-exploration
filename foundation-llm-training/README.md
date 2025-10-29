# Foundation LLM Training

Short guide for the scripts in this folder and the recommended run order.

Prerequisites
- Python 3.8+
- Optional: GPU + CUDA or Apple Silicon GPU MPS enabled for faster training
- Create a virtual environment and install dependencies if a requirements file exists:
  - python3 -m venv .venv
  - source .venv/bin/activate
  - pip install -r requirements.txt

Files
- training-script.py — main fine-tuning script (uses Hugging Face Trainer/tokenizer helpers).
- my_data.txt — training data used by training-script.py.
- prompt-testing.py — simple inference/test script that loads the saved finetuned model (saved to ./finetuned_model by default).

Recommended run order
1. Prepare environment
   - Activate virtualenv and install requirements (see above).
   - Make any edits to my_data.txt or training hyperparameters inside training-script.py before starting.

2. Train / fine-tune
   - Run: python training-script.py
   - Output: a directory ./finetuned_model (or the path configured in the script) containing the saved model and tokenizer.

3. Quick test / inference
   - Run: python prompt-testing.py
   - This script loads the model from ./finetuned_model and runs a few example prompts to verify behavior.

Notes & tips
- To change training data, edit my_data.txt or update the training data path in training-script.py.
- For large models or long runs, run on a machine with a GPU and ensure transformers/PyTorch are installed with CUDA support.
- If training fails due to memory, reduce batch size, sequence length, or use gradient accumulation (tweak hyperparameters in training-script.py).
- Logs and checkpoints: check the script for where logs/checkpoints are written (by default inside the working folder or ./runs).

Contact / troubleshooting
- Inspect training-script.py for exact hyperparameters and model/tokenizer selection.
- If you need a tailored run command (e.g., different output path or custom training args), specify the change and a short example command will be provided.