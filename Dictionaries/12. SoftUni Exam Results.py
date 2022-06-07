text = input()
exam_results = {}
language_dict = {}
while text != "exam finished":
    info = text.split("-")
    name = info[0]
    language = info[1]

    if language != "banned":
        score = int(info[2])
        if name not in exam_results:
            exam_results[name] = score
        else:
            if exam_results[name] < score:
                exam_results[name] = score

        if language not in language_dict:
            language_dict[language] = 1
        else:
            language_dict[language] += 1
    else:
        if name in exam_results:
            exam_results.pop(name)
    text = input()
print("Results:")
for key,value in exam_results.items():

    print(f"{key} | {value}")
print("Submissions:")
for key, value in language_dict.items():

    print(f"{key} - {value}")