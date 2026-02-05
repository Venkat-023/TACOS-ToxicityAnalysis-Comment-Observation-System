from fastapi import FastAPI
from pydantic import BaseModel
from toxic_model.model import predict

# -------------------------------------------------
# App initialization
# -------------------------------------------------
app = FastAPI(
    title="TACOS Backend",
    description="Toxicity Analysis & Comment Observation System",
    version="1.0"
)

# -------------------------------------------------
# Request schema
# -------------------------------------------------
class CommentRequest(BaseModel):
    comment: str


# -------------------------------------------------
# Health check
# -------------------------------------------------
@app.get("/")
def root():
    return {"status": "ok", "message": "TACOS backend is running"}


# -------------------------------------------------
# Moderation endpoint (USED BY STREAMLIT)
# -------------------------------------------------
@app.post("/moderate")
def moderate_comment(request: CommentRequest):
    """
    Input:
    {
        "comment": "some user comment"
    }

    Output:
    {
        "scores": { label: probability },
        "action": "ALLOW | WARN | BLOCK"
    }
    """

    # Get probability scores from model
    scores = predict(request.comment)

    # ---------------- Decision Logic ----------------
    THRESHOLD = 0.20

    hate_signal = (
        scores.get("identity_hate", 0)
        + scores.get("threat", 0)
        + scores.get("toxic", 0)
    )

    abuse_signal = (
        scores.get("toxic", 0)
        + scores.get("insult", 0)
        + scores.get("obscene", 0)
    )

    if hate_signal >= 0.45:
        action = "BLOCK"
    elif abuse_signal >= 0.35:
        action = "WARN"
    else:
        action = "ALLOW"
    return {
        "scores": scores,
        "action": action,
        "signals": {
            "hate_signal": hate_signal,
            "abuse_signal": abuse_signal
        }
    }
