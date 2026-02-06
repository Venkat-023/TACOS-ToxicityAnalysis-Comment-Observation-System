# TACOS – Toxicity Analysis Comment Observation System

This project presents a **machine-learning-based text moderation system** for detecting toxic, abusive, and harmful comments in online user-generated content.  
It leverages **Transformer-based Natural Language Processing (NLP) models** to understand contextual meaning, intent, and tone in text rather than relying on simple keyword filtering.  
A **Streamlit** interface enables real-time comment analysis and instant visualization of toxicity predictions.

---

## Intuition

Online platforms generate enormous volumes of comments every second, making manual moderation impractical.  
Traditional rule-based systems fail to identify implicit toxicity such as sarcasm, indirect insults, or context-dependent hate speech.  
TACOS treats toxicity detection as a **supervised text classification problem** and applies **pre-trained Transformer models** that understand semantic context and intent.  
By fine-tuning these models on real-world toxic comment datasets, the system generalizes effectively to unseen content and provides scalable moderation support.

---

## Features
- **Real-Time Comment Analysis**: Enter comments and instantly detect toxicity
- **DistilBERT-Based NLP Model**: Lightweight Transformer model optimized for fast and accurate toxicity detection
- **Multi-Class Toxicity Detection**:
  - Toxic
  - Severe Toxic
  - Obscene
  - Threat
  - Insult
  - Identity Hate
- **Confidence Scores**: Probability values for each toxicity category
- **Interactive UI**: Clean and user-friendly Streamlit interface
- **Modular Architecture**: Separate backend and frontend for scalability

---

### Dataset used -[Jigsaw Toxic Comment Classification Dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Venkat-023/TACOS-ToxicityAnalysis-Comment-Observation-System
cd TACOS-ToxicityAnalysis-Comment-Observation-System
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

---

## Usage

### Running the Application

Start the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at:
```
http://localhost:8501
```
---

## Workflow

1. The user uploads an image and enters a comment.
2. On clicking **Post Comment**, the comment is sent to the backend for toxicity analysis.
3. Based on the prediction:
   - **ALLOW**: Comment is posted.
   - **BLOCK**: Comment is blocked and toxicity scores are shown.
4. Blocked comments can be edited or discarded by the user.

This workflow enables real-time comment moderation with user feedback and correction support.

---

## Future Scope
- Multilingual toxicity detection
- Explainable AI for highlighting toxic phrases
- Integration with social media platforms
- Deployment as a REST API or browser extension

---

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

---
