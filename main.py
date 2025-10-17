from google import genai

client = genai.Client(api_key="YOUR_API_KEY_HERE")

image_path = "Path to udostakKurmanAli.png"
with open(image_path, "rb") as f:
    image_bytes = f.read()

image_part = genai.types.Part.from_bytes(
    data=image_bytes,
    mime_type='image/png'
)

response = client.models.generate_content(
    model="gemma-3-27b-it",
    contents=[
        genai.types.Part.from_text(text="""You are a data analyst's helper specialized in analyzing student grade certificates. Your task is to accurately extract information from the provided image, which contains text in **Russian and Kazakh languages**.

Instructions:
1.  Extract the following data points: Full Name, Document Number, School Name, and a list of all subjects and their corresponding grades.
2.  Output the result strictly in JSON format.
3.  The output values for Full Name, School Name, and Subject/Grade names must be returned in their original language (Russian or Kazakh).
4.  Be highly meticulous with characters, especially those with diacritics such as ә, ғ, қ, ң, ө, ұ, ү, һ, ensuring their accurate transcription.
5.  Use the following JSON structure:
    ```json
    {
      "full_name": "...", 
      "document_number": "...", 
      "school_name": "...", 
      "grades": [
        {"subject": "...", "grade": "..."}, 
        {"subject": "...", "grade": "..."}
      ]
    }
    ```
6.  If any required field (e.g., "document\_number") is not found in the image, set its value to `null`."""),
        image_part 
    ]
)
print(response.text)

with open("Path to attestatKurmanAli.png", "rb") as r:
    image_bytes2 = r.read()

image_part = genai.types.Part.from_bytes(
    data=image_bytes2,
    mime_type='image/png'
)
response2 = client.models.generate_content(
    model="gemma-3-27b-it",
    contents=[
        genai.types.Part.from_text(text="""You are a data analyst's helper specialized in analyzing student grade certificates. Your task is to accurately extract information from the provided image, which contains text in **Russian and Kazakh languages**.

Instructions:
1.  Extract the following data points: Full Name, Document Number, School Name, and a list of all subjects and their corresponding grades.
2.  Output the result strictly in JSON format.
3.  The output values for Full Name, School Name, and Subject/Grade names must be returned in their original language (Russian or Kazakh).
4.  Be highly meticulous with characters, especially those with diacritics such as ә, ғ, қ, ң, ө, ұ, ү, һ, ensuring their accurate transcription.
5.  Use the following JSON structure:
    ```json
    {
      "full_name": "...", 
      "document_number": "...", 
      "school_name": "...", 
      "grades": [
        {"subject": "...", "grade": "..."}, 
        {"subject": "...", "grade": "..."}
      ]
    }
    ```
6.  If any required field (e.g., "document\_number") is not found in the image, set its value to `null`.
                                   """),
        image_part
    ]
)
print(response2.text)
