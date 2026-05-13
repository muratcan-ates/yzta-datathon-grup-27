<div align="center">

# 🧠 YZTA 2026 Datathon — Grup 27

### Bilişsel Performans Skoru Tahmini

**YZTA 5. Akademi Dönemi · Veri Bilimi Datathon · Mayıs 2026**

<br/>

<p align="center">
  <a href="#-proje-özeti"><strong>Proje Özeti</strong></a> ·
  <a href="#-yarışma-yaklaşımı"><strong>Yaklaşım</strong></a> ·
  <a href="#-sonuçlar"><strong>Sonuçlar</strong></a> ·
  <a href="#-kurulum"><strong>Kurulum</strong></a> ·
  <a href="#-reprodüksiyon"><strong>Reprodüksiyon</strong></a>
</p>

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-4.6-02569B?style=for-the-badge)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.3-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-Submitted-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)

<br/>

![GitHub last commit](https://img.shields.io/github/last-commit/muratcan-ates/yzta-datathon-grup-27?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/muratcan-ates/yzta-datathon-grup-27?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/muratcan-ates/yzta-datathon-grup-27?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/muratcan-ates/yzta-datathon-grup-27?style=flat-square)

</div>

<br/>

---

## 📖 İçindekiler

- [🎯 Proje Özeti](#-proje-özeti)
- [📋 Yarışma Yaklaşımı](#-yarışma-yaklaşımı)
- [👥 Takım](#-takım)
- [🛠️ Kullanılan Teknolojiler](#️-kullanılan-teknolojiler)
- [📊 Sonuçlar](#-sonuçlar)
- [🔬 Veri ve Ön İşleme](#-veri-ve-ön-işleme)
- [🏗️ Pipeline Mimarisi](#️-pipeline-mimarisi)
- [⚠️ Kapsam ve Sınırlamalar](#️-kapsam-ve-sınırlamalar)
- [🚀 Kurulum](#-kurulum)
- [🔁 Reprodüksiyon](#-reprodüksiyon)
- [📁 Proje Yapısı](#-proje-yapısı)
- [📝 Lisans](#-lisans)

<br/>

---

## 🎯 Proje Özeti

Bu depo, **YZTA 5. Akademi Dönemi Datathon yarışması** kapsamında Grup 27 tarafından geliştirilen makine öğrenmesi çözümünü içermektedir.

**Problem:** Bireylerin uyku, yaşam tarzı ve demografik özelliklerinden yola çıkarak **bilişsel performans skorlarını (`bilissel_performans_skoru`, 0-10 aralığında sürekli değer)** tahmin etmek.

**Yaklaşımımız:** LightGBM tabanlı, 5-fold KFold çapraz doğrulama ile eğitilmiş tek modelli bir regresyon pipeline'ı. Kategorik değişkenler LightGBM'in native categorical handling özelliğiyle işlendi; manuel encoding yapılmadı. Sonuç, Kaggle'a submit edilebilir formatta `submissions/` klasöründe.

**Tek cümleyle:** Train + test CSV'lerini al → preprocessing + 5-fold LightGBM → out-of-fold tahmin + Kaggle submission CSV.

<br/>

---

## 📋 Yarışma Yaklaşımı

### Değerlendirme

- **Metrik:** RMSE (Root Mean Squared Error)
- **Format:** Kaggle competition (`yzta-2026-datathon`)
- **Submission limiti:** Günde 3 submission, finalde 2 best seçilir
- **Public/Private split:** %50 / %50 (random)

### Stratejik Kararlar

| Karar | Gerekçe |
|-------|---------|
| Tek model (LightGBM) | Zaman kısıtı + variance kontrol |
| 5-fold KFold (shuffled) | Bias-variance trade-off için yeterli, time-series değil |
| Native categorical handling | One-hot encoding'e kıyasla ~%3 daha iyi RMSE |
| Early stopping (100 rounds) | Overfit önleme, ortalama best_iter ~190 |
| Median + std değil mean blend | 5-fold mean test prediction averaging |

<br/>

---

## 👥 Takım

- **Muratcan Ateş** ([@muratcan-ates](https://github.com/muratcan-ates)) — Orchestrator / ML Engineer
- **Sezin Tarlığ** ([@sezintarlig](https://github.com/sezintarlig)) — Data Analyst / EDA
- **Buse Gülçen** ([@busegulcenn](https://github.com/busegulcenn)) — Feature Engineering
- **Abdülaziz Kıran** ([@Abdulaziz-kiran](https://github.com/Abdulaziz-kiran)) — Documentation
- **Eray Güler** ([@erayglr](https://github.com/erayglr)) — Takım Üyesi

<br/>

---

## 🛠️ Kullanılan Teknolojiler

| Katman | Teknoloji | Sürüm | Neden? |
|--------|-----------|:-----:|--------|
| **Dil** | Python | 3.11 | Veri bilimi standardı |
| **Veri** | pandas, numpy | 2.3, 2.0+ | Veri okuma ve nümerik işlemler |
| **ML** | LightGBM | 4.6 | Gradient boosting, native categorical handling, hızlı eğitim |
| **Validation** | scikit-learn KFold | 1.7 | 5-fold CV ile robust OOF tahmin |
| **Notebook** | Jupyter | 1.1 | EDA ve baseline geliştirme |
| **Versiyon Kontrol** | Git + GitHub | — | Çoklu branch + PR workflow |

Tüm bağımlılıklar `requirements.txt` içinde sürümlenmiştir.

<br/>

---

## 📊 Sonuçlar

### Baseline Model (LightGBM 5-Fold)

| Metrik | Değer |
|--------|:-----:|
| **OOF RMSE** | **1.22924** |
| Mean fold RMSE | 1.22921 (±0.00968) |
| Eğitim süresi | 17.2 saniye (5 fold, ~190 iter/fold) |
| Kaggle Public Score | **1.21440** |

### Fold Bazlı Sonuçlar

| Fold | RMSE | Best Iteration |
|:----:|:----:|:--------------:|
| 1 | 1.22917 | 170 |
| 2 | 1.22885 | 228 |
| 3 | 1.21558 | 229 |
| 4 | 1.22662 | 161 |
| 5 | 1.24581 | 177 |

**Yorum:** Fold-bazlı RMSE değerleri **çok düşük variance** gösteriyor (±0.01). Bu, modelin farklı veri dilimlerinde tutarlı çalıştığına ve overfitting olmadığına işaret eder. Public score (1.21440), OOF'den (1.22924) biraz daha iyi geldi — beklendiği gibi, train/test dağılımları örtüşüyor.

### Submission Geçmişi

| Tarih | Model | OOF RMSE | Public Score |
|-------|-------|:--------:|:------------:|
| 13 Mayıs 2026 | LightGBM 5-fold baseline | 1.22924 | **1.21440** |

> 📝 *Bu README, geliştirme süreci boyunca güncellenecektir. Yeni submission'lar ve iyileştirmeler eklendiğinde tablo genişletilecektir.*

<br/>

---

## 🔬 Veri ve Ön İşleme

### Veri Seti

| Özellik | Değer |
|---------|-------|
| Train satır sayısı | 56,000 |
| Test satır sayısı | 24,000 |
| Toplam öznitelik (feature) | 22 |
| Numerik öznitelikler | 15 |
| Kategorik öznitelikler | 7 |
| Hedef değişken | `bilissel_performans_skoru` (float, 0-10) |
| Eksik değer (train) | 9,372 |
| Eksik değer (test) | 4,068 |

### Hedef Dağılımı

- **Ortalama:** 5.913
- **Standart sapma:** 2.232
- **Min / Max:** 0.0 / 10.0
- **Çeyrekler:** 25% = 4.40, 50% = 6.03, 75% = 7.57

Dağılım normal-benzeri, hafif sola çarpık.

### Ön İşleme Adımları

1. **Train + test load** → `pandas.read_csv` ile yükleme
2. **Categorical encoding** → `object` dtype → `category` dtype dönüşümü (LightGBM native handling için)
3. **Missing value handling** → LightGBM native NaN handling (manuel imputation yok)
4. **Train/test categorical alignment** → Test'te train'de olmayan kategori yoktu (kontrol edildi)
5. **Feature/target split** → `id` ve hedef hariç tüm sütunlar feature olarak kullanıldı

<br/>

---

## 🏗️ Pipeline Mimarisi

```
data/raw/
  ├── train.csv (56000 satır)
  ├── test_x.csv (24000 satır)
  └── sample_submission.csv

         │
         ▼
┌─────────────────────────────────────┐
│  notebooks/02_baseline_lightgbm.ipynb │
│                                       │
│  1. Data load                         │
│  2. Categorical → category dtype      │
│  3. 5-fold KFold split (seed=42)      │
│                                       │
│  ┌───────────────────────────────┐   │
│  │ Fold 1-5 (her fold için):     │   │
│  │  ├ LightGBM train             │   │
│  │  ├ Early stopping (100)       │   │
│  │  ├ OOF prediction (validation)│   │
│  │  └ Test prediction (averaged) │   │
│  └───────────────────────────────┘   │
│                                       │
│  4. OOF RMSE hesapla                  │
│  5. Test predictions → clip(0, 10)    │
│  6. Submission CSV oluştur            │
└─────────────────┬─────────────────────┘
                  │
                  ▼
           submissions/
              └── sub_lgbm_5fold_oof1.2292_*.csv
                  → Kaggle upload
```

### LightGBM Hiperparametreleri

```python
{
    "objective": "regression",
    "metric": "rmse",
    "learning_rate": 0.05,
    "num_leaves": 63,
    "feature_fraction": 0.9,
    "bagging_fraction": 0.9,
    "bagging_freq": 5,
    "min_child_samples": 20,
    "seed": 42,
}
```

Bu değerler baseline default'tur — hyperparameter tuning (Optuna) bir sonraki iterasyona planlanmıştır.

<br/>

---

## ⚠️ Kapsam ve Sınırlamalar

Şeffaflık akademik bir prensiptir. Bu çözümün mevcut durumda **sınırlamalarını** açıkça belirtmek istiyoruz:

### Model Sınırlamaları

- **Tek model:** Sadece LightGBM kullanıldı. CatBoost, XGBoost gibi alternatif modeller veya bunların blend'i denenmedi.
- **Default hyperparameters:** Optuna gibi otomatik hyperparameter tuning yapılmadı. Manuel olarak seçilen değerler kullanıldı.
- **Feature engineering minimal:** Sezin ve Buse'nin geliştirdiği özel feature fonksiyonları (`src/grup27/features.py`) henüz baseline'a entegre edilmedi — bu, sonraki iterasyona planlanmıştır.

### Veri Sınırlamaları

- **Train/test dağılım analizi sınırlı:** Test setinin train'e ne kadar benzediği derinlemesine incelenmedi (KS test, distribution drift analizi yapılmadı).
- **Outlier handling yok:** Aykırı değerler tespit edilip işlenmedi.
- **Cross-validation strategy basit:** 5-fold KFold (shuffled) kullanıldı. Stratified KFold (binning) veya Repeated KFold daha robust olabilir.

### Sıralama Sınırlaması

Kaggle leaderboard'da yarışma kazananları **0.13-0.20 RMSE bandında** yer alıyor. Bizim mevcut skorumuz (**1.21440**) bu seviyenin çok altında. Bu fark, üst sıralardaki takımların muhtemelen **agresif feature engineering**, **multi-model ensemble** ve **kapsamlı hyperparameter tuning** uyguladığını gösteriyor. Mevcut baseline'ımız sağlam bir temel olarak korunmakla birlikte, bu boşluğu kapatmak için yukarıdaki "Sınırlamalar" maddelerinin ele alınması gerekiyor.

<br/>

---

## 🚀 Kurulum

### Ön Koşullar

- Python 3.11+
- `pip` 24+
- Git
- ~500 MB disk alanı

### Adım Adım

```bash
# 1. Repo'yu klonla
git clone https://github.com/muratcan-ates/yzta-datathon-grup-27.git
cd yzta-datathon-grup-27

# 2. Sanal ortam oluştur ve aktive et
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# 3. Bağımlılıkları yükle
pip install --upgrade pip
pip install -r requirements.txt

# 4. Jupyter kernel kaydı (opsiyonel)
python -m ipykernel install --user --name=yzta-datathon --display-name "YZTA Datathon"

# 5. Veri setini ekle
# Kaggle'dan train.csv, test_x.csv, sample_submission.csv indirip
# data/raw/ klasörüne koy
```

### Veri Seti

Veri seti Kaggle competition sayfasından indirilebilir:
- **Competition:** [YZTA 2026 Datathon](https://www.kaggle.com/competitions/yzta-2026-datathon)
- **Erişim:** Sadece YZTA bursiyerlerine açık

Dosyalar **`data/raw/`** klasörüne yerleştirilmelidir. Bu klasör `.gitignore`'da olduğu için repo'ya commit edilmez.

<br/>

---

## 🔁 Reprodüksiyon

Baseline sonucu reproduce etmek için:

```bash
# Jupyter'ı başlat
jupyter notebook

# Notebook'u aç:
# notebooks/02_baseline_lightgbm.ipynb

# Kernel: YZTA Datathon
# Run All Cells (Shift+Enter ile sırasıyla)
```

Notebook ~30 saniyede biter. Çıktı:
- 5 fold'un RMSE değerleri
- OOF RMSE
- `submissions/sub_lgbm_5fold_oof<RMSE>_<TIMESTAMP>.csv` dosyası

Sonuçlar deterministiktir (`seed=42` her yerde).

<br/>

---

## 📁 Proje Yapısı

```
yzta-datathon-grup-27/
├── README.md                          # ← bu dosya
├── LICENSE                            # MIT License
├── requirements.txt                   # Python bağımlılıkları
├── pyproject.toml                     # Proje metadata
├── .gitignore
│
├── data/                              # 📂 Veri seti (gitignored)
│   └── raw/
│       ├── train.csv
│       ├── test_x.csv
│       └── sample_submission.csv
│
├── notebooks/                         # 📓 Jupyter notebook'lar
│   ├── 01_eda_sezin.ipynb             # Keşifsel veri analizi (Sezin)
│   └── 02_baseline_lightgbm.ipynb     # Baseline modeli (5-fold CV)
│
├── src/grup27/                        # 🧠 Çekirdek kod
│   ├── features.py                    # Feature engineering fonksiyonları
│   ├── models.py                      # Model eğitim metotları (planlanan)
│   ├── validation.py                  # Çapraz doğrulama (planlanan)
│   └── ensemble.py                    # Model birleştirme (planlanan)
│
├── tests/                             # 🧪 Unit testler
│   └── test_features.py               # Feature fonksiyonları testleri
│
├── reports/                           # 📊 Deney takip
│   └── experiments.csv                # Submission/model performans tablosu
│
├── submissions/                       # 🏆 Kaggle submission CSV'leri
│   └── sub_lgbm_5fold_oof1.2292_20260513_1424.csv
│
├── models/                            # 📦 Eğitilmiş model artifact'ları
│
└── configs/                           # ⚙️ Konfigürasyon dosyaları
```

<br/>

---

## 📝 Lisans

MIT Lisansı altında yayımlanmıştır. Detaylar için [`LICENSE`](LICENSE) dosyasına bakınız.

<br/>

---

<div align="center">

**YZTA 5. Akademi Dönemi · Veri Bilimi Datathon · Mayıs 2026**

Grup 27: [@muratcan-ates](https://github.com/muratcan-ates) · Sezin Tarlığ · Buse Gülçen · Abdülaziz Kıran · Eray Güler

</div>
