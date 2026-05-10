# TEAM_RULES.md — Grup 27 Datathon Sözleşmesi

> Repo'yu clone ettin mi? Bu dosyayı oku. Her commit'ten önce ilgili bölüme bak. Slack'te `#yzta-datathon-grup-27` kanalına pin'lendi.

**Yarışma:** YZTA 2026 Datathon · Son teslim **13 May 2026 23:59 TRT** · Bilişsel performans regresyon, RMSE optimize.

---

## 1. Takım ve Rol Dağılımı

| Rol | Üye | Ana çıktı | Aktif gün |
|---|---|---|---|
| Orchestrator + ensemble | **Murat** | `ensemble.py`, final 2 submission seçimi, takım koordinasyonu | 10-13 May |
| EDA + temel features | **Sezin** | `01_eda.ipynb`, `features.py` (8 fonksiyon) | 10-11 May (bitir) |
| Feature engineering v2 | **Buse** | `02_features.ipynb`, `features.py` (+6 fonksiyon) | 11-12 May |
| Modeling + tuning | **Eray** | `validation.py`, `models.py`, `submit.py`, `03_models.ipynb` | 11-13 May |
| Notebook polish + README | **Abdülaziz** | `FINAL.ipynb`, `README.md`, `experiments.csv` | 11-13 May |

**Bağımlılıklar:** Sezin → Buse → Eray → Abdülaziz. Her aşama bir öncekinin PR merge'ünden sonra başlar.

---

## 2. Branch İsimlendirme

```
feature/<isim>-<topic>     # yeni özellik (her commit bu)
fix/<isim>-<topic>         # bug fix
docs/<isim>-<topic>        # sadece dokümantasyon
exp/<isim>-<topic>         # deneysel — main'e merge edilmeyebilir
```

**Örnek:** `feature/sezin-eda-features`, `feature/eray-validation`, `docs/abdulaziz-readme`.

⚠️ **Main branch'e direkt push YASAK.** Her şey PR ile.

---

## 3. Commit Mesaj Formatı (Conventional Commits)

```
feat: yeni özellik ekle
fix: bug düzelt
docs: dokümantasyon
refactor: kod düzeni (davranış değişmez)
test: test ekle/değiştir
chore: build/deps güncelle
exp: deneysel kod
```

**Örnek:**
- ✅ `feat: add 8 domain feature functions for sleep/cognition`
- ✅ `fix: catboost cat_features parameter typo`
- ✅ `docs: enhance README with reproduction steps`
- ❌ `update`, `wip`, `son`, `çalıştı`

**Dil:** Commit mesajları **İngilizce**. Sohbet ve dokümantasyon Türkçe olabilir.

---

## 4. PR Review Süreci

1. Branch'inde işini bitir, `pytest tests/` yeşil olduğunu gör
2. Push et, GitHub'da Pull Request aç
3. Reviewer olarak **Murat** ekle
4. PR description'a şu 4 başlık:
   - **Ne yaptım** (1-2 cümle)
   - **Neden** (1 cümle)
   - **Test ettim mi** (yes/no + nasıl)
   - **Bağımlılık** (kimi engelledi/engellemiyor)
5. Murat 30 dakika içinde review eder, küçük değişiklik isteyebilir
6. Yeşil ışık + `pytest` geçtikten sonra **squash merge** edilir
7. Merge sonrası kendi branch'ini sil

**13 May saat 09:00 sonrası:** Murat acil `fix:` PR'larını self-merge edebilir, beklemeyin.

---

## 5. Submission Protokolü

**Toplam hak:** 12 (4 gün × 3) · **Final için seçilecek:** 2 · **Hedef anlamlı submission:** 6-8

