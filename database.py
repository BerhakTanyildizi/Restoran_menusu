import sqlite3
from pathlib import Path

# Veritabanı dosyasının yolu
DATABASE_PATH = "restoran.db"

def create_tables():
    """Veritabanı tablolarını oluşturur"""
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    # Kategori tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kategoriler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        aciklama TEXT,
        ana_kategori_id INTEGER NULL,
        FOREIGN KEY (ana_kategori_id) REFERENCES kategoriler (id)
    )
    ''')
    # Ürün tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS urunler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        fiyat REAL NOT NULL,
        aciklama TEXT,
        resim_url TEXT,
        kategori_id INTEGER NOT NULL,
        FOREIGN KEY (kategori_id) REFERENCES kategoriler (id)
    )
    ''')
    
    conn.commit()
    conn.close()
    
def populate_sample_data():
    """Örnek verileri veritabanına ekler"""
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Ana kategorileri ekle
    ana_kategoriler = [
        ("Yemekler", "Ana yemek kategorisi"),
        ("İçecekler", "İçecek kategorisi"),
        ("Tatlılar", "Tatlı kategorisi")
    ]
    
    cursor.executemany("INSERT INTO kategoriler (ad, aciklama) VALUES (?, ?)", ana_kategoriler)
    
    # Alt kategorileri ekle
    alt_kategoriler = [
        ("Başlangıçlar", "Başlangıç yemekleri", 1),
        ("Ana Yemekler", "Ana yemek çeşitleri", 1),
        ("Salatalar", "Salata çeşitleri", 1),
        ("Sıcak İçecekler", "Sıcak içecek çeşitleri", 2),
        ("Soğuk İçecekler", "Soğuk içecek çeşitleri", 2),
        ("Sütlü Tatlılar", "Sütlü tatlı çeşitleri", 3),
        ("Şerbetli Tatlılar", "Şerbetli tatlı çeşitleri", 3)
    ]
    
    cursor.executemany("INSERT INTO kategoriler (ad, aciklama, ana_kategori_id) VALUES (?, ?, ?)", alt_kategoriler)
    
    # Örnek ürünleri ekle - Ana Yemekler
    ana_yemekler = [
        ("Izgara Tavuk", 120, "Özel baharatlarla marine edilmiş ızgara tavuk", "https://images.unsplash.com/photo-1600891964599-f61ba0e24092", 5),
        ("Köfte", 110, "El yapımı köfte", "https://images.unsplash.com/photo-1529042410759-befb1204b468", 5),
        ("Makarna", 90, "İtalyan usulü makarna", "https://images.unsplash.com/photo-1473093295043-cdd812d0e601", 5),
        ("Pizza", 130, "Karışık pizza", "https://images.unsplash.com/photo-1513104890138-7c749659a591", 5),
        ("Balık Izgara", 150, "Günün balığı ızgara", "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2", 5),
        ("Lazanya", 125, "Ev yapımı lazanya", "https://images.unsplash.com/photo-1574894709920-11b28e7367e3", 5),
        ("Sebzeli Noodle", 100, "Taze sebzeli noodle", "https://images.unsplash.com/photo-1552611052-33e04de081de", 5),
        ("Mantı", 95, "Yoğurtlu mantı", "https://images.unsplash.com/photo-1661604580970-e8a62c26807e", 5),
        ("Karnabahar Kızartması", 85, "Baharatlı karnabahar kızartması", "https://images.unsplash.com/photo-1640719028782-8230f1bdc56f", 5),
        ("Karnıyarık", 105, "Geleneksel karnıyarık", "https://images.unsplash.com/photo-1625938145744-e380515399fa", 5)
    ]
    
    cursor.executemany("INSERT INTO urunler (ad, fiyat, aciklama, resim_url, kategori_id) VALUES (?, ?, ?, ?, ?)", ana_yemekler)
    
    # Örnek ürünleri ekle - Soğuk İçecekler
    soguk_icecekler = [
        ("Ayran", 30, "Ev yapımı ayran", "https://images.unsplash.com/photo-1626078437375-99379dd55ae3", 8),
        ("Kola", 40, "Coca Cola", "https://images.unsplash.com/photo-1554866585-cd94860890b7", 8),
        ("Limonata", 45, "Ev yapımı limonata", "https://images.unsplash.com/photo-1523703591032-c582f1eefc25", 8),
        ("Portakal Suyu", 35, "Taze sıkılmış portakal suyu", "https://images.unsplash.com/photo-1600271886742-f049cd451bba", 8),
        ("Ice Tea", 35, "Şeftali aromalı ice tea", "https://images.unsplash.com/photo-1556679343-c1917e0fbcc9", 8),
        ("Smoothie", 55, "Taze meyveli smoothie", "https://images.unsplash.com/photo-1553530666-ba11a90bb0ae", 8),
        ("Soda", 25, "Meyveli soda", "https://images.unsplash.com/photo-1603569283847-aa295f0d016a", 8),
        ("Milkshake", 60, "Çikolatalı milkshake", "https://images.unsplash.com/photo-1568901839119-631418a3910d", 8),
        ("Soğuk Kahve", 50, "Buzlu americano", "https://images.unsplash.com/photo-1517959105821-eaf2591984ca", 8),
        ("Maden Suyu", 20, "Doğal maden suyu", "https://images.unsplash.com/photo-1520006403909-838d6b92c22e", 8)
    ]
    
    cursor.executemany("INSERT INTO urunler (ad, fiyat, aciklama, resim_url, kategori_id) VALUES (?, ?, ?, ?, ?)", soguk_icecekler)
    
    # Örnek ürünleri ekle - Sıcak İçecekler
    sicak_icecekler = [
        ("Türk Kahvesi", 35, "Geleneksel Türk kahvesi", "https://images.unsplash.com/photo-1598908314732-07113901949e", 7),
        ("Espresso", 30, "İtalyan usulü espresso", "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04", 7),
        ("Americano", 40, "Sıcak su ile inceltilmiş espresso", "https://images.unsplash.com/photo-1635213748264-6690cc3615b6", 7),
        ("Cappuccino", 45, "Espresso, süt ve süt köpüğü", "https://images.unsplash.com/photo-1572442388796-11668a67e53d", 7),
        ("Latte", 45, "Espresso ve buharlanmış süt", "https://images.unsplash.com/photo-1587401098761-a292e46999aa", 7),
        ("Sıcak Çikolata", 40, "Kremsi sıcak çikolata", "https://images.unsplash.com/photo-1542990254-19864e577b4e", 7),
        ("Chai Tea Latte", 45, "Baharatlı chai çayı ve süt", "https://images.unsplash.com/photo-1549241520-425e3dfc01cb", 7),
        ("Filtre Kahve", 35, "Geleneksel filtre kahve", "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085", 7),
        ("Ihlamur Çayı", 30, "Bitki çayı", "https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9", 7),
        ("Adaçayı", 30, "Taze adaçayı", "https://images.unsplash.com/photo-1525057965667-26419a4c4a74", 7),
        ("Yeşil Çay", 30, "Sağlıklı yeşil çay", "https://images.unsplash.com/photo-1627435601361-ec25f8e1d0b5", 7)
    ]
    
    cursor.executemany("INSERT INTO urunler (ad, fiyat, aciklama, resim_url, kategori_id) VALUES (?, ?, ?, ?, ?)", sicak_icecekler)
    
    # Örnek ürünleri ekle - Sütlü Tatlılar
    sutlu_tatlilar = [
        ("Sütlaç", 60, "Fırınlanmış sütlaç", "https://images.unsplash.com/photo-1565958953583-0da703bed0a5", 9),
        ("Kazandibi", 65, "Klasik kazandibi", "https://images.unsplash.com/photo-1643538554183-37111ca705cd", 9),
        ("Tavuk Göğsü", 55, "Klasik tavuk göğsü tatlısı", "https://images.unsplash.com/photo-1616645258469-ec681c17f3ee", 9),
        ("Muhallebi", 50, "Geleneksel muhallebi", "https://images.unsplash.com/photo-1623246123320-0d6636755796", 9),
        ("Trileçe", 70, "Üç süt ile hazırlanan karamelli tatlı", "https://images.unsplash.com/photo-1608047555433-28c4f3cc7be4", 9),
        ("Magnolia", 75, "Çikolatalı magnolia", "https://images.unsplash.com/photo-1551969014-7d2c4cddf0b6", 9),
        ("Profiterol", 70, "Çikolata soslu profiterol", "https://images.unsplash.com/photo-1623595119708-26b1f7500ddd", 9),
        ("Panna Cotta", 65, "Meyveli panna cotta", "https://images.unsplash.com/photo-1488477181946-6428a0291777", 9),
        ("Tiramisu", 80, "İtalyan usulü tiramisu", "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9", 9)
    ]
    
    cursor.executemany("INSERT INTO urunler (ad, fiyat, aciklama, resim_url, kategori_id) VALUES (?, ?, ?, ?, ?)", sutlu_tatlilar)
    
    # Örnek ürünleri ekle - Şerbetli Tatlılar
    serbetli_tatlilar = [
        ("Baklava", 75, "Fıstıklı baklava", "https://images.unsplash.com/photo-1625935267543-644fcd73a42e", 10),
        ("Künefe", 80, "Kadayıf ve peynirli künefe", "https://images.unsplash.com/photo-1679958158777-5d87aaa0d8aa", 10),
        ("Revani", 65, "Şerbetli revani", "https://images.unsplash.com/photo-1690131123573-00e44c050b8a", 10),
        ("Tulumba", 60, "Çıtır tulumba tatlısı", "https://images.unsplash.com/photo-1658473681884-8080713a74ac", 10),
        ("Şekerpare", 65, "Geleneksel şekerpare", "https://images.unsplash.com/photo-1569383549104-64908ac55522", 10),
        ("Kadayıf", 70, "Cevizli kadayıf", "https://images.unsplash.com/photo-1576175468911-dfefb4888e23", 10),
        ("Fıstıklı Sarma", 85, "Fıstıklı sarma tatlısı", "https://images.unsplash.com/photo-1582263352657-ddda9a04787f", 10),
        ("Burma Kadayıf", 75, "Geleneksel burma kadayıf", "https://images.unsplash.com/photo-1623428454614-abaf7c8690ef", 10),
        ("Cevizli Baklava", 70, "Cevizli ev yapımı baklava", "https://images.unsplash.com/photo-1485963631004-f2f00b1d6606", 10)
    ]
    
    cursor.executemany("INSERT INTO urunler (ad, fiyat, aciklama, resim_url, kategori_id) VALUES (?, ?, ?, ?, ?)", serbetli_tatlilar)
    
    # Örnek ürünleri ekle - Başlangıçlar
    baslangiclar = [
        ("Mercimek Çorbası", 40, "Geleneksel Türk mercimek çorbası", "https://images.unsplash.com/photo-1547592166-23ac45744acd", 4),
        ("Humus", 45, "Nohut ezmesi", "https://images.unsplash.com/photo-1593007791459-4b05e1158229", 4),
        ("Sigara Böreği", 55, "Peynirli sigara böreği", "https://images.unsplash.com/photo-1589187151053-5ec8818e661b", 4),
        ("Çıtır Kalamari", 65, "Çıtır kalamar halkaları", "https://images.unsplash.com/photo-1599147977231-d42ef16ad4fa", 4),
        ("Patates Kızartması", 50, "Çıtır patates kızartması", "https://images.unsplash.com/photo-1623238914334-3042187b5bf6", 4),
        ("Paçanga Böreği", 60, "Pastırmalı paçanga böreği", "https://images.unsplash.com/photo-1618040996337-28944ba054bb", 4),
        ("Mantar Sote", 55, "Tereyağında sotelenmiş mantar", "https://images.unsplash.com/photo-1611891745509-8c552daac164", 4),
        ("Arnavut Ciğeri", 70, "Soğanlı Arnavut ciğeri", "https://images.unsplash.com/photo-1630698467933-60119dad6e64", 4),
        ("Zeytinyağlı Yaprak Sarma", 60, "Zeytinyağlı pirinçli yaprak sarma", "https://images.unsplash.com/photo-1624555630566-606cedc77010", 4)
    ]
    
    cursor.executemany("INSERT INTO urunler (ad, fiyat, aciklama, resim_url, kategori_id) VALUES (?, ?, ?, ?, ?)", baslangiclar)
    
    # Örnek ürünleri ekle - Salatalar
    salatalar = [
        ("Sezar Salata", 70, "Tavuklu sezar salata", "https://images.unsplash.com/photo-1550304943-4f24f54ddde9", 6),
        ("Akdeniz Salata", 65, "Zeytinli, peynirli akdeniz salatası", "https://images.unsplash.com/photo-1540420773420-3366772f4999", 6),
        ("Ton Balıklı Salata", 75, "Ton balıklı yeşil salata", "https://images.unsplash.com/photo-1511357840105-cde01bdc7be8", 6),
        ("Çoban Salatası", 55, "Klasik çoban salatası", "https://images.unsplash.com/photo-1644944075287-c28012dce4a0", 6),
        ("Kinoa Salatası", 80, "Kinoa ve taze sebzelerle hazırlanmış", "https://images.unsplash.com/photo-1544378358-230db1ea627c", 6),
        ("Roka Salatası", 60, "Parmesan peynirli roka salatası", "https://images.unsplash.com/photo-1604909052743-94e838986d24", 6),
        ("Tavuklu Semizotu Salatası", 70, "Tavuklu semizotu salatası", "https://images.unsplash.com/photo-1626200930896-4c35d594de6b", 6),
        ("Yoğurtlu Havuç Salatası", 55, "Yoğurtlu havuç ve ceviz salatası", "https://images.unsplash.com/photo-1522676373813-e5d0d35d7ab8", 6),
        ("Yeşil Salata", 50, "Mevsim yeşillikleri salatası", "https://images.unsplash.com/photo-1512621776951-a57141f2eefd", 6)
    ]
    
    cursor.executemany("INSERT INTO urunler (ad, fiyat, aciklama, resim_url, kategori_id) VALUES (?, ?, ?, ?, ?)", salatalar)
    
    conn.commit()
    conn.close()

