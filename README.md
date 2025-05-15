# Restoran Menü Sistemi

Bu proje, bir restoranın dijital menü sistemini FastAPI kullanarak web üzerinden servis eder. Tüm içerik SQLite veritabanından yüklenir ve admin girişi ile fiyat güncelleme özelliğine sahiptir.

## Kurulum

1. Gerekli paketleri yükleyin:
```
pip install -r requirements.txt
```

2. Uygulamayı çalıştırın:
```
python main.py
```

3. Tarayıcınızda şu adresi açın:
```
http://localhost:8000
```

## Özellikler

- Modern ve şık kullanıcı arayüzü
- **Tamamen veritabanına dayalı menü sistemi**: 
  - Tüm içerik veritabanından dinamik olarak yüklenir
  - Kategoriler ve alt kategoriler hiyerarşik olarak görüntülenir
  - Ürünler resimleriyle birlikte gösterilir

- **Ana Kategori Yapısı**:
  - Yemekler (Başlangıçlar, Ana Yemekler, Salatalar)
  - İçecekler (Sıcak İçecekler, Soğuk İçecekler)
  - Tatlılar (Sütlü Tatlılar, Şerbetli Tatlılar)

- **Admin Paneli**:
  - Kullanıcı adı/şifre ile giriş (admin/admin123)
  - Ürün fiyatlarını güncelleme özelliği
  - Yetkisiz erişim kontrolü

## Veritabanı Yapısı

- `kategoriler` tablosu: Menü kategorileri (ana ve alt kategoriler)
- `urunler` tablosu: Yemek, içecek ve tatlı ürünleri

## API Endpointleri

- `/api/kategoriler` - Tüm kategorileri listeler
- `/api/kategori/{kategori_id}` - Belirli bir kategoriyi getirir
- `/api/urunler/{kategori_id}` - Kategori ID'sine göre ürünleri listeler
- `/api/urun/{urun_id}` - ID'ye göre bir ürünü getirir
- `/api/urun/update/{urun_id}` - Ürün fiyatını günceller (POST)

## Sayfalar

- `index.html` - Ana sayfa, tüm ana kategorilere bağlantılar içerir
- `category.html` - Seçilen kategorinin alt kategorilerini ve ürünlerini gösterir
- `admin.html` - Admin giriş ve fiyat güncelleme sayfası

## Teknolojiler

- Backend:
  - FastAPI
  - SQLite
  - Jinja2 Templates
- Frontend:
  - HTML
  - CSS
  - JavaScript
  - Modern responsive tasarım

## Ekran Görüntüleri

- Ana sayfa: Modern menü butonları ve karşılama mesajı
- Veritabanı menüsü: Tüm kategoriler ve ürünler tek sayfada
- Admin paneli: Güvenli giriş ekranı ve fiyat güncelleme formları 