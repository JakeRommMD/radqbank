
### Data files expected by the app

1. `config.yaml` at repo root  
2. `data/questions_master.csv` – main question bank  
3. `media/` – images referenced in the CSV  

See **DATA_SCHEMA.md** for full column-by-column specs and examples.

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