# 📌 Project Title
**YouTube Analytics: EdTech Student Engagement & Performance (Physics Wallah Channel)**

---

## 🔍 Objective
Analyze Physics Wallah’s YouTube channel to measure **student engagement** and **video performance** over time using:
- YouTube Data API (for data extraction)
- Excel (for cleaning & lookup tables)
- Power BI (for ETL, modeling, and dashboard creation)
- **Time Series Analysis** for seasonal trends & long-term patterns

---

## 📊 Workflow

1. **API Extraction**
   - Collected video metadata: *title, duration, views, likes, publish date, subject, exam type, class*.

2. **Excel Cleaning**
   - Removed duplicates, handled missing values.
   - Created lookup tables for exam type & subjects.

3. **Power Query (Power BI Cleaning)**
   - Converted video duration into minutes.
   - Created calculated columns (Engagement Rate = Likes / Views).
   - Merged lookup tables for class & exam mapping.

4. **KPIs & Measures**
   - **Total Views**
   - **Average Views per Video**
   - **Average Likes per Video**
   - **Engagement Rate (likes/views)**

5. **Visualizations**
   - KPI Cards (Total Views, Avg Views, Avg Likes)
   - Views by Duration (<200 min, >200 min)
   - Subject & Exam-wise Performance
   - Views by Class (11th vs 12th)
   - Engagement by Content Type
   - **Time Series Trends**: Yearly (2017–2025) & Seasonal (Monthly)

---

## 📸 Dashboard Preview
![Edtech Dashboard](./Edtech%20analysis.png)

---

## ⚙️ Tools & Tech
- **Python** → YouTube Data API, Pandas for preprocessing  
- **Excel** → Lookup tables, initial cleanup  
- **Power BI** → ETL, transformations, time series, dashboard creation  

---

## 🚀 Insights

### 🔹 Overall Channel Performance
- **Total Views**: 2B+  
- **Average Views per Video**: 2M  
- **Average Likes per Video**: 50K  

### 🔹 Time Series Analysis
- **Peak year**: 2018 (2.9M avg views) → Decline after 2019  
- **Seasonal trend**: Sharp **spike in May–July** (5.5M in May), aligning with exam season  
- Views stabilized at ~1.2M average in 2024–2025  

### 🔹 Student Segmentation
- **By Class**: 11th (54%) > 12th (46%)  
- **By Exam Type**: NEET (40.1%) dominates, followed by JEE (30.7%) and JEE/NEET combined (29.2%)  

### 🔹 Content Performance
- **Shorter videos (<200 min)** drive maximum views  
- **Content types** like *Paper Decoders* and *1 Shot* attract more views & likes compared to Timetable videos  

### 🔹 Subject Engagement
- **Highest engagement** in **Organic Chemistry** and **Physics**  
- **Biology** shows strong performance (especially for NEET audience)  
- **Math** lags behind in engagement  

### 🔹 Exam & Class Cross Analysis
- **NEET (11th class)** → Highest views (~2M)  
- **JEE/NEET (12th class)** → Higher engagement rate even with lower views  

---

✅ This analysis highlights how **Physics Wallah’s channel engagement aligns with exam timelines** and shows **Physics & Chemistry dominance** in both views and likes.

