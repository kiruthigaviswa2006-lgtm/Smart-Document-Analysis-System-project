import pandas as pd
import os

def generate_report(results):

    df = pd.DataFrame(results)

    os.makedirs("output", exist_ok=True)

    output_file = "output/classification_results.csv"

    df.to_csv(output_file, index=False)

    print("\nCSV Report Generated Successfully!")
    print("Saved at:", output_file)