def get_kategoriler():
    """Tüm kategorileri getirir"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM kategoriler WHERE ana_kategori_id IS NULL")
    ana_kategoriler = cursor.fetchall()
    
    result = []
    for kategori in ana_kategoriler:
        kategori_dict = dict(kategori)
        cursor.execute("SELECT * FROM kategoriler WHERE ana_kategori_id = ?", (kategori['id'],))
        alt_kategoriler = cursor.fetchall()
        kategori_dict['alt_kategoriler'] = [dict(k) for k in alt_kategoriler]
        result.append(kategori_dict)
    
    conn.close()
    return result

def get_kategori_by_id(kategori_id):
    """ID'ye göre kategori bilgisini getirir"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM kategoriler WHERE id = ?", (kategori_id,))
    kategori = cursor.fetchone()
    
    conn.close()
    return dict(kategori) if kategori else None

def get_urunler_by_kategori(kategori_id):
    """Kategori ID'sine göre ürünleri getirir"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM urunler WHERE kategori_id = ?", (kategori_id,))
    urunler = cursor.fetchall()
    
    conn.close()
    return [dict(urun) for urun in urunler]

def get_urun_by_id(urun_id):
    """ID'ye göre ürün bilgisini getirir"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM urunler WHERE id = ?", (urun_id,))
    urun = cursor.fetchone()
    
    conn.close()
    return dict(urun) if urun else None

