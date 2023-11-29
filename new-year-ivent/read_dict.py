from datetime import datetime


def result_output(dct):
    with open("Общая_сумма_баллов.txt", "w", encoding="utf-8") as output_result_point:
        for elem in sorted(dct.items()):
            string = f"№{elem[0]} - количество баллов = {elem[1]}"
            print(string, file=output_result_point)


def result_output_and_times(card, point):
    with open("Карточки_даты_получения_баллов.txt", "a", encoding="utf-8") as output_adding_point_and_times:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        string = f"Карточка № {card}, количество баллов {point}, время пополнения {current_time}"
        output_adding_point_and_times.write(string + "\n")
