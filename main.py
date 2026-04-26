from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Vinasumo AI Industrial System")

# Catalog sản phẩm mẫu
CATALOG = {
    "quat_vuong": {"name": "Quạt hút vuông công nghiệp", "models": ["1380x1380", "1100x1100"]},
    "may_lam_mat": {"name": "Máy làm mát TM-18TA", "flow": 18000, "power": "1.1kW"},
    "ly_tam": {"name": "Quạt ly tâm cao áp", "flow_max": 24000, "power": "11kW-15kW"}
}

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Vinasumo AI Online", "contact": "0829483868"}

@app.post("/ai-consultant")
async def ai_consultant(req: ChatRequest):
    msg = req.message.lower()
    
    # Logic tư vấn kỹ sư cho phòng sơn
    if "7*4*2.6m" in msg or "phòng sơn" in msg:
        return {
            "reply": "Chào anh, với phòng sơn 7x4x2.6m, kỹ thuật Vinasumo tư vấn cấu hình: Cấp 5.5kW (15.500 m3/h) để bù áp, Hút 4kW + Lọc trần F5 600G + Lọc sàn sợi thủy tinh. Đây là giải pháp tối ưu để chốt sale cho hệ sơn này. Anh có muốn em xuất báo giá PDF ngay không?",
            "quote_id": "QUOTE-SON-001",
            "contact": "0829483868"
        }
    
    # Logic tư vấn quạt ly tâm
    if "24000m3/h" in msg:
        return {
            "reply": "Với lưu lượng 24.000 m3/h, bên em đang có dòng quạt ly tâm công suất 11kW – 15kW. Áp suất đạt 3500Pa, cực bền cho hệ thống hút bụi xưởng. Anh để lại số em gửi thông số chi tiết qua Zalo nhé.",
            "product": CATALOG["ly_tam"]
        }

    return {"reply": "Em là Trợ lý Kỹ sư Vinasumo. Anh cần tính toán lưu lượng xưởng, báo giá quạt hút vuông hay thiết kế hệ thống lọc mùi VOC?"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
