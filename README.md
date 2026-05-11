# 🚀 YZTA 2026 Datathon - Grup 27

Bu depo, YZTA 2026 Datathon yarışması kapsamında **Grup 27** tarafından geliştirilen makine öğrenmesi çözümlerini içermektedir. Amacımız, verilen veri seti üzerinde en yüksek tahminleme başarısını yakalarken, temiz ve sürdürülebilir bir kod mimarisi sunmaktır.

## 👥 Takım Üyeleri ve Roller

* **Murat:** Orchestrator (Proje Yönetimi ve Kaggle Submission)
* **Sezin:** Feature Engineering (Özellik Mühendisliği)
* **Buse:** Model Development (Model Geliştirme - XGBoost, LightGBM)
* **Eray:** Validation & Ensemble (Çapraz Doğrulama ve Model Birleştirme)
* **Abdülaziz:** Documentation & Presentation (Dokümantasyon ve Final Notebook)

## 📁 Proje Yapısı

```text
├── data/                  # Veri setleri (GitHub'a yüklenmez)
├── notebooks/             # Jupyter notebook'lar (FINAL.ipynb buradadır)
├── reports/               # Deney takip tabloları (experiments.csv)
├── src/grup27/            # Ana kaynak kod klasörü
│   ├── features.py        # Veri işleme fonksiyonları
│   ├── models.py          # Model eğitim metotları
│   ├── validation.py      # Çapraz doğrulama stratejileri
│   └── ensemble.py        # Ağırlıklı birleştirme metotları
├── TEAM_RULES.md          # Takım çalışma sözleşmesi
└── requirements.txt       # Gerekli Python kütüphaneleri