from scripts.extract_youtube import extract_data
from scripts.transform_youtube import transform_data
from scripts.load_to_s3 import upload_to_s3

if __name__ == "__main__":
    # Extract
    input_file = "data/USvideos.csv"
    raw_data = extract_data(input_file)

    # Transform
    output_file = "data/transformed_youtube.csv"
    transform_data(raw_data, output_file)

    # Load
    upload_to_s3(
        file_name=output_file,
        bucket="youtube-etl-oladapo",
        object_name="youtube/transformed_youtube.csv"
    )

    print("✅ ETL pipeline complete.")