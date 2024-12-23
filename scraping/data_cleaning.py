import pandas as pd

# Load the dataset
df = pd.read_csv("allmovies.csv", encoding='utf-8')

# print(df.head())  # Display first few rows
# print(df.info())  # Get column data types and missing values
# print(df.describe())  # Check statistical summary for numerical columns

# print(df.isnull().sum())

# print(df['Genres'].unique())
# print(df['Rating'].unique())
# print(df['Time'].unique())

# Converting time into minutes

# def convert_time_to_minutes(time_str):
#     try:
#         # Remove 'm' and split by 'h'
#         if 'h' in time_str and 'm' in time_str:
#             hours, minutes = map(int, time_str.replace('m', '').split('h'))
#             return hours * 60 + minutes
#         elif 'h' in time_str:  # Handle cases with only hours
#             hours = int(time_str.replace('h', ''))
#             return hours * 60
#         elif 'm' in time_str:  # Handle cases with only minutes
#             minutes = int(time_str.replace('m', ''))
#             return minutes
#         else:  # Handle invalid formats
#             return None
#     except Exception as e:
#         print(f"Error processing time: {time_str}, error: {e}")
#         return None

# # Apply the function to the 'Time' column
# df['Time'] = df['Time'].apply(convert_time_to_minutes)

# # Optional: Handle missing values after conversion
# df['Time'].fillna(0, inplace=True)  # Replace None with 0 or any default value

# #testing with sample data
# sample_data = ['1h 30m', '2h', '45m', '', 'NaN', '3h 20m']
# for time in sample_data:
#     print(f"{time} -> {convert_time_to_minutes(time)}")

# #remove extra spaces or invalid characters 
# df['Genres'] = df['Genres'].str.replace(' ', '').str.strip()
# print(df['Genres'].unique())

# df['Time'].fillna(0, inplace=True)  # Replace None with 0 (or another default value)

# # Hindi to English movie conversion - Sample Data
# from googletrans import Translator

# # Initialize the translator
# translator = Translator()

# # Sample list of movie names in Hindi
# hindi_movie_names = ['दिलवाले दुल्हनिया ले जाएंगे', '3 इडियट्स', 'सागर की कहानियाँ', 'वह यादगार क्रिसमस', 'ग्लेडिएटर', 'बुरे बंदे: हॉन्टेड हाइस्ट' ]

# # Function to translate a list of Hindi movie names to English
# def translate_movie_names(names):
#     translated_names = []
#     for name in names:
#         try:
#             translated = translator.translate(name, src='hi', dest='en')
#             translated_names.append(translated.text)
#         except Exception as e:
#             print(f"Error translating {name}: {e}")
#             translated_names.append(name)  # Append the original name if translation fails
#     return translated_names

# # Translate the movie names
# english_movie_names = translate_movie_names(hindi_movie_names)

# # Output the translated names
# print(english_movie_names)

