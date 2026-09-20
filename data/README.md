# Data / البيانات

The raw data files are **not** stored in this repository (`cab_rides.csv` is ~89 MB).
ملفات البيانات الخام غير مرفوعة هنا (حجم `cab_rides.csv` حوالي 89 ميجابايت).

## Source / المصدر

Uber & Lyft Dataset (Boston, MA) on Kaggle:
**[add the official Kaggle link + dataset author here / أضيفوا رابط Kaggle واسم صاحب الداتاسيت]**

Files needed / الملفات المطلوبة:

| File | Description |
|---|---|
| `cab_rides.csv` | ~693k rides (price, surge multiplier, source, destination, ...) |
| `weather.csv` | weather readings per Boston location |

Download them and place them in this `data/` folder, then run:
حمّلوهما وضعوهما في هذا المجلد ثم شغّلوا:

```bash
python src/feature_engineering.py
```

Output / الناتج: `data/Makkah_Ramadan_Rides_Clean.csv` (~638k rows, simulated Makkah/Ramadan features).

> ⚠️ The Ramadan/prayer/weather columns are simulated. / أعمدة رمضان والصلاة والطقس مُحاكاة.
