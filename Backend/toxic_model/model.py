from pathlib import Path
import torch
import torch.nn as nn
from transformers import DistilBertConfig, DistilBertModel, DistilBertTokenizerFast

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
LABEL_COLS = [
    "toxic",
    "severe_toxic",
    "obscene",
    "threat",
    "insult",
    "identity_hate"
]

MAX_LEN = 128  # MUST match training
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -------------------------------------------------------------------
# Model Definition
# -------------------------------------------------------------------
class DistilBertMultiLabel(nn.Module):
    def __init__(self):
        super().__init__()
        # Build the base architecture locally so container startup does not
        # depend on downloading model weights from the internet.
        self.bert = DistilBertModel(DistilBertConfig())
        self.dropout = nn.Dropout(0.3)
        self.classifier = nn.Linear(
            self.bert.config.hidden_size,
            len(LABEL_COLS)
        )

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        pooled = outputs.last_hidden_state[:, 0]
        pooled = self.dropout(pooled)
        logits = self.classifier(pooled)
        return logits

# -------------------------------------------------------------------
# Load Tokenizer (MUST match training)
# -------------------------------------------------------------------
tokenizer = DistilBertTokenizerFast.from_pretrained(
    BASE_DIR,
    local_files_only=True
)

# -------------------------------------------------------------------
# Load Model Weights
# -------------------------------------------------------------------
model = DistilBertMultiLabel()
model.load_state_dict(
    torch.load(BASE_DIR / "model.pt", map_location=DEVICE)
)
model.to(DEVICE)
model.eval()

# -------------------------------------------------------------------
# Inference Helper (Used by FastAPI)
# -------------------------------------------------------------------
def predict(text: str) -> dict:
    """
    Takes raw text and returns probability scores for each toxicity label.
    """

    encoding = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=MAX_LEN,
        return_tensors="pt"
    )

    encoding = {k: v.to(DEVICE) for k, v in encoding.items()}

    with torch.no_grad():
        logits = model(
            input_ids=encoding["input_ids"],
            attention_mask=encoding["attention_mask"]
        )
        probs = torch.sigmoid(logits).cpu().numpy()[0]

    return {
        LABEL_COLS[i]: float(probs[i])
        for i in range(len(LABEL_COLS))
    }
