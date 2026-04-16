# TACOS

TACOS stands for Toxicity Analysis & Comment Observation System. It is a machine-learning-based moderation project for detecting toxic, abusive, and harmful comments in user-generated content using a fine-tuned DistilBERT model, a FastAPI backend, and a Streamlit frontend.

## Live Demo

- Hugging Face Space: [https://huggingface.co/spaces/Venkat-023/TACOS](https://huggingface.co/spaces/Venkat-023/TACOS)

## Project Overview

This project analyzes text comments and predicts toxicity-related categories in real time. Based on the model output, the app can decide whether to:

- `ALLOW` a comment
- `WARN` the user
- `BLOCK` the comment

The supported labels are:

- `toxic`
- `severe_toxic`
- `obscene`
- `threat`
- `insult`
- `identity_hate`

## Features

- Real-time moderation through a Streamlit UI
- FastAPI backend for inference requests
- DistilBERT-based multi-label toxicity classification
- Confidence scores for each toxicity category
- Dockerized deployment for Hugging Face Spaces

## Tech Stack

- `FastAPI`
- `Streamlit`
- `PyTorch`
- `Transformers`
- `Docker`

## Dataset

- [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

## Project Structure

```text
Backend/
  app.py
  requirements.txt
  toxic_model/
Frontend/
  front.py
Dockerfile
requirements-docker.txt
start.py
README.md
```

## Local Run With Docker

```bash
docker build -t tacos-app .
docker run -p 7860:7860 tacos-app
```

Then open `http://localhost:7860`.

## Deployment Notes

The Docker container is configured to:

- expose the Streamlit UI on port `7860`
- run the FastAPI backend internally on port `8000`
- use the bundled model weights from `Backend/toxic_model/model.pt`

## Workflow

1. The user uploads an image and enters a comment.
2. The frontend sends the comment to the FastAPI backend.
3. The backend scores the comment across multiple toxicity categories.
4. The UI decides whether to allow, warn, or block the comment.

## Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Venkat-023">
        <img src="https://github.com/Venkat-023.png" width="100px;" alt="Venkat"/>
        <br />
        <sub><b>Venkat</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/rishitha-1612">
        <img src="https://github.com/rishitha-1612.png" width="100px;" alt="Rishitha Rasineni"/>
        <br />
        <sub><b>Rishitha Rasineni</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/2406-Sowmya">
        <img src="https://github.com/2406-Sowmya.png" width="100px;" alt="Sowmya"/>
        <br />
        <sub><b>Sowmya PR</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Diamonds-shine">
        <img src="https://github.com/Diamonds-shine.png" width="100px;" alt="Diamonds-shine"/>
        <br />
        <sub><b>Diamonds Shine</b></sub>
      </a>
    </td>
  </tr>
</table>
