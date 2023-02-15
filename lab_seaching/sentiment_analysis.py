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

with open('e_sentiment_file.txt', 'r') as f:
    q_result_list = f.read().split("\n")

with open('startend.txt', 'r') as f:
    startend = f.read().split("\n")

# int型に変換
startend = list(map(int, startend))

with open('pnn_sum.txt', 'r') as f:
    pnn_sum = f.read().split("\n")
    # float型に変換
    pnn_sum = list(map(float, pnn_sum))

positive_average = 0.0
positive_sum = 0.0
neutral_average = 0.0
neutral_sum = 0.0
negative_average = 0.0
negative_sum = 0.0

def sentiment_analysis_example(client):
    global positive_sum
    global neutral_sum
    global negative_sum
    
    research_array = []
    start = startend[0]
    end = startend[1]
    # print(q_result_list)
    for i in range(start, end):
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
        positive = "{:.2f}".format(document.confidence_scores.positive)
        neutral = "{:.2f}".format(document.confidence_scores.neutral)
        negative = "{:.2f}".format(document.confidence_scores.negative)
        print("positive = " + positive)
        print("neutral = " + neutral)
        print("negative = " + negative)
        print("")
        
        # 合計を求める
        pnn_sum[0] += float(positive)
        pnn_sum[1] += float(neutral)
        pnn_sum[2] += float(negative)
    
    # 平均を求める
    positive_average = pnn_sum[0] / end
    neutral_average = pnn_sum[1] / end
    negative_average = pnn_sum[2] / end
    
    print("合計" + str(end) + "レビュー")
    print("")
    print("positive_sum = " + str(pnn_sum[0]))
    print("neutral_sum = " + str(pnn_sum[1]))
    print("negative_sum = " + str(pnn_sum[2]))
    print("")
    print("positive_average = " + str(positive_average))
    print("neutral_average = " + str(neutral_average))
    print("negative_average = " + str(negative_average))

sentiment_analysis_example(client)

startend[0] += 10
startend[1] += 10

startend = list(map(str, startend))
# print(startend)
with open('startend.txt','w') as f:
    f.writelines('\n'.join(startend))

pnn_sum = list(map(str, pnn_sum))
# print(pnn_sum)
with open('pnn_sum.txt','w') as f:
    f.writelines('\n'.join(pnn_sum))
