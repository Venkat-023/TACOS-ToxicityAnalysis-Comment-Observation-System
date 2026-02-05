import torch
from model import model, tokenizer, LABEL_COLS, DEVICE

MAX_LEN = 128
THRESHOLD = 0.4

def predict(text):
    encoding = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=MAX_LEN,
        return_tensors="pt"
    )

    with torch.no_grad():
        input_ids = encoding["input_ids"].to(DEVICE)
        attention_mask = encoding["attention_mask"].to(DEVICE)

        logits = model(input_ids, attention_mask)
        probs = torch.sigmoid(logits).cpu().numpy()[0]

    results = {
        LABEL_COLS[i]: float(probs[i])
        for i in range(len(LABEL_COLS))
        if probs[i] >= THRESHOLD
    }

    return results


if __name__ == "__main__":
    text = "You are a useless idiot and nobody likes you"
    output = predict(text)

    print("Input:", text)
    print("Detected toxicity:", output)
