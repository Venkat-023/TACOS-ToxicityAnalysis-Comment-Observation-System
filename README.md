---
title: TACOS
emoji: "🛡️"
colorFrom: blue
colorTo: red
sdk: docker
app_port: 7860
---

# TACOS

TACOS stands for Toxicity Analysis & Comment Observation System. It is a toxic comment moderation project that combines a `FastAPI` inference backend, a `Streamlit` frontend, and a fine-tuned toxicity classification model to review user comments before posting.

## Live Demo

- Hugging Face Space: [https://huggingface.co/spaces/Venkat-023/TACOS](https://huggingface.co/spaces/Venkat-023/TACOS)

## Project Overview

This project helps detect harmful or abusive comments and classifies them into common toxicity categories such as:

- `toxic`
- `severe_toxic`
- `obscene`
- `threat`
- `insult`
- `identity_hate`

Based on the model scores, the application can decide whether to:

- `ALLOW` a comment
- `WARN` the user
- `BLOCK` the comment

## Tech Stack

- `FastAPI` backend for inference APIs
- `Streamlit` frontend for the user interface
- `PyTorch` and `Transformers` for the toxicity model
- Root-level `Dockerfile` for Hugging Face Docker Spaces deployment

## Local Docker Run

```bash
docker build -t tacos-app .
docker run -p 7860:7860 tacos-app
```

Then open `http://localhost:7860`.

## Hugging Face Space

The container:

- Exposes the Streamlit UI on port `7860`
- Starts the FastAPI backend internally on port `8000`
- Uses the bundled model weights from `Backend/toxic_model/model.pt`
