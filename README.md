# nano-mind-reader: Visualizing the Internal "Thought Patterns" of a Tiny GPT

## Project Overview

This project, inspired by Andrej Karpathy's `nanoGPT`, aims to provide a glimpse into the internal workings of a small Generative Pre-trained Transformer (GPT) model. By visualizing the attention mechanisms within the transformer blocks, we can observe how the model "attends" to different parts of the input sequence when generating new text. This offers a thought-provoking perspective on how these powerful language models process information and form connections.

## Features

- **Tiny GPT Implementation:** A minimalistic, character-level GPT model built from scratch using PyTorch.
- **Attention Visualization:** Generates heatmaps of attention weights for each head in every transformer block, illustrating the model's focus during text generation.
- **Text Generation:** Demonstrates the model's ability to generate new text after a brief training period.

## How it Works

The core of this project is a simplified GPT model. During the forward pass, we extract the attention weights from each multi-head attention layer. These weights indicate the importance or relevance of each input token to the current token being processed. By visualizing these weights as heatmaps, we can intuitively understand which parts of the input sequence the model is 
focusing on at different layers and heads.

## Installation and Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/RawQubit/nano-mind-reader.git
    cd nano-mind-reader
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    uv pip install torch --index-url https://download.pytorch.org/whl/cpu
    uv pip install matplotlib numpy requests
    ```

4.  **Download the dataset:**
    ```bash
    mkdir -p data
    wget -O data/input.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
    ```

5.  **Run the project:**
    ```bash
    python3 main.py
    ```

    This will train a small GPT model, generate attention visualizations in the `visualizations/` directory, and print some generated text to the console.

## Example Visualizations

(Images will be inserted here after generation)

## Acknowledgements

This project is heavily inspired by Andrej Karpathy's excellent `nanoGPT` repository, which provides a clean and understandable implementation of a GPT model.
