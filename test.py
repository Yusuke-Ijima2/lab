research_array = []
array = ["イケメン。","ブス。"]
for i in range(len(array)):
    documents = [
        {
            "id": i + 1,
            "language": "ja",
            "text": array[i]
        }
    ]
    research_array.append(documents)
print(research_array)