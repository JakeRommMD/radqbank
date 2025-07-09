1 Project layout (required files & folders)
bash
Copy
Edit
radqbank/
├─ src/radqbank/
│  └─ …                     # Python code
├─ data/
│  └─ questions_master.csv  # ← main question bank
├─ media/                   # ← images referenced in the CSV
│     └─ <image files>
├─ config.yaml              # ← global settings (see § 2)
└─ README.md
Tip: keep data/ and media/ out of version-control if the bank ever gets large; instead track them with Git-LFS or pull them from cloud storage in CI.

2 config.yaml fields
Key	Type	Purpose / example
app_title	str	Displayed in tab + sidebar.
"RadQBank"
csv_path	str	Relative or absolute path to the main questions CSV.
"data/questions_master.csv"
media_dir	str	Folder where image_filename values live.
"media"
points.correct	int	XP awarded per correct answer.
points.streak_bonus	int	Extra XP per Q when current streak ≥ 3.
level_thresholds	list[int]	Cumulative XP cut-offs for levels, e.g. [0, 250, 600, 1000, 1500].

yaml
Copy
Edit
# example config.yaml
app_title: "RadQBank"
csv_path: "data/questions_master.csv"
media_dir: "media"
points:
  correct: 10
  streak_bonus: 5
level_thresholds: [0, 250, 600, 1000, 1500]

3 questions_master.csv schema
Column (header)	Type	Required	Description
question_id	str / int	✔	Unique key (used in user progress).
stem_md	Markdown	✔	Full question stem. Supports inline images & LaTeX ($…$).
options_json	JSON array	✔	e.g. ["Option A", "Option B", "Option C", "Option D"]. Order is preserved.
correct_answer	str	✔	Must match one element in options_json exactly.
explanation_md	Markdown	✔	Shown after submission. May include links, bold, etc.
primary_topic	str	✔	e.g. "Chest CT", "Nuclear Cardiology". Drives sidebar filters.
secondary_topic	str	–	Optional finer grouping.
difficulty	str / int	–	Your scale: "easy" / "moderate" / "hard" or 1-5.
tags	CSV string	–	Extra keywords, e.g. "PET, oncology, SUV".
image_filename	str	–	File located under media/; leave blank if not used.

Minimal example row
csv
Copy
Edit
question_id,stem_md,options_json,correct_answer,explanation_md,primary_topic,image_filename
Q001,"A 65-year-old man with dyspnea undergoes a V/Q scan. The perfusion images show…",\
    ["Pulmonary embolism","COPD","Pulmonary hypertension","Normal study"],\
    "Pulmonary embolism",\
    "**PE** causes segmental perfusion defects with preserved ventilation.",\
    "Nuclear Medicine","vq_pe_example.png"
(Note the back-slash line continuations above are just for readability; real CSV has one physical line.)

4 Image requirements
Put files in media/ (or a subfolder).

Reference them by filename only (no path) in image_filename.

Supported formats: .png, .jpg, .jpeg, .gif; Streamlit picks the correct loader.

5 Optional future tables (for Supabase phase)
Table	Purpose	Minimal columns
users	Auth + XP	id, email, hashed_password, xp, level
responses	Per-user answer log	user_id, question_id, is_correct, timestamp

(Not needed for the offline MVP—local Session State handles progress until you wire Supabase.)

6 Validation checklist before import
CSV parses: python -c "import pandas as pd, sys; pd.read_csv(sys.argv[1])";
should exit silently.

Every correct_answer is present in its options_json list (case-sensitive).

No duplicate question_id.

Any image_filename value exists under media/.

Markdown renders correctly in a quick preview (VS Code “Markdown Preview” or GitHub viewer).