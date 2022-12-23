key = "20b487e731954ee683ddba763fe40c53"
endpoint = "https://tubokawa-lab-research2.cognitiveservices.azure.com/"

# 各種ライブラリのインポート
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# キーとエンドポイントを利用してクライアントの認証を行う
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, 
        credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example function for detecting sentiment in text
def sentiment_analysis_example(client):
    research_array = []
    array = ["イケメン。","ブス。"]
    for i in range(len(array)):
        documents = {
                "id": i  + 1,
                "language": "ja",
                "text": array[i]
            }
        research_array.append(documents)
    
    print(research_array)

    response = client.analyze_sentiment(documents=research_array)

    for document in response:
        print("Document Id: ", document.id)
        print("Document Sentiment: {}".format(document.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            document.confidence_scores.positive,
            document.confidence_scores.neutral,
            document.confidence_scores.negative,
        ))
        for idx, sentence in enumerate(document.sentences):
            print("Sentence: {}".format(sentence.text))
            print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
            print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative,
            ))
sentiment_analysis_example(client)