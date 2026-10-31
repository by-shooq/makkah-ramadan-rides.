# Data / البيانات

The raw CSV files are not stored in this repository. Download the required files from the source dataset and place them in this `data/` folder.

ملفات CSV الخام غير مرفوعة في هذا المستودع. حمّل الملفات المطلوبة من مصدر البيانات وضعها داخل مجلد `data/`.

## Source / المصدر

Uber & Lyft Dataset (Boston, MA) on Kaggle:

https://www.kaggle.com/datasets/ravi72munde/uber-lyft-cab-prices

## Required files / الملفات المطلوبة

| File | Description |
|---|---|
| `cab_rides.csv` | Ride records, including price, surge multiplier, source, and destination |
| `weather.csv` | Weather readings associated with Boston locations |

## Run / التشغيل

After placing both files in this folder, return to the repository root and run:

بعد وضع الملفين في هذا المجلد، ارجع إلى المجلد الرئيسي للمستودع وشغّل:

```bash
python feature_engineering.py
```

The script generates a cleaned, simulated Makkah/Ramadan dataset under `data/`.

ينتج السكربت ملف بيانات مُنظفاً ومُحاكًى لسياق مكة ورمضان داخل مجلد `data/`.

> ⚠️ Ramadan, prayer-period, and localized Makkah context features are simulated. They are not real operational observations.
>
> ⚠️ ميزات رمضان وفترات الصلاة وتوطين المواقع على مكة مُحاكاة، وليست بيانات تشغيلية حقيقية.
