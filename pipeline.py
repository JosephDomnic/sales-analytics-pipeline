import subprocess

steps = [
    ("Step 1: Cleaning data...", ["python", "src/clean_data.py"]),
    ("Step 2: Loading to database...", ["python", "src/load_to_db.py"]),
    ("Step 3: Running queries...", ["python", "src/queries.py"]),
]

for label, cmd in steps:
    print(f"▶ {label}")
    subprocess.run(cmd, check=True)

print("\n✅ Pipeline complete! All steps ran successfully.")