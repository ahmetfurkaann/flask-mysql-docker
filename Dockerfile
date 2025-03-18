# Resmi Python image'ını kullan
FROM python:3.11

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# Bağımlılıkları ve kodları kopyala
COPY requirements.txt ./
COPY app.py ./

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# .env dosyasını korumak için image içine kopyalama yerine dışarıdan yükle
CMD ["python", "app.py"]
