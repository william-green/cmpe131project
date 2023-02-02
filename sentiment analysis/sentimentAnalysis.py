from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

with open("input.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        print("input: " + line)
        print("sentiment: " + analyze_sentiment(line))