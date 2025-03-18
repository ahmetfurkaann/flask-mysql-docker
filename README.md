# MySQL Bağlantı Uygulaması

Bu uygulama, MySQL veritabanına bağlanan ve verileri API üzerinden sunan basit bir Flask uygulamasıdır.

## API Route'leri

- `/`: Ana sayfa, "hello index" mesajını döndürür
- `/kisiler`: MySQL veritabanındaki kisiler tablosundaki tüm verileri JSON formatında döndürür

## Docker ile Çalıştırma

1. Projeyi klonlayın
2. `.env` dosyasını oluşturun ve aşağıdaki değişkenleri ekleyin:
   ```
   DB_HOST=c_mysql
   DB_USER=root
   DB_PASSWORD=rootpassword
   DB_NAME=deneme
   ```
3. Docker Compose ile uygulamayı başlatın:
   ```bash
   docker-compose up --build
   ```

Uygulama varsayılan olarak `http://localhost:3030` adresinde çalışacaktır.

## Veritabanı Bilgileri

- Host: c_mysql
- Port: 3306
- Kullanıcı: root
- Şifre: rootpassword
- Veritabanı: deneme 