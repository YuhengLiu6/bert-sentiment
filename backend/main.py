from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import BertTokenizerFast, BertForSequenceClassification
import torch

# 初始化 FastAPI 应用
app = FastAPI()

# 启用 CORS 解决 React 端调用接口时的跨域问题
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中建议只允许特定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 模型路径和标签映射
MODEL_DIR = "./sentiment_model"
label_map = {0: "negative", 1: "neutral", 2: "positive"}  # 请确保顺序与你的训练一致

# 加载 tokenizer 和模型
tokenizer = BertTokenizerFast.from_pretrained(MODEL_DIR)
model = BertForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()

# 输入/输出数据结构定义
class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    sentiment: str
    confidence: float

# 推理接口
@app.post("/predict", response_model=PredictionOut)
def predict_sentiment(data: TextIn):
    inputs = tokenizer(data.text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        pred_label_idx = torch.argmax(probs, dim=1).item()
        confidence = probs[0][pred_label_idx].item()

    sentiment_label = label_map[pred_label_idx]
    return PredictionOut(sentiment=sentiment_label, confidence=round(confidence, 4))
