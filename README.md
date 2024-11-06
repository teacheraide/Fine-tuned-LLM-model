# Fine-Tuning a Causal Language Model with LoRA

This project demonstrates the fine-tuning of a causal language model using the [LoRA (Low-Rank Adaptation)](https://arxiv.org/abs/2106.09685) technique. We leverage Hugging Face's `transformers` library and the PEFT library to efficiently adapt a pre-trained model on a dataset of high school education data.

## Requirements

To run this code, install the following Python packages:

```bash
pip install datasets transformers peft
