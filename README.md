# MySQL Bağlantı Uygulaması

Bu uygulama, MySQL veritabanına bağlanan ve verileri API üzerinden sunan iki Flask uygulamasından oluşmaktadır.

## API Route'leri

### Ana Flask Uygulaması (`s_flask`)
- `/`: Ana sayfa, `"hello index"` mesajını döndürür.
- `/kisiler`: MySQL veritabanındaki `kisiler` tablosundaki tüm verileri JSON formatında döndürür.
- `/cevap`: İkinci Flask uygulamasına (`s_flask2`) istek atarak dönen cevabı gösterir.

### İkinci Flask Uygulaması (`s_flask2`)
- `/`: `"Başka bir flask uygulamasından merhaba"` mesajını döndürür.

## Docker ile Çalıştırma

1. Projeyi klonlayın:
   ```bash
   git clone <repo-url>
   cd <repo-adı>
   ```

2. `.env` dosyasını oluşturun ve aşağıdaki değişkenleri ekleyin:
   ```ini
   DB_HOST=c_mysql
   DB_USER=root
   DB_PASSWORD=rootpassword
   DB_NAME=deneme
   ```

3. Docker Compose ile uygulamayı başlatın:
   ```bash
   docker-compose up --build
   ```

4. Çalışan container’ları görmek için:
   ```bash
   docker ps
   ```

5. Eğer hata alırsanız, önce eski container’ları temizleyip yeniden başlatabilirsiniz:
   ```bash
   docker-compose down
   docker-compose up --build
   ```

Uygulamalar varsayılan olarak aşağıdaki adreslerde çalışacaktır:

- **Ana Flask Uygulaması (`s_flask`)**: [http://localhost:3030](http://localhost:3030)
- **İkinci Flask Uygulaması (`s_flask2`)**: [http://localhost:3031](http://localhost:3031)

## Veritabanı Bilgileri

- **Host:** c_mysql
- **Port:** 3306
- **Kullanıcı:** root
- **Şifre:** rootpassword
- **Veritabanı:** deneme
