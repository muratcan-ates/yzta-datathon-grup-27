<div align="center">

# 🧠 YZTA 2026 Datathon — Grup 27

### Bilişsel Performans Skoru Tahmini

**YZTA 5. Akademi Dönemi · Veri Bilimi Datathon · Mayıs 2026**

<br/>

<p align="center">
  <a href="#-proje-özeti"><strong>Proje Özeti</strong></a> ·
  <a href="#-yarışma-kriterleri"><strong>Yarışma</strong></a> ·
  <a href="#-sonuçlar"><strong>Sonuçlar</strong></a> ·
  <a href="#-pipeline-mimarisi"><strong>Mimari</strong></a> ·
  <a href="#-kurulum"><strong>Kurulum</strong></a>
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
![License](https://img.shields.io/github/license/muratcan-ates/yzta-datathon-grup-27?style=flat-square)

</div>

<br/>

---

## 📖 İçindekiler

- [🎯 Proje Özeti](#-proje-özeti)
- [📋 Yarışma Kriterleri](#-yarışma-kriterleri)
- [👥 Takım](#-takım)
- [🛠️ Kullanılan Teknolojiler](#️-kullanılan-teknolojiler)
- [📊 Sonuçlar](#-sonuçlar)
- [🔬 Veri ve Ön İşleme](#-veri-ve-ön-işleme)
- [🏗️ Pipeline Mimarisi](#️-pipeline-mimarisi)
- [⚠️ Kapsam ve Sınırlamalar](#️-kapsam-ve-sınırlamalar)
- [🚀 Kurulum](#-kurulum)
- [🔁 Reprodüksiyon](#-reprodüksiyon)
- [📁 Proje Yapısı](#-proje-yapısı)
- [🔧 Geliştirme](#-geliştirme)
- [📝 Lisans](#-lisans)

<br/>

---

## 🎯 Proje Özeti

Bu depo, **YZTA 5. Akademi Dönemi Datathon yarışması** kapsamında Grup 27 tarafından geliştirilen makine öğrenmesi çözümünü içermektedir. Sistem, bireylerin uyku, yaşam tarzı ve demografik özelliklerinden yola çıkarak **bilişsel performans skorlarını** tahmin eden uçtan uca bir regresyon pipeline'ıdır.

**Neden önemli?** Bilişsel performans, kişinin günlük yaşam kalitesini, iş verimliliğini ve uzun vadeli sağlığını doğrudan etkileyen bir gösterge. Uyku düzeni, kafein tüketimi, ekran süresi gibi değiştirilebilir alışkanlıkların bilişsel skorla ilişkisini modelleyebilmek, hem bireysel sağlık takibi hem de toplumsal sağlık politikaları için somut bir bilgi tabanı oluşturuyor. Bu projede sadece bir tahmin skoru değil, **şeffaf ve tekrarlanabilir bir ML pipeline'ı** üretilmiştir — başka takım üyeleri kodu klonlayıp aynı sonucu deterministik biçimde üretebilir.

**Tek cümleyle:** Train + test CSV'lerini al → 5-fold LightGBM CV → out-of-fold tahmin + Kaggle submission CSV.

<br/>

---

## 📋 Yarışma Kriterleri

YZTA 5. Akademi Dönemi Datathon Bursiyer Kılavuzu'nda belirtilen tüm değerlendirme kriterleri bu projede ele alınmıştır.

### Datathon Değerlendirme Kriterleri

| # | Kriter | Durum | Karşılandığı Yer |
|---|--------|:-:|------------------|
| 1 | Feature Engineering | 🟡 | `src/grup27/features.py` (Sezin + Buse), baseline'a entegrasyon planlandı |
| 2 | Exploratory Data Analysis (EDA) | ✅ | `notebooks/01_eda_sezin.ipynb` |
| 3 | Kütüphane & Algoritma Seçimleri | ✅ | LightGBM seçim gerekçesi → `README` |
| 4 | Model Performans Metrikleri (RMSE) | ✅ | OOF RMSE 1.22924, Public 1.21440 |
| 5 | Temiz Kod & Düzenli Notebook | ✅ | `notebooks/02_baseline_lightgbm.ipynb` modüler hücreler |

### Teslim Beklentisi

| Beklenti | Durum |
|----------|:-:|
| Kaggle submission (13 Mayıs 23:59) | ✅ |
| Notebook (Code kısmı veya GitHub) | ✅ [`02_baseline_lightgbm.ipynb`](notebooks/02_baseline_lightgbm.ipynb) |
| Public GitHub repository | ✅ [muratcan-ates/yzta-datathon-grup-27](https://github.com/muratcan-ates/yzta-datathon-grup-27) |
| Reprodüksiyon talimatları | ✅ Bu README → [Reprodüksiyon](#-reprodüksiyon) |

<br/>

---

## 👥 Takım

<table align="center">
<tr>
<td align="center">
  <a href="https://github.com/muratcan-ates">
    <img src="https://github.com/muratcan-ates.png" width="100" alt="Muratcan Ates"/>
    <br/>
    <sub><b>Muratcan Ateş</b></sub>
  </a>
  <br/>
  <sub>Orchestrator</sub>
  <br/>
  <sub>ML Pipeline · Submission</sub>
</td>
<td align="center">
  <a href="https://github.com/sezintarlig">
    <img src="https://github.com/sezintarlig.png" width="100" alt="Sezin Tarlıg"/>
    <br/>
    <sub><b>Sezin Tarlığ</b></sub>
  </a>
  <br/>
  <sub>Data Analyst</sub>
  <br/>
  <sub>EDA · Feature Functions</sub>
</td>
<td align="center">
  <a href="https://github.com/busegulcenn">
    <img src="https://github.com/busegulcenn.png" width="100" alt="Buse Gulcen"/>
    <br/>
    <sub><b>Buse Gülçen</b></sub>
  </a>
  <br/>
  <sub>Feature Engineer</sub>
  <br/>
  <sub>v2 Features · Tests</sub>
</td>
<td align="center">
  <a href="https://github.com/Abdulaziz-kiran">
    <img src="https://github.com/Abdulaziz-kiran.png" width="100" alt="Abdulaziz Kiran"/>
    <br/>
    <sub><b>Abdülaziz Kıran</b></sub>
  </a>
  <br/>
  <sub>Documentation</sub>
  <br/>
  <sub>README · Repo Structure</sub>
</td>
<td align="center">
  <a href="https://github.com/erayglr">
    <img src="https://github.com/erayglr.png" width="100" alt="Eray Guler"/>
    <br/>
    <sub><b>Eray Güler</b></sub>
  </a>
  <br/>
  <sub>Support Engineer</sub>
  <br/>
  <sub>—</sub>
</td>
</tr>
</table>

<br/>

---

## 🛠️ Kullanılan Teknolojiler

| Katman | Teknoloji | Sürüm | Neden? |
|--------|-----------|:-----:|--------|
| **Dil** | Python | 3.11 | Veri bilimi ekosisteminin standart dili |
| **Veri** | pandas, numpy | 2.3, 2.0+ | Veri okuma ve nümerik işlemler için endüstri standardı |
| **ML** | LightGBM | 4.6 | Gradient boosting, native categorical handling, CPU üzerinde 5-fold ~17 saniye |
| **Validation** | scikit-learn KFold | 1.7 | 5-fold CV ile robust OOF tahmin |
| **Notebook** | Jupyter | 1.1 | EDA ve baseline geliştirme |
| **Versiyon Kontrol** | Git + GitHub | — | Çoklu branch + PR workflow ile takım koordinasyonu |

Tüm bağımlılıklar `requirements.txt` içinde sürümlenmiştir. Eğitim/test tek bir conda+venv ortamında reprodüksiyona uygun şekilde çalışır.

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

**Yorum:** Fold-bazlı RMSE değerleri **çok düşük variance** gösteriyor (standart sapma ±0.01). Bu, modelin farklı veri dilimlerinde tutarlı çalıştığına ve overfitting olmadığına işaret ediyor. Kaggle public score (1.21440), OOF skorundan (1.22924) biraz daha iyi geldi — beklendiği gibi, train ve test setlerinin dağılımları büyük ölçüde örtüşüyor. Bu durum, train üzerinde 5-fold CV ile alınan RMSE'nin gerçek test performansı için **güvenilir bir tahminci** olduğunu doğruluyor.

### Submission Geçmişi

| Tarih | Model | OOF RMSE | Public Score |
|-------|-------|:--------:|:------------:|
| 13 Mayıs 2026 | LightGBM 5-fold baseline | 1.22924 | **1.21440** |

> 📝 *Bu README, geliştirme süreci boyunca güncellenecektir. Yeni submission'lar ve iyileştirmeler eklendiğinde tablo genişletilecektir.*

<br/>

---

## 🔬 Veri ve Ön İşleme

**Veri seti:** YZTA 2026 Datathon Kaggle competition (`yzta-2026-datathon`) — Bursiyerlere özel sentetik veri seti, bireylerin uyku düzeni, yaşam alışkanlıkları ve demografik bilgilerinden bilişsel performans skoru türetilmiş.

### Veri İstatistikleri

| Özellik | Değer |
|---------|-------|
| Train satır sayısı | 56,000 |
| Test satır sayısı | 24,000 |
| Toplam öznitelik (feature) | 22 |
| Numerik öznitelikler | 15 |
| Kategorik öznitelikler | 7 |
| Hedef değişken | `bilissel_performans_skoru` (float, 0-10 aralığı) |
| Eksik değer (train) | 9,372 |
| Eksik değer (test) | 4,068 |

### Hedef Dağılımı

- **Ortalama:** 5.913
- **Standart sapma:** 2.232
- **Min / Max:** 0.0 / 10.0
- **Çeyrekler:** 25% = 4.40, 50% = 6.03, 75% = 7.57

Dağılım normal-benzeri, hafif sola çarpık. Hedef değişken sürekli ve sınırlı bir aralıkta olduğu için `np.clip(0, 10)` ile tahminlerin sınırlandırılması beklenen davranıştır.

### Kategorik Değişkenler

Toplam 7 adet kategorik değişken bulunmaktadır:
- `cinsiyet`, `meslek`, `ulke`, `kronotip`, `ruh_sagligi_durumu`, `mevsim`, `gun_tipi`

Bu değişkenler **LightGBM'in native categorical handling** özelliğiyle işlendi. One-hot encoding yerine doğrudan `category` dtype kullanıldı; bu yaklaşım hem RMSE açısından (~%3 daha iyi) hem de hesaplama maliyeti açısından (daha az bellek) avantaj sağlıyor.

### Ön İşleme Adımları

1. **Train + test load** → `pandas.read_csv` ile yükleme
2. **Categorical encoding** → `object` dtype → `category` dtype dönüşümü
3. **Missing value handling** → LightGBM native NaN handling (manuel imputation yok)
4. **Train/test categorical alignment** → Test'te train'de olmayan kategori yoktu (kontrol edildi)
5. **Feature/target split** → `id` ve hedef hariç tüm sütunlar feature olarak kullanıldı

<br/>

---

## 🏗️ Pipeline Mimarisi

### Akış Diyagramı

```
data/raw/
  ├── train.csv (56000 satır)
  ├── test_x.csv (24000 satır)
  └── sample_submission.csv

         │
         ▼
┌─────────────────────────────────────────┐
│  notebooks/02_baseline_lightgbm.ipynb   │
│                                         │
│  1. Data load                           │
│  2. Categorical → category dtype        │
│  3. 5-fold KFold split (seed=42)        │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ Fold 1-5 (her fold için):       │    │
│  │  ├ LightGBM train               │    │
│  │  ├ Early stopping (100 rounds)  │    │
│  │  ├ OOF prediction (validation)  │    │
│  │  └ Test prediction (averaged)   │    │
│  └─────────────────────────────────┘    │
│                                         │
│  4. OOF RMSE hesapla                    │
│  5. Test predictions → clip(0, 10)      │
│  6. Submission CSV oluştur              │
└──────────────────┬──────────────────────┘
                   │
                   ▼
            submissions/
               └── sub_lgbm_5fold_oof1.2292_*.csv
                   → Kaggle upload
```

### Bileşenler

**Veri Yükleme:**
- Train ve test CSV'leri `data/raw/` altından okunur
- `data/` klasörü `.gitignore`'da olduğu için repo'ya commit edilmez

**Categorical Handling:**
- 7 kategorik sütun `category` dtype'a çevrilir
- LightGBM `categorical_feature` parametresiyle native handling

**Cross-Validation:**
- 5-fold KFold, shuffled (random_state=42)
- Her fold için ayrı LightGBM modeli eğitilir
- Test tahminleri 5 modelin ortalamasıdır (`/N_SPLITS`)

**Early Stopping:**
- Validation RMSE 100 round boyunca iyileşmezse durdurulur
- Ortalama best_iter ~190 (max 2000 round içinde)

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

Bu değerler **baseline default'tur** — Optuna ile hyperparameter tuning bir sonraki iterasyona planlanmıştır. Mevcut konfigürasyon, hızlı eğitim (17.2s) ile düşük variance (±0.01) arasında dengeli bir trade-off sunuyor.

<br/>

---

## ⚠️ Kapsam ve Sınırlamalar

Şeffaflık önemli bir akademik prensiptir. Bu çözümün mevcut durumdaki sınırlamaları aşağıda açıkça belirtilmiştir.

### Model Sınırlamaları

- **Tek model:** Sadece LightGBM kullanıldı. CatBoost, XGBoost gibi alternatif modeller veya bunların blend'i denenmedi.
- **Default hyperparameters:** Optuna gibi otomatik hyperparameter tuning yapılmadı. Manuel olarak seçilen değerler kullanıldı.
- **Feature engineering minimal:** Sezin ve Buse'nin geliştirdiği özel feature fonksiyonları (`src/grup27/features.py`) henüz baseline'a entegre edilmedi — bu, sonraki iterasyona planlanmıştır.

### Veri Sınırlamaları

- **Train/test dağılım analizi sınırlı:** Test setinin train'e ne kadar benzediği derinlemesine incelenmedi (KS test, distribution drift analizi yapılmadı).
- **Outlier handling yok:** Aykırı değerler tespit edilip işlenmedi.
- **Cross-validation strategy basit:** 5-fold KFold (shuffled) kullanıldı. Stratified KFold (target binning ile) veya Repeated KFold daha robust olabilir.

### Sıralama Sınırlaması

Kaggle leaderboard'da yarışma kazananları **0.13-0.20 RMSE bandında** yer alıyor. Bizim mevcut skorumuz (**1.21440**) bu seviyenin çok altında. Bu fark, üst sıralardaki takımların muhtemelen **agresif feature engineering**, **multi-model ensemble** ve **kapsamlı hyperparameter tuning** uyguladığını gösteriyor. Mevcut baseline'ımız sağlam bir temel olarak korunmakla birlikte, bu boşluğu kapatmak için yukarıdaki sınırlamaların ele alınması gerekiyor.

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
```

### Veri Seti

Veri seti Kaggle competition sayfasından indirilebilir:
- **Competition:** [YZTA 2026 Datathon](https://www.kaggle.com/competitions/yzta-2026-datathon)
- **Erişim:** Sadece YZTA bursiyerlerine açık

İndirdiğiniz dosyalar **`data/raw/`** klasörüne yerleştirilmelidir:

```
data/raw/
  ├── train.csv
  ├── test_x.csv
  └── sample_submission.csv
```

Bu klasör `.gitignore`'da olduğu için repo'ya commit edilmez.

<br/>

---

## 🔁 Reprodüksiyon

Baseline sonucu **deterministik biçimde** reproduce etmek için:

```bash
# Jupyter'ı başlat
jupyter notebook

# Notebook'u aç:
# notebooks/02_baseline_lightgbm.ipynb

# Kernel: YZTA Datathon
# Run All Cells (sırasıyla Shift+Enter)
```

Notebook yaklaşık **30 saniyede** biter ve şu çıktıları üretir:

- 5 fold'un fold-bazlı RMSE değerleri
- OOF RMSE (1.22924)
- `submissions/sub_lgbm_5fold_oof<RMSE>_<TIMESTAMP>.csv` dosyası

**Determinizm garantisi:** `seed=42` her yerde tutarlı kullanıldığı için, aynı veri seti ve aynı kod ile her zaman aynı OOF RMSE elde edilir.

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

## 🔧 Geliştirme

### Branch Stratejisi

- `main` — production, sadece tamamlanmış ve test edilmiş kod
- Feature branch'leri — yeni özellik/düzeltme çalışmaları için

PR workflow:

```bash
git checkout -b feature/yeni-ozellik
# geliştirme...
git commit -m "feat: kısa açıklama"
git push origin feature/yeni-ozellik
# GitHub'da PR aç → main
```

### Commit Konvansiyonu

[Conventional Commits](https://www.conventionalcommits.org/) formatı kullanılmıştır:

- `feat:` — yeni özellik
- `fix:` — bug fix
- `refactor:` — davranış değişmeden yapı iyileştirmesi
- `docs:` — dokümantasyon
- `chore:` — yardımcı değişiklikler (dependency update, config)
- `test:` — test ekleme/düzeltme

<br/>

---

## 📝 Lisans

MIT Lisansı altında yayımlanmıştır. Detaylar için [`LICENSE`](LICENSE) dosyasına bakınız.

<br/>

---

<div align="center">

**YZTA 5. Akademi Dönemi · Veri Bilimi Datathon · Mayıs 2026**

Geliştirenler: Muratcan Ates · Sezin Tarlığ · Buse Gülçen · Abdülaziz Kıran · Eray Güler

</div>
