import pandas as pd

def extract_data(input_file):
    df = pd.read_csv(input_file)
    print(f"✅ Extracted {len(df)} rows from {input_file}")
    return df

# Optional test run
if __name__ == "__main__":
    df = extract_data("data/USvideos.csv")
    df.to_csv("data/cleaned_youtube.csv", index=False)
    print("💾 Saved cleaned data to data/cleaned_youtube.csv")
