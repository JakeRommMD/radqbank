# Radiology Q‑Bank Streamlit App – Functional Spec

---

## 1 · Vision & Core Objectives

- **Audience:** Radiology residents, fellows, and anyone reviewing radiology topics.
- **Purpose:** Deliver a high‑yield question bank (Q‑bank) that tracks performance and layers in motivating gamification (XP, levels, badges à la Boot.dev) to create a “dopamine‑rich” study experience.
- **Guiding Principles**
  1. *Fast iteration* – build a minimal core first, then add layers.
  2. *Data‑driven* – every answer feeds analytics & progress stats.
  3. *Extensible* – CSV import today, optional DB / API tomorrow.

## 2 · High‑Level Architecture

| Layer            | Choice (MVP)                             | Notes                                                                      |
| ---------------- | ---------------------------------------- | -------------------------------------------------------------------------- |
| **Frontend**     | Streamlit (st‑pages or multipage native) | Rapid dev, easy deploy (Streamlit Cloud, HuggingFace Space, or container). |
| **Auth**         | Supabase Auth (free tier)                | Email/OAuth (Google, GitHub) with JWT stored in `st.session_state`.        |
| **Data store**   | CSV → DuckDB/SQLite on boot              | Keeps authoring simple while enabling SQL‑speed filters.                   |
| **Media**        | `/media/<filename>` referenced in CSV    | Display via `st.image` or `st.markdown(<img>)`.                            |
| **Gamification** | Local JSON/SQLite tables                 | XP, levels, badges, streaks.                                               |
| **Config**       | `config.yaml` (optional) or `st.secrets` | Parameters editable without code.                                          |

## 3 · Question Data Model

```text
question_id        str  • stable UUID or incremental
stem_md            str  • markdown; supports inline ‹img› tags
question_type      enum • MCQ / MultiSelect / TrueFalse / ImageMCQ
options_json       str  • JSON array of answer choices (for MCQ)
correct_answer     str  • "A" / ["A","C"] depending on type
explanation_md     str  • markdown w/ links & images
image_filename     str? • optional – file found in /media
primary_topic      str  • e.g. "MSK", "Chest", "Physics"
secondary_topics   str  • pipe‑delimited list
difficulty         int  • 1‑5
points             int  • default = 10
```

## 4 · User/Progress Schema (SQLite)

```text
users(id, email, display_name, pwd_hash, xp, level, created_at)
responses(id, user_id, question_id, selected_json, is_correct, ts)
user_badges(user_id, badge_code, awarded_ts)
```

### XP & Leveling Formula

```
XP per correct              = 10
Streak bonus (n ≥ 3)        = 5 × (n‑2)
Level thresholds (XP total) = [0, 250, 600, 1000, …]
Ranks                       = Regretful R1, Contrast Cruisader, Numb R2, Bad to the CORE R3, Powerscribe Burnt R4, Aloof Fellow
```

### Badge Catalogue (initial)

| Code           | Name          | Criteria                               |
| -------------- | ------------- | -------------------------------------- |
| FIRST\_CORRECT | First Blood   | First correct answer                   |
| TEN\_STREAK    | Hot Streak 10 | 10 correct in a row                    |
| TOPIC\_MASTER  | Topic Master  | ≥ 80 % correct on ≥ 50 Qs in one topic |
| COMPLETIONIST  | 100 % Club    | Answered every question                |

## 5 · Core Screens / Routes

1. **Login / Register** – simple auth; fallback “guest mode” w/out persistence.
2. **Dashboard**
   - XP bar, current level & rank
   - Badge grid (earned vs locked)
   - Topic‑wise heat‑map (%)
3. **Question Session**
   - Sidebar filters: topic(s), difficulty, unused/incorrect.
   - Question card → submit → immediate feedback + explanation.
   - “Next” obeys filter + shuffle toggle.
4. **Review / Analytics**
   - Table of answered questions with filters (incorrect, last 7 days, etc.).
   - Ability to re‑queue incorrect items.
5. **Admin** (hidden behind role flag)
   - Upload/replace CSV, preview parsed rows, run integrity checker (image exists, correct answers valid, etc.).

## 6 · Config Parameters (sample `config.yaml`)

```yaml
app_title: "RadQBank"
csv_path: "data/questions_master.csv"
media_dir: "media"
points:
  correct: 10
  streak_bonus: 5
level_thresholds: [0, 250, 600, 1000, 1500, 2100]
badges:
  FIRST_CORRECT:
    name: "First Blood"
    criterion: "first_correct"
  TEN_STREAK:
    name: "Hot Streak 10"
    criterion: "streak >= 10"
```

## 7 · Milestone Roadmap

| Phase | Goal                            | Key Deliverables                                   |
| ----- | ------------------------------- | -------------------------------------------------- |
| **1** | Core Q‑bank                     | CSV ingest → QuestionSession → basic progress %    |
| **2** | Persistent Progress             | SQLite user & response tables; dashboard charts    |
| **3** | Gamification Layer              | XP engine, level calculation, badge service        |
| **4** | Polish & Deploy                 | Responsive layout, dark mode, containerized deploy |
| **5** | Social & Leaderboards (stretch) | Global leaderboard, shareable badges               |

## 8 · Key Non‑Functional Reqs

- **Performance:** ≤ 200 ms to pull & render next question (cache in memory).
- **Accessibility:** keyboard nav, alt‑text for images.
- **Security:** Hash passwords (`argon2`), parameterize file uploads to prevent traversal.
- **Testing:** pytest + Streamlit Testing Framework; lint via Ruff.

## 9 · Open Questions


---

*End of Spec*

