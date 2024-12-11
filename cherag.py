import pandas as pd
import io
import os
import pyperclip  # Import pyperclip for clipboard access

def generate_dataset_info_and_prompt(dataset_path):
    while not os.path.isfile(dataset_path):
        print(f"Error: The file at '{dataset_path}' does not exist. Please check the file path and try again.")
        dataset_path = input("Enter the path to your dataset (CSV file): ")

    try:

        data = pd.read_csv(dataset_path)

        info_buffer = io.StringIO()
        data.info(buf=info_buffer)
        info_text = info_buffer.getvalue()

        data_head = data.head()

        # Generate output
        output_text = f"Dataset Info:\n{info_text}\n\nFirst 5 Rows of the Dataset:\n{data_head}\n"

        suggested_prompt = (
            "What would you like to do next? Here are some options:\n"
            "1. Perform Exploratory Data Analysis (EDA)\n"
            "2. Build a machine learning model\n"
            "3. Perform time series forecasting\n"
            "4. Exit\n"
            "Enter the number corresponding to your choice: "
        )

        choice = input(suggested_prompt)

        if choice == "1":
            final_prompt = f'{output_text}\nCan you perform EDA on this dataset?'
        elif choice == "2":
            final_prompt = f'{output_text}\nCan you build a machine learning model to predict column_X using this dataset?'
        elif choice == "3":
            final_prompt = f'{output_text}\nCan you perform time series forecasting?'
        elif choice == "4":
            print(f"Exiting. Feel free to run the script again if you need further assistance!")
            return
        else:
            print(f"Invalid choice. Please rerun the script and try again.")
            return

        # Output final prompt
        print(final_prompt)

        # Copy final prompt to clipboard
        pyperclip.copy(final_prompt)
        print("\nThe final prompt has been copied to the clipboard.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    dataset_path = input("Enter the path to your dataset (CSV file): ")
    generate_dataset_info_and_prompt(dataset_path)
