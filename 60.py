from textblob import TextBlob

blob = TextBlob("I havv a guud ideea")

corrected_blob = blob.correct()

print("Original Text:", blob)
print("Corrected Text:", corrected_blob)