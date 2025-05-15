from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn
import database as db
from pydantic import BaseModel

# Fiyat güncelleme model tanımı
class UrunFiyatGuncelle(BaseModel):
    fiyat: float

# Veritabanını başlat
db.init_db()

app = FastAPI(title="Restoran Menü Sistemi")

# HTML klasörünü statik dosyalar olarak tanımlama
app.mount("/static", StaticFiles(directory="HTML"), name="static")

# Şablonlar için Jinja2 ayarları
templates = Jinja2Templates(directory="HTML")

# Web sayfaları için route'lar
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Ana sayfayı doğrudan HTML klasöründen servis et
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/index.html", response_class=HTMLResponse)
async def index_redirect(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/category.html", response_class=HTMLResponse)
async def category_page(request: Request):
    return templates.TemplateResponse("category.html", {"request": request})

@app.get("/admin.html", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# CSS dosyası için özel endpoint
@app.get("/style.css")
async def get_css():
    css_content = ""
    css_path = Path("HTML/style.css")
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
    return HTMLResponse(content=css_content, media_type="text/css")

# API Endpointleri
@app.get("/api/kategoriler", response_class=JSONResponse)
async def api_kategoriler():
    """Tüm kategorileri JSON formatında döndürür"""
    return db.get_kategoriler()

@app.get("/api/kategori/{kategori_id}", response_class=JSONResponse)
async def api_kategori(kategori_id: int):
    """Belirli bir kategoriyi ID'ye göre getirir"""
    kategori = db.get_kategori_by_id(kategori_id)
    if not kategori:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    return kategori

@app.get("/api/urunler/{kategori_id}", response_class=JSONResponse)
async def api_urunler_by_kategori(kategori_id: int):
    """Belirli bir kategoriye ait ürünleri getirir"""
    urunler = db.get_urunler_by_kategori(kategori_id)
    return urunler

@app.get("/api/urun/{urun_id}", response_class=JSONResponse)
async def api_urun(urun_id: int):
    """ID'ye göre bir ürünü getirir"""
    urun = db.get_urun_by_id(urun_id)
    if not urun:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı")
    return urun

@app.post("/api/urun/update/{urun_id}", response_class=JSONResponse)
async def api_update_urun_fiyat(urun_id: int, fiyat_bilgi: UrunFiyatGuncelle):
    """Ürün fiyatını günceller"""
    if fiyat_bilgi.fiyat <= 0:
        raise HTTPException(status_code=400, detail="Fiyat pozitif bir değer olmalıdır")
    
    success, result = db.update_urun_fiyat(urun_id, fiyat_bilgi.fiyat)
    
    if not success:
        raise HTTPException(status_code=404, detail=result)
    
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)




