key = "20b487e731954ee683ddba763fe40c53"
endpoint = "https://tubokawa-lab-research2.cognitiveservices.azure.com/"

# # 各種ライブラリのインポート
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# # キーとエンドポイントを利用してクライアントの認証を行う
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, 
        credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

with open('q_sentiment_test.txt', 'r') as f:
    q_result_list = f.read().split("\n")

with open('startend.txt', 'r') as f:
    startend = f.read().split("\n")

# int型に変換
startend = list(map(int, startend))
# print(startend)

# with open('w_sentiment_test.txt', 'r') as f:
#     w_result_list = f.read().split("\n")
    
# with open('e_sentiment_test.txt', 'r') as f:
#     e_result_list = f.read().split("\n")

def sentiment_analysis_example(client):
    research_array = []
    start = startend[0]
    end = startend[1]
    # print(q_result_list)
    for i in range(44, 51):
        print(i)
        documents = {
                "id": 1 + i,
                "language": "ja",
                "text": q_result_list[i]
            }
        research_array.append(documents)

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

startend[0] += 10
startend[1] += 10
# print(startend)

startend = list(map(str, startend))
# print(startend)
with open('startend.txt','w') as f:
    f.writelines('\n'.join(startend))