def update_urun_fiyat(urun_id, yeni_fiyat):
    """Ürün fiyatını günceller"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE urunler SET fiyat = ? WHERE id = ?", (yeni_fiyat, urun_id))
    conn.commit()
    
    # Etkilenen satır sayısını kontrol et
    if cursor.rowcount < 1:
        conn.close()
        return False, "Ürün bulunamadı"
    
    conn.close()
    
    # Güncellenmiş ürünü getir
    urun = get_urun_by_id(urun_id)
    if not urun:
        return False, "Ürün güncellendi fakat getirilemedi"
    
    return True, urun

# Veritabanını sıfırla ve yeniden oluştur
def reset_db():
    """Veritabanını sıfırlar ve yeniden oluşturur"""
    if Path(DATABASE_PATH).exists():
        Path(DATABASE_PATH).unlink()  # Dosyayı sil
    create_tables()
    populate_sample_data()
    print(f"Veritabanı sıfırlandı ve yeniden oluşturuldu: {DATABASE_PATH}")

# Veritabanı dosyası yoksa, tabloları ve örnek verileri oluştur
def init_db():
    if not Path(DATABASE_PATH).exists():
        create_tables()
        populate_sample_data()
        print(f"Veritabanı oluşturuldu: {DATABASE_PATH}")
    else:
        print(f"Veritabanı zaten mevcut: {DATABASE_PATH}")

# Veritabanını başlat
if __name__ == "__main__":
    reset_db()  # Veritabanını sıfırla ve yeniden oluştur 
    
    
    