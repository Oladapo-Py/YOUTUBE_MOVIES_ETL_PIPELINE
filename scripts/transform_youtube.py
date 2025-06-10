def transform_data(df, output_file):
    # Example transformation: remove rows with missing values
    df_cleaned = df.dropna()

    # Save the transformed data
    df_cleaned.to_csv(output_file, index=False)
    print(f"🔄 Transformed data saved to {output_file}")
