# main.py
from demographic_data_analyzer import demographic_data_analyzer

results = demographic_data_analyzer()
for key, value in results.items():
    print(f"{key} \n{value}\n")

