import pickle

file_name = "pipeline.bin"

with open(file_name, "rb") as model:
    pipeline = pickle.load(model)

record = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}

print(round(pipeline.predict_proba(record)[0, 1], 3))