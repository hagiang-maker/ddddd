from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

# LỆNH QUAN TRỌNG: Mở giao diện khi khách vào web
@app.get("/")
async def read_index():
    return FileResponse('index.html')

# LỆNH QUAN TRỌNG: Dự phòng cho link /index.html
@app.get("/index.html")
async def read_index_alt():
    return FileResponse('index.html')

@app.post("/ai-consultant")
async def ai_consultant(req: ChatRequest):
    msg = req.message.lower()
    if "7*4*2.6m" in msg or "phòng sơn" in msg:
        return {"reply": "Chào anh, với phòng sơn 7x4x2.6m, kỹ thuật Vinasumo tư vấn: Cấp 5.5kW (15.500m3/h) bù áp, Hút 4kW + Lọc trần F5 + Lọc sàn thủy tính. Anh cần báo giá qua Zalo 0829483868 không?"}
    return {"reply": "Chào anh, em là AI kỹ sư Vinasumo. Anh cần tính toán lưu lượng xưởng hay báo giá loại quạt nào ạ?"}
