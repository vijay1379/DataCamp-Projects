Organizing Medical Transcriptions with the OpenAI API

📌 Project Overview

This project demonstrates how to use the OpenAI API to extract
structured medical information from unstructured medical transcription
text.

By leveraging AI, healthcare providers can reduce administrative
workload and automate the extraction of:

-   Patient age
-   Medical specialty
-   Recommended treatment (from PLAN section)
-   Appropriate ICD-10 code based on diagnosis

------------------------------------------------------------------------

🛠️ Technologies Used

-   Python
-   Pandas
-   OpenAI Python SDK
-   JSON

------------------------------------------------------------------------

📂 Project Structure

    ├── data/
    │   └── transcriptions.csv
    ├── main.py
    ├── README.txt

------------------------------------------------------------------------

🔐 Environment Setup

Before running the project, you must configure your OpenAI API key.

1️⃣ Set Environment Variable (Mac/Linux)

    export OPENAI_API_KEY="your_api_key_here"

2️⃣ Set Environment Variable (Windows - PowerShell)

    setx OPENAI_API_KEY "your_api_key_here"

3️⃣ (Optional) Using a .env file

Create a .env file:

    OPENAI_API_KEY=your_api_key_here

Then install python-dotenv:

    pip install python-dotenv

And add this to the top of your script:

    from dotenv import load_dotenv
    import os

    load_dotenv()

------------------------------------------------------------------------

▶️ How It Works

1.  Load medical transcription data using Pandas.
2.  Send each transcription to the OpenAI API.
3.  Use function calling to extract structured fields.
4.  Convert the results into a structured DataFrame.
5.  Print or export the structured medical data.

------------------------------------------------------------------------

🚀 Running the Project

Install dependencies:

    pip install openai pandas python-dotenv

Run the script:

    python main.py

------------------------------------------------------------------------

📊 Example Output

The script produces a structured DataFrame like:

  age   medical_specialty   recommended_treatment   icd_10_code
  ----- ------------------- ----------------------- -------------
  45    Cardiology          Start beta blockers     I10

------------------------------------------------------------------------

⚠️ Notes

-   Ensure your OpenAI API key is valid.
-   The model used is gpt-4o-mini.
-   This project demonstrates function calling for structured data
    extraction.

------------------------------------------------------------------------

📄 License

This project is for educational and demonstration purposes.
