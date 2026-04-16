---
title: TACOS
emoji: "🛡️"
colorFrom: blue
colorTo: red
sdk: docker
app_port: 7860
---

# TACOS

TACOS is a toxic comment moderation demo with:

- A `FastAPI` backend for inference
- A `Streamlit` frontend for the user interface
- A root `Dockerfile` ready for Hugging Face Docker Spaces

## Local Docker Run

```bash
docker build -t tacos-app .
docker run -p 7860:7860 tacos-app
```

Then open `http://localhost:7860`.

## Hugging Face Space

Push this repository to a Hugging Face Space created with the `Docker` SDK.

The container:

- Exposes the Streamlit UI on port `7860`
- Starts the FastAPI backend internally on port `8000`
- Uses the bundled model weights from `Backend/toxic_model/model.pt`
