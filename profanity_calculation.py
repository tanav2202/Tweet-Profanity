# Import the library to ignore warnings
import pandas as pd
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")
# Open words.txt and read the words into a list
with open('words.txt', 'r') as f:
    words = f.read().splitlines()

# Open tweets.txt and read the sentences into a list
with open('tweets.txt', 'r') as f:
    sentences = f.read().splitlines()

df = pd.DataFrame(columns=['User_ID', 'Tweet', 'Words_Used',
                  'Words_Used_Count', 'Words_Count', 'Degree_of_Profanity'])

# Loop through each sentence in the sentences list
for sentence in sentences:
    # Split the sentence into the User_ID and the tweet text
    user_id, tweet = sentence.split(' ', 1)

    # Count the number of words in the tweet
    words_count = len(tweet.split())

    # Count the number of times each word in the words list appears in the tweet
    words_used = []
    words_used_count = 0
    for word in words:
        count = tweet.count(word)
        if count > 0:
            words_used.append(word)
            words_used_count += count

    # Calculate the degree of profanity in the tweet
    degree_of_profanity = 0
    for word in words_used:
        if word in words:
            degree_of_profanity += 1

    # Add the results to the dataframe
    profanity = degree_of_profanity/words_count
    df = df.append({'User_ID': user_id, 'Tweet': tweet, 'Words_Used': words_used, 'Words_Used_Count': words_used_count,
                   'Words_Count': words_count, 'Degree_of_Profanity': profanity}, ignore_index=True)

df.to_csv('degree_of_word_usage.csv')
