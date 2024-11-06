# Fine-Tuning a Causal Language Model with LoRA

This project demonstrates the fine-tuning of a causal language model using the [LoRA (Low-Rank Adaptation)](https://arxiv.org/abs/2106.09685) technique. We leverage Hugging Face's `transformers` library and the PEFT library to efficiently adapt a pre-trained model on a dataset of high school education data.

## Requirements

To run this code, install the following Python packages:

```bash
pip install datasets transformers peft

## Code Overview
The following steps outline the process of preparing and fine-tuning the model.

Step 1: Load Dataset
We start by loading a dataset focused on high school education.

Step 2: Subset Selection
To reduce processing time, a small subset of 100 training and 10 testing examples is selected.

Step 3: Load Model and Tokenizer
Load the Gemma-2 model and tokenizer, adjusting the pad_token if missing.

Step 4: Tokenize Dataset
The dataset is tokenized to a maximum sequence length of 256.

Step 5: Define LoRA Configuration
Define the configuration parameters for LoRA.

Step 6: Wrap Model with LoRA
The model is adapted with LoRA for efficient fine-tuning.

Step 7: Define Training Arguments
Specify the training arguments, such as batch size, learning rate, and evaluation strategy.

Step 8: Define Data Collator
Define a data collator to manage language model training without masked language modeling (MLM).

Step 9: Set Up Trainer
The Trainer class is used to manage training and evaluation.

Step 10: Train the Model
Fine-tune the model on the selected dataset.

Step 11: Evaluate the Model
After training, the model is evaluated on the test set.

Step 12: Merge LoRA Weights
Merge LoRA weights into the base model.

Step 13: Save the Fine-Tuned Model
Save the fully fine-tuned model and tokenizer.
