import pandas as pd
from behave import given, when, then

@given('input files are available')
def step_check_input_files(context):
    # Load input files into dataframes
    context.instrument_df = pd.read_csv("input_files/InstrumentDetails.csv")
    context.position_df = pd.read_csv("input_files/PositionDetails.csv")

@when("the application generates the output file")
def generate_output_file(context):
    # Merge input files based on InstrumentID and ID
    merged_df = context.position_df.merge(
        context.instrument_df, left_on="InstrumentID", right_on="ID"
    )
    # Rename columns and calculate Total Price
    merged_df["ID"] = range(1, len(merged_df) + 1)
    merged_df["PositionID"] = merged_df["ID_y"]
    merged_df["Total Price"] = merged_df["Quantity"] * merged_df["Unit Price"]
    output_df = merged_df[["ID", "PositionID", "ISIN", "Quantity", "Total Price"]]
    output_df.rename(
        columns={
            "ID": "ID",
            "PositionID": "PositionID",
            "ISIN": "ISIN",
            "Quantity": "Quantity",
            "Total Price": "Total Price",
        },
        inplace=True,
    )
    # Save the output file
    output_df.to_csv("output_files/PositionReport.csv", index=False)
    context.output_df = pd.read_csv("output_files/PositionReport.csv")
    print("Output file is generated and saved to 'output_files/PositionReport.csv'.")

@then("output file should have correct transformations")
def validate_output(context):
    for _, row in context.output_df.iterrows():
        # Calculate the expected Total Price
        expected_total = row["Quantity"] * context.instrument_df.loc[
            context.instrument_df["ISIN"] == row["ISIN"], "Unit Price"
        ].values[0]
        assert row["Total Price"] == expected_total, f"Mismatch for ID {row['ID']}"
    print("Output file validation passed.")