**Kim ne zaman submit eder:**
- 11 May 18:00 — **Eray** baseline LGBM (Sub #1)
- 12 May 14:00 — **Eray** tuned LGBM (Sub #2)
- 12 May 19:00 — **Eray** tuned CatBoost (Sub #3)
- 12 May 23:00 — **Murat** ilk blend (Sub #4)
- 13 May 15:00 — **Eray** TabPFN OOF (Sub #5, opsiyonel)
- 13 May 20:00 — **Murat** hill-climb ensemble (Sub #6)
- 13 May 23:00 — **Murat** best blend (Sub #7)
- 13 May günü 2 yedek hak

⚠️ **"Ne olur acaba" submission YASAK.** Her submission bir hipotez test edecek. Hak israfı = ilk 10'a girememek.

**Final 2 seçimi (13 May 20:59):**
- Pick 1: **CV-best** (CV RMSE en düşük blend)
- Pick 2: **CV-diverse** (Pick 1'den farklı blend, risk dağıtımı)
- ❌ **Public LB-best seçilmez** çünkü %50 split, shake-up routine

---

## 6. AI Kullanım Kuralları

**Serbest mi:** Evet. Kaggle "profesyonel destek" kuralı insan koçluğa atıfta. Claude/ChatGPT/Cursor/Copilot serbest.

**Ama dikkat:**
- Her AI farklı kod stili üretir → **ortak `requirements.txt`** + **bu MD'deki kurallar** = standart sapması düşer
- AI yanlış sürüm önerebilir (Python 3.10) → biz **Python 3.11** kullanıyoruz, override et
- AI test verisinde `fit_transform` önerebilir → leakage. Pipeline pattern'ine zorla
- Kod yazımının %100'ünü AI'ya bırakma → her satırı anla, sor

**Prompt template:** Her üye kendi MD'sini AI'sına yapıştırıyor (`SEZIN_BRIEF.md`, `BUSE_BRIEF.md`, vs). Yeni chat açtığında tüm context oluşuyor.

**AI çıktısını commit etmeden önce:**
- Kodu okuyup anla
- `pytest` yeşil mi
- Random state 42 mi
- Hard-coded path var mı
- Notebook output'u silinmiş mi (silinmemeli)

---

## 7. Slack İletişim Kuralları

**Kanal:** `#yzta-datathon-grup-27`

**Pin'lenecekler:**
- Bu MD (TEAM_RULES.md)
- Kaggle yarışma linki
- Mevcut leaderboard skoru (günlük güncellenir)
- Kalan submission hakkı sayısı

**Mesaj formatı:**
- ✅ "validation.py PR atıldı, reviewer Murat" (net, eylem dahil)
- ✅ "30 dk LGBM tuning hatasında takıldım, error mesajı thread'de" (yardım çağrısı net)
- ❌ "ne yapayım", "çalışmıyor" (bağlamsız)

**Daily standup:** Her gün **21:00 TRT** Slack'te 5 cümlelik özet:
1. Bugün ne yaptım
2. Yarın ne yapacağım
3. Bekliyor muyum kimseyi
4. Engelleyen var mı

**Submission anonsları:**
- Submit ederken kanala yaz: `Sub #3 — CatBoost tuned, CV 1.18, public LB pending`
- Public LB skoru çıkınca güncelle: `Sub #3 public LB: 1.193`
- Anomali (CV iyi, LB kötü gibi) → hemen thread aç

---

## 8. 30 Dakika Kuralı

**Bir hata, bir takıntı, bir karar 30 dakikadan fazla seni durdurursa Slack'e yaz.**

- Hata: error mesajını + komutu paylaş
- Takıntı: ne yapmaya çalıştığını + denediğini paylaş
- Karar: A vs B seçeneklerini + risk değerlendirmesini paylaş

**Niye:** 5 kişilik takımda 1 kişi 1 saat takılırsa = takım 1 saat geride. 30 dk + 5 kişi soracak = 6 dk × 5 = en kötü 30 dk kayıp. Çok daha az.

---

## 9. Veri Seti Güvenliği

**Kaggle yarışma kuralı:** Datathon linkini başkalarıyla paylaşma. Sadece YZTA bursiyerlerine açık.

- ❌ Sosyal medyada paylaşma
- ❌ Stackoverflow'a kod yapıştırırken veri set adını yazma
- ❌ AI'ya veri içeriğini yapıştırma (kolon isimleri OK, satırlar değil)
- ❌ Public Kaggle notebook olarak yayınlama

**Repo public mi?** Evet, kod açık (yarışma kuralı + akademi şartı). **Veri repo'da YOK** — gitignored, herkes kendi Kaggle hesabından indirir.

---

## 10. Reprodüksiyon Disiplini

**Her PR'da bunlar kontrol edilecek:**

- [ ] `random_state=42` her yerde
- [ ] Hard-coded path yok (`pathlib.Path` kullanılmış)
- [ ] `pyproject.toml` + `requirements.txt` güncel
- [ ] `pytest tests/` yeşil
- [ ] Notebook `Restart and Run All` ile çalışıyor
- [ ] Notebook output'u commit'te dolu (silinmemiş)
- [ ] Türkçe karakterli yeni feature ismi yok (snake_case İngilizce)

---

## 11. Acil Durum Senaryoları

**13 May saat 17:00, FINAL.ipynb çalışmıyor:**
- Abdülaziz Slack'te alarm verir
- Murat + Eray bağlanır, 30 dk debug
- Çözülmezse: önceki çalışan submission (Sub #6 veya #7) final pick yapılır

**13 May saat 22:00, Kaggle erişim sorunu:**
- Mobil hotspot'a geç
- VPN dene
- 23:30'da hâlâ giriş yoksa Slack'ten YZTA akademi destek hattına yaz

**Takım üyesi ulaşılamaz:**
- 2 saat boyunca yanıt yoksa Murat görevini devralır veya pause eder
- Onun parçası olmadan ilerlenebiliyorsa devam, ilerleyemiyorsa dur ve bekle

---

## 12. Kazanma Felsefesi

**Hız değil disiplin.** **Public LB değil CV.** **En karmaşık model değil en istikrarlı pipeline.**

Datathon değerlendirme kriterleri:
1. Feature Engineering — Sezin + Buse
2. EDA — Sezin
3. Kütüphane & Algoritma seçimi — Eray
4. Model Performans (RMSE) — Eray + Murat
5. Temiz Kod & Düzenli Notebook — Abdülaziz

**Hedef ilk 10.** Top 3 olursa 50.000 TL ödül. Olmazsa Bootcamp tecrübesi + GitHub portföy.

---

**Son güncelleme:** 10 May 2026
**Sahibi:** Abdülaziz (zenginleştirme), Murat (onay)