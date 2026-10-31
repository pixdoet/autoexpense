from fastapi import FastAPI
from pydantic import BaseModel

from parse import parse_ocr

app = FastAPI()


@app.get("/")
async def get_root():
    return {"success": True, "message": "Autoexpense backend api!"}


class OCRText(BaseModel):
    text: str


@app.post("/parse")
async def get_parse(message: OCRText):
    return_value = parse_ocr.parse_ocr_amount(text=message.text)
    if return_value:
        return {"success": True, "message": "Found OCR values!", "values": return_value}
    else:
        return {"success": False, "message": "Internal error!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8050)
