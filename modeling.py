import tkinter as tk
from tkinter import ttk
import random


window = tk.Tk()
window.title("Nums GUI")
window.geometry('1650x600')
window.resizable(0, 0)

oneGrades = []


def generate_nums():

    oneGrades = list(l_users_data_1st_text.get().split(' '))


    if len(oneGrades) < 10:


        list_rnd_1raz = []

        state1 = random.getstate()

        list_rnd_1raz = []

        for i in range(0, 1000):
            rnd = random.randint(0, 9)
            list_rnd_1raz.append(rnd)
            i += 1
        list_rnd_1raz_new = list_rnd_1raz[0: 10]

        row_rnd_1raz = 2

        for i in range(len(list_rnd_1raz_new)):
            data = tk.Label(frame_main_inform, text=list_rnd_1raz_new[i], width=14, relief="groove")
            data.grid(column=4, row=row_rnd_1raz)
            row_rnd_1raz += 1
            i += 1

        print(state1)

        random.setstate(state1)
        list_rnd_1raz_checking = []

        for i in range(0, 1000):
            rnd = random.randint(0, 9)
            list_rnd_1raz_checking.append(rnd)
            i += 1
        print(list_rnd_1raz_checking)




        x = 0
        for i in range(len(list_rnd_1raz)):
            if list_rnd_1raz[i] not in nums1_empty:
                nums1_empty.append(list_rnd_1raz[i])
                colours_empty.append(list_colour[x])
                x += 1

        i = 0

        for col in range(15):
            for row in range(12):
                data = tk.Label(frame_vizual2, text=list_rnd_1raz[i], width=2, bg=colours_empty[nums1_empty.index(list_rnd_1raz[i])])
                data.grid(column=col, row=row)
                i += 1

        if list_rnd_1raz == list_rnd_1raz_checking:
            table_count1 = tk.Label(frame_main_inform, text=1, width=14, relief="groove", bg="#F0E68C")
            table_count1.grid(column=4, row=13)
        else:
            table_count1 = tk.Label(frame_main_inform, text=0, width=14, relief="groove", bg="#F0E68C")
            table_count1.grid(column=4, row=13)

    else:

        row_rnd_1raz = 2
        oneGrades = [int(i) for i in oneGrades]

        for i in range(len(oneGrades)):
            data = tk.Label(frame_main_inform, text=oneGrades[i], width=14, relief="groove")
            data.grid(column=4, row=row_rnd_1raz)
            row_rnd_1raz += 1
            i += 1

        nums1_empty_entry = []
        colours_empty_entry = []

        x = 0
        for i in range(len(oneGrades)):
            if oneGrades[i] not in nums1_empty_entry:
                nums1_empty_entry.append(oneGrades[i])
                colours_empty_entry.append(list_colour[x])
                x += 1

        i = 0

        for col in range(3):
            for row in range(3):
                data = tk.Label(frame_vizual6, text=oneGrades[i], width=2, bg=colours_empty_entry[nums1_empty_entry.index(oneGrades[i])])
                data.grid(column=col, row=row)
                i += 1







    if len(oneGrades) < 10:
        list_1raz_algoritm = list_rnd_1raz

        i = 0
        list_count1_alg = []

        while i < 10:

            for i in range(0, 10):
                amount = list_1raz_algoritm.count(i)
                list_count1_alg.append(amount)
                i += 1

        l1_persent_alg = [(i * 100) / len(list_1raz_algoritm) for i in list_count1_alg]

        summ1_alg = 0
        persent_list1_alg = []
        x = 0
        for i in list_count1_alg:
            summ1_alg = i * l1_persent_alg[x] / 100
            persent_list1_alg.append(summ1_alg)
            x += 1

        persent_list1_summ_alg = sum(persent_list1_alg)

        res1_alg = persent_list1_summ_alg * 100 / len(list_1raz_algoritm)
        res1_alg = int(res1_alg * 100) / 100

        kr1_to_alg1 = tk.Label(frame_main_inform, text=res1_alg, width=14, relief="groove", bg="#F0E68C")
        kr1_to_alg1.grid(column=4, row=12)

    else:

        list_1raz_algoritm = oneGrades
        print(list_1raz_algoritm)

        x = 0
        list_count1_alg = []

        while x < 10:

            for i in range(0, 10):
                amount = list_1raz_algoritm.count(x)
                list_count1_alg.append(amount)
                x += 1



        l1_persent_alg = [(i * 100) / len(list_1raz_algoritm) for i in list_count1_alg]

        summ1_alg = 0
        persent_list1_alg = []
        x = 0
        for i in list_count1_alg:
            summ1_alg = i * l1_persent_alg[x] / 100
            persent_list1_alg.append(summ1_alg)
            x += 1

        persent_list1_summ_alg = sum(persent_list1_alg)



        res1_alg = persent_list1_summ_alg * 100 / len(list_1raz_algoritm)
        res1_alg = int(res1_alg * 100) / 100


        kr1_to_alg = tk.Label(frame_main_inform, text=res1_alg, width=14, relief="groove", bg="#F0E68C")
        kr1_to_alg.grid(column=4, row=12)



    twoGrades = list(l_users_data_2st_text.get().split(' '))


    if len(twoGrades) < 10:

        list_rnd_2raz = []

        state2 = random.getstate()
        list_rnd_2raz = []


        for i in range(0, 1000):
            rnd = random.randint(10, 99)

            list_rnd_2raz.append(rnd)
            i += 1


        list_rnd_2raz_new = list_rnd_2raz[0: 10]
        row_rnd_2raz = 2

        for i in range(len(list_rnd_2raz_new)):
            data = tk.Label(frame_main_inform, text=list_rnd_2raz_new[i], width=14, relief="groove")
            data.grid(column=5, row=row_rnd_2raz)
            row_rnd_2raz += 1
            i += 1



        print(state2)
        random.setstate(state2)

        list_rnd_2raz_checking = []


        for i in range(0, 1000):
            rnd = random.randint(10, 99)

            list_rnd_2raz_checking.append(rnd)
            i += 1

        print(list_rnd_2raz_checking)

        if list_rnd_2raz == list_rnd_2raz_checking:
            table_count1 = tk.Label(frame_main_inform, text=1, width=14, relief="groove", bg="#F0E68C")
            table_count1.grid(column=5, row=13)
        else:
            table_count1 = tk.Label(frame_main_inform, text=0, width=14, relief="groove", bg="#F0E68C")
            table_count1.grid(column=5, row=13)

        nums1_empty2 = []
        colours_empty2 = []

        for i in range(len(list_rnd_2raz)):
            if list_rnd_2raz[i] not in nums1_empty2:
                nums1_empty2.append(list_rnd_2raz[i])
                colours_empty2.append(list_colour[x])
                x += 1

        i = 0

        for col in range(15):
            for row in range(12):
                data = tk.Label(frame_vizual4, text=list_rnd_2raz[i], width=2, bg=colours_empty2[nums1_empty2.index(list_rnd_2raz[i])])

                data.grid(column=col, row=row)
                i += 1



    else:

        row_rnd_2raz = 2
        twoGrades = [int(i) for i in twoGrades]

        for i in range(len(twoGrades)):
            data = tk.Label(frame_main_inform, text=twoGrades[i], width=14, relief="groove")
            data.grid(column=5, row=row_rnd_2raz)
            row_rnd_2raz += 1
            i += 1



        nums1_empty_entry = []
        colours_empty_entry = []

        x = 0
        for i in range(len(twoGrades)):
            if twoGrades[i] not in nums1_empty_entry:
                nums1_empty_entry.append(twoGrades[i])
                colours_empty_entry.append(list_colour[x])
                x += 1

        i = 0

        for col in range(3):
            for row in range(3):
                data = tk.Label(frame_vizual7, text=twoGrades[i], width=2, bg=colours_empty_entry[nums1_empty_entry.index(twoGrades[i])])
                data.grid(column=col, row=row)
                i += 1




    if len(twoGrades) < 10:

        list_2raz_algoritm = list_rnd_2raz

        x = 10
        list_count2_alg = []

        while x < 100:

            for i in range(0, 100):
                amount = list_2raz_algoritm.count(x)
                list_count2_alg.append(amount)
                x += 1

        l2_persent_alg = [(i * 100) / len(list_2raz_algoritm) for i in list_count2_alg]

        summ2_alg = 0
        persent_list2_alg = []
        x = 0
        for i in list_count2_alg:
            summ2_alg = i * l2_persent_alg[x] / 100
            persent_list2_alg.append(summ2_alg)
            x += 1

        persent_list2_summ_alg = sum(persent_list2_alg)

        res2_alg = persent_list2_summ_alg * 100 / len(list_2raz_algoritm)
        res2_alg = int(res2_alg * 100) / 100

        kr1_to_alg2 = tk.Label(frame_main_inform, text=res2_alg, width=14, relief="groove", bg="#F0E68C")
        kr1_to_alg2.grid(column=5, row=12)



    else:

        list_2raz_algoritm = twoGrades

        x = 10
        list_count2_alg = []

        while x < 100:

            for i in range(0, 100):
                amount = list_2raz_algoritm.count(x)
                list_count2_alg.append(amount)
                x += 1

        l2_persent_alg = [(i * 100) / len(list_2raz_algoritm) for i in list_count2_alg]

        summ2_alg = 0
        persent_list2_alg = []
        x = 0
        for i in list_count2_alg:
            summ2_alg = i * l2_persent_alg[x] / 100
            persent_list2_alg.append(summ2_alg)
            x += 1

        persent_list2_summ_alg = sum(persent_list2_alg)

        res2_alg = persent_list2_summ_alg * 100 / len(list_2raz_algoritm)
        res2_alg = int(res2_alg * 100) / 100

        kr1_to_alg2 = tk.Label(frame_main_inform, text=res2_alg, width=14, relief="groove", bg="#F0E68C")
        kr1_to_alg2.grid(column=5, row=12)


    threeGrades = list(l_users_data_3st_text.get().split(' '))


    if len(threeGrades) < 10:

        list_rnd_3raz = []

        state3 = random.getstate()
        list_rnd_3raz = []

        for i in range(0, 1000):
            rnd = random.randint(100, 999)

            list_rnd_3raz.append(rnd)
            i += 1

        list_rnd_3raz_new = list_rnd_3raz[0: 10]
        row_rnd_3raz = 2


        for i in range(len(list_rnd_3raz_new)):
            data = tk.Label(frame_main_inform, text=list_rnd_3raz_new[i], width=14, relief="groove")
            data.grid(column=6, row=row_rnd_3raz)
            row_rnd_3raz += 1
            i += 1

        print(state3)
        random.setstate(state3)

        list_rnd_3raz_checking = []

        for i in range(0, 1000):
            rnd = random.randint(100, 999)

            list_rnd_3raz_checking.append(rnd)
            i += 1

        print(list_rnd_3raz_checking)

        if list_rnd_3raz == list_rnd_3raz_checking:
            table_count1 = tk.Label(frame_main_inform, text=1, width=14, relief="groove", bg="#F0E68C")
            table_count1.grid(column=6, row=13)
        else:
            table_count1 = tk.Label(frame_main_inform, text=0, width=14, relief="groove", bg="#F0E68C")
            table_count1.grid(column=6, row=13)

    else:

        row_rnd_3raz = 2
        threeGrades = [int(i) for i in threeGrades]

        for i in range(len(threeGrades)):
            data = tk.Label(frame_main_inform, text=threeGrades[i], width=14, relief="groove")
            data.grid(column=6, row=row_rnd_3raz)
            row_rnd_3raz += 1
            i += 1


    if len(threeGrades) < 10:

        list_3raz_algoritm = list_rnd_3raz

        ch3 = 100
        list_count3_alg = []

        while ch3 < 1000:

            for i in range(0, 1000):
                amount = list_3raz_algoritm.count(ch3)
                list_count3_alg.append(amount)
                ch3 += 1

        l3_persent_alg = [(i * 100) / len(list_3raz_algoritm) for i in list_count3_alg]

        summ3_alg = 0
        persent_list3_alg = []
        x = 0
        for i in list_count3_alg:
            summ3_alg = i * l3_persent_alg[x] / 100
            persent_list3_alg.append(summ3_alg)
            x += 1

        persent_list3_summ_alg = sum(persent_list3_alg)

        res3_alg = persent_list3_summ_alg * 100 / len(list_3raz_algoritm)
        res3_alg = int(res3_alg * 100) / 100

        kr1_to_alg3 = tk.Label(frame_main_inform, text=res3_alg, width=14, relief="groove", bg="#F0E68C")
        kr1_to_alg3.grid(column=6, row=12)

    else:

        list_3raz_algoritm = threeGrades

        ch3 = 100
        list_count3_alg = []

        while ch3 < 1000:

            for i in range(0, 1000):
                amount = list_3raz_algoritm.count(ch3)
                list_count3_alg.append(amount)
                ch3 += 1

        l3_persent_alg = [(i * 100) / len(list_3raz_algoritm) for i in list_count3_alg]

        summ3_alg = 0
        persent_list3_alg = []
        x = 0
        for i in list_count3_alg:
            summ3_alg = i * l3_persent_alg[x] / 100
            persent_list3_alg.append(summ3_alg)
            x += 1

        persent_list3_summ_alg = sum(persent_list3_alg)

        res3_alg = persent_list3_summ_alg * 100 / len(list_3raz_algoritm)
        res3_alg = int(res3_alg * 100) / 100

        kr1_to_alg3 = tk.Label(frame_main_inform, text=res3_alg, width=14, relief="groove", bg="#F0E68C")
        kr1_to_alg3.grid(column=6, row=12)




##########################################################################################################

frame_main_inform = tk.Frame(window, width=700, height=350, bg='#90EE90')
frame_adding_place = tk.Frame(window, width=350, height=250, bg='#AFEEEE')
frame_statistic = tk.Frame(window, width=350, height=250, bg='#FFEBCD')


frame_main_inform.grid(column=0, row=1, columnspan=2, sticky="snwe")
frame_adding_place.grid(column=0, row=0, sticky="nwse")
frame_statistic.grid(column=1, row=0, sticky="nswe")

###########################################################################################################
l_random_common_empty = tk.Label(frame_statistic, text="", bg='#FFEBCD')
l_random_common_empty.grid(row=0, column=0, pady=25)

l_random_common = tk.Label(frame_statistic, text="Критерий №1(Кр.№1): ", font="Arial 10 bold", bg='#FFEBCD')
l_random_common.grid(row=1, column=0)

l_random_common_text1 = tk.Label(frame_statistic, text="Норма для 1 разряда = 10", font="Helvetica 10", bg='#FFEBCD')
l_random_common_text1.grid(row=1, column=1, sticky="w")

l_random_common_text2 = tk.Label(frame_statistic, text="Норма для 2 разряда = 1", font="Helvetica 10", bg='#FFEBCD')
l_random_common_text2.grid(row=2, column=1, sticky="w")

l_random_common_text3 = tk.Label(frame_statistic, text="Норма для 3 разряда = 0.1", font="Helvetica 10", bg='#FFEBCD')
l_random_common_text3.grid(row=3, column=1, sticky="w")


l_random_common_empty = tk.Label(frame_statistic, text="", bg='#FFEBCD')
l_random_common_empty.grid(row=4, column=0, pady=7)


l_random_commonKR2 = tk.Label(frame_statistic, text="Критерий №2(Кр.№2): ", font="Arial 10 bold", bg='#FFEBCD')
l_random_commonKR2.grid(row=5, column=0)

l_random_common_KR2text1 = tk.Label(frame_statistic, text="Норма = 0", font="Helvetica 10", bg='#FFEBCD')
l_random_common_KR2text1.grid(row=5, column=1, sticky="w")

l_random_common_KR2text2 = tk.Label(frame_statistic, text="Отклонение = 1", font="Helvetica 10", bg='#FFEBCD')
l_random_common_KR2text2.grid(row=6, column=1, sticky="w")


############################################################################################################


l_users_empty = tk.Label(frame_adding_place, text="", bg='#AFEEEE')
l_users_empty.grid(column=0, row=0)
l_users_empty2 = tk.Label(frame_adding_place, text="", bg='#AFEEEE')
l_users_empty2.grid(column=0, row=1)


l_adding_information = tk.Label(frame_adding_place, text="Введите 10 произвольных чисел через пробел", font="Helvetica 11 bold"
                                , bg='#AFEEEE')
l_adding_information.place(relx=0.05, rely=0.05)


l_users_data_1st = tk.Label(frame_adding_place, text="Одноразрядные: ", bg='#AFEEEE',
                            font="Arial 10 bold")
l_users_data_1st_text = tk.Entry(frame_adding_place, width=35, justify=tk.LEFT)
l_users_data_1st.grid(column=0, row=2, sticky="w", padx=10, pady=20)
l_users_data_1st_text.grid(column=1, row=2, sticky="e", padx=10, pady=20)


l_users_data_2st = tk.Label(frame_adding_place, text="Двухразрядные: ", bg='#AFEEEE',
                            font="Arial 10 bold")
l_users_data_2st_text = tk.Entry(frame_adding_place, width=35, justify=tk.LEFT)
l_users_data_2st.grid(column=0, row=3, sticky="w", padx=10, pady=20)
l_users_data_2st_text.grid(column=1, row=3, sticky="e", padx=10, pady=20)


l_users_data_3st = tk.Label(frame_adding_place, text="Трехразрядные: ", bg='#AFEEEE',
                            font="Arial 10 bold")
l_users_data_3st_text = tk.Entry(frame_adding_place, width=35, justify=tk.LEFT)
l_users_data_3st.grid(column=0, row=4, sticky="w", padx=10, pady=20)
l_users_data_3st_text.grid(column=1, row=4, sticky="e", padx=10, pady=20)


l_btn_gen = tk.Button(frame_adding_place, text="Старт", command=generate_nums, font="Arial 12 bold")
l_btn_gen.grid(column=0, row=5, columnspan=2, pady=15)


"""
37542 04805  64894 74296  24805 24037  20636 10402  00822 91665
08422 68953  19645 09303  23209 02560  15953 34764  35080 33606
99019 02529  09376 70715  38311 31165  88676 74397  04436 27659
12807 99970  80157 36147  64032 36653  98951 16877  12171 76833
66065 74717  34072 76850  36697 36170  65813 39885  11199 29170
31060 10805  45571 82406  35303 42614  86799 07439  23403 09732
85269 77602  02051 65692  68665 74818  73053 85247  18623 88579
63573 32135  05325 47048  90553 57548  28468 28709  83491 25624
73796 45753  03529 64778  35808 34282  60935 20344  35273 88435
"""

##########################################################################################################
# создаем заголовки для таблицы

table_emptyRow = tk.Label(frame_main_inform, text="")
table_emptyRow.grid(column=0, row=0)

table_group1 = tk.Label(frame_main_inform, text="Табличные значения", width=55, bd=4, relief="groove")
# table_group1.grid(column=0, row=0, columnspan=3)
table_group1.place(relx=0, rely=0)

table_group2 = tk.Label(frame_main_inform, text="Алгоритмические значения", width=46, bd=4, relief="groove")
# table_group2.grid(column=1, row=0, columnspan=3)
table_group2.place(relx=0.552, rely=0)



table_head_id = tk.Label(frame_main_inform, text="№ п/п", width=10, relief="groove")
table_head_id.grid(column=0, row=1)

table_head_1raz = tk.Label(frame_main_inform, text="1 разряд", width=14, relief="groove")
table_head_1raz.grid(column=1, row=1)

table_head_2raz = tk.Label(frame_main_inform, text="2 разряд", width=14, relief="groove")
table_head_2raz.grid(column=2, row=1)

table_head_3raz = tk.Label(frame_main_inform, text="3 разряд", width=14, relief="groove")
table_head_3raz.grid(column=3, row=1)

table_head_1raz_2 = tk.Label(frame_main_inform, text="1 разряд", width=14, relief="groove")
table_head_1raz_2.grid(column=4, row=1)

table_head_2raz_2 = tk.Label(frame_main_inform, text="2 разряд", width=14, relief="groove")
table_head_2raz_2.grid(column=5, row=1)

table_head_3raz_2 = tk.Label(frame_main_inform, text="3 разряд", width=14, relief="groove")
table_head_3raz_2.grid(column=6, row=1)



table_count_head = tk.Label(frame_main_inform, text="Кр. №1", width=10, relief="groove", bg="#FFD700")
table_count_head.grid(column=0, row=12)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=1, row=12)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=2, row=12)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=3, row=12)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=4, row=12)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=5, row=12)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=6, row=12)


table_count_head = tk.Label(frame_main_inform, text="Кр. №2", width=10, relief="groove", bg="#FFD700")
table_count_head.grid(column=0, row=13)

table_count1 = tk.Label(frame_main_inform, text="0", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=1, row=13)

table_count1 = tk.Label(frame_main_inform, text="0", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=2, row=13)

table_count1 = tk.Label(frame_main_inform, text="0", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=3, row=13)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=4, row=13)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=5, row=13)

table_count1 = tk.Label(frame_main_inform, text="", width=14, relief="groove", bg="#F0E68C")
table_count1.grid(column=6, row=13)


######################################################################################################
# заполняем таблицу табличными значениями

list_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
row_id = 2

for i in range(len(list_id)):

    data=tk.Label(frame_main_inform, text=list_id[i], width=10, relief="groove")
    data.grid(column=0, row=row_id)
    row_id += 1
    i += 1


list_1raz = [3, 7, 5, 4, 2, 0, 4, 8, 0, 5]
row_1raz = 2

for i in range(len(list_1raz)):

    data=tk.Label(frame_main_inform, text=list_1raz[i], width=14, relief="groove")
    data.grid(column=1, row=row_1raz)
    row_1raz += 1
    i += 1


list_2raz = [64, 89, 47, 42, 96, 24, 80, 52, 40, 37]
row_2raz = 2

for i in range(len(list_2raz)):

    data=tk.Label(frame_main_inform, text=list_2raz[i], width=14, relief="groove")
    data.grid(column=2, row=row_2raz)
    row_2raz += 1
    i += 1


list_3raz = [206, 361, 402, 822, 916, 650, 842, 268, 953, 196]
row_3raz = 2


for i in range(len(list_3raz)):

    data=tk.Label(frame_main_inform, text=list_3raz[i], width=14, relief="groove")
    data.grid(column=3, row=row_3raz)
    row_3raz += 1
    i += 1

########################################################################################################
# алгоритмический способ Mersenne twister (Вихрь Мерсенна)

state1 = random.getstate()

list_rnd_1raz = []

for i in range(0, 1000):
    rnd = random.randint(0, 9)
    list_rnd_1raz.append(rnd)
    i += 1
list_rnd_1raz_new = list_rnd_1raz[0: 10]




print(state1)

random.setstate(state1)
list_rnd_1raz_checking = []

for i in range(0, 1000):
    rnd = random.randint(0, 9)
    list_rnd_1raz_checking.append(rnd)
    i += 1
print(list_rnd_1raz_checking)

if list_rnd_1raz == list_rnd_1raz_checking:
    table_count1 = tk.Label(frame_main_inform, text=1, width=14, relief="groove", bg="#F0E68C")
    table_count1.grid(column=4, row=13)
else:
    table_count1 = tk.Label(frame_main_inform, text=0, width=14, relief="groove", bg="#F0E68C")
    table_count1.grid(column=4, row=13)

#######################################


state2 = random.getstate()
list_rnd_2raz = []


for i in range(0, 1000):
    rnd = random.randint(10, 99)
    list_rnd_2raz.append(rnd)
    i += 1

list_rnd_2raz_new = list_rnd_2raz[0: 10]


print(state2)
random.setstate(state2)

list_rnd_2raz_checking = []

for i in range(0, 1000):
    rnd = random.randint(10, 99)
    list_rnd_2raz_checking.append(rnd)
    i += 1

print(list_rnd_2raz_checking)

if list_rnd_2raz == list_rnd_2raz_checking:
    table_count1 = tk.Label(frame_main_inform, text=1, width=14, relief="groove", bg="#F0E68C")
    table_count1.grid(column=5, row=13)
else:
    table_count1 = tk.Label(frame_main_inform, text=0, width=14, relief="groove", bg="#F0E68C")
    table_count1.grid(column=5, row=13)

############################################


state3 = random.getstate()
list_rnd_3raz = []

for i in range(0, 1000):
    rnd = random.randint(100, 999)
    list_rnd_3raz.append(rnd)
    i += 1


print(state3)
list_rnd_3raz_new = list_rnd_3raz[0: 10]


random.setstate(state3)

list_rnd_3raz_checking = []


for i in range(0, 1000):
    rnd = random.randint(100, 999)
    list_rnd_3raz_checking.append(rnd)
    i += 1

print(list_rnd_3raz_checking)

if list_rnd_3raz == list_rnd_3raz_checking:
    table_count1 = tk.Label(frame_main_inform, text=1, width=14, relief="groove", bg="#F0E68C")
    table_count1.grid(column=6, row=13)
else:
    table_count1 = tk.Label(frame_main_inform, text=0, width=14, relief="groove", bg="#F0E68C")
    table_count1.grid(column=6, row=13)






#########################################################################################################
# добавляем алгоритмические значения в таблицу

row_rnd_1raz = 2

for i in range(len(list_rnd_1raz_new)):

    data=tk.Label(frame_main_inform, text=list_rnd_1raz_new[i], width=14, relief="groove")
    data.grid(column=4, row=row_rnd_1raz)
    row_rnd_1raz += 1
    i += 1


row_rnd_2raz = 2

for i in range(len(list_rnd_2raz_new)):

    data=tk.Label(frame_main_inform, text=list_rnd_2raz_new[i], width=14, relief="groove")
    data.grid(column=5, row=row_rnd_2raz)
    row_rnd_2raz += 1
    i += 1


row_rnd_3raz = 2

for i in range(len(list_rnd_3raz_new)):

    data=tk.Label(frame_main_inform, text=list_rnd_3raz_new[i], width=14, relief="groove")
    data.grid(column=6, row=row_rnd_3raz)
    row_rnd_3raz += 1
    i += 1

#######################################################################################################
# критерий №1 для табличных 1 разряд

list_1raz_table = [3754204805648947429624805240372063610402008229166508422689531964509303232090256015953347643508033606990190252909376707153831131165886767439704436276591280799970801573614764032366539895116877]


list_1raz_table_new = [int(i) for number in list_1raz_table for i in str(number)]

# ####################
# расчет кол-ва элементов

i = 0
list_count1 = []

while i < 10:

    for i in range(0, 10):
        amount = list_1raz_table_new.count(i)
        list_count1.append(amount)
        i += 1


#######################
# высчитываем процент
l1_persent = [(i * 100) / len(list_1raz_table_new) for i in list_count1]


#######################
# высчитываем среднее

summ1 = 0
persent_list1 =[]
x = 0
for i in list_count1:
    summ1 = i * l1_persent[x]/100
    persent_list1.append(summ1)
    x += 1

persent_list1_summ = sum(persent_list1)

res1 = persent_list1_summ * 100 / len(list_1raz_table_new)
res1 = int(res1 * 100) / 100


kr1_to_table1 = tk.Label(frame_main_inform, text=res1, width=14, relief="groove", bg="#F0E68C")
kr1_to_table1.grid(column=1, row=12)


# #######################################################################################################
# # критерий №1 для табличных 2 разряд

list_2raz_table = [6489474296248052403720636104020082291665084226895319645093032320902560159533476435080336069901902529093767071538311311658867674397044362765912807999708015736147640323665398951168771217176833660657471734072768503669736170658133988511199291703106010805455718240635303426148679907439234030973285269776020205165692686657481873053852471862388579]
list_2raz_table_new = [int(i) for number in list_2raz_table for i in str(number)]


str2 = ''.join(str(i) for i in list_2raz_table_new)

list_2sep = [str2[i] + str2[i+1] for i in range(len(str2)) if i < len(str2)-1]


check = '0'

list_2sep = [idx for idx in list_2sep if idx[0].lower() != check.lower()]


i = 0
for i in range (len(list_2sep)):
    list_2sep[i] = int(list_2sep[i])
    i += 1


# #####################
# #расчет кол-во элементов

x = 10
list_count2 = []

while x < 100:

    for i in range(0, 100):
        amount = list_2sep.count(x)
        list_count2.append(amount)
        x += 1


# # #######################
# # # высчитываем процент
l2_persent = [(i * 100) / len(list_2raz_table_new) for i in list_count2]


# #######################
# # высчитываем среднее

summ2 = 0
persent_list2 =[]
x = 0
for i in list_count2:
    summ2 = i * l2_persent[x]/100
    persent_list2.append(summ2)
    x += 1

persent_list2_summ = sum(persent_list2)

res2 = persent_list2_summ * 100 / len(list_2raz_table_new)
res2 = int(res2 * 100) / 100


kr1_to_table1 = tk.Label(frame_main_inform, text=res2, width=14, relief="groove", bg="#F0E68C")
kr1_to_table1.grid(column=2, row=12)



# #######################################################################################################
# # критерий №1 для табличных 3 разряд

list_3raz_table = [206361402822916650842268953196450930323209025601595334764350803360699019025290937670715383113116588676743970443627659128079997080157361476403236653989511687712171768336606574717340727685036697361706581339885111992917031060108054557182406353034261486799074392340309732852697760202051656926866574818730538524718623885796357332135053254704890553575482846828709834912562473796457530352964778358083428260935203443527388435]
list_3raz_table_new = [int(i) for number in list_3raz_table for i in str(number)]


str3 = ''.join(str(i) for i in list_3raz_table_new)


n = 3
str3 = [str3[i:i+n] for i in range(0, len(str3), n)]

check = '0'

str3 = [idx for idx in str3 if idx[0].lower() != check.lower()]

int_str3 = [int(i) for i in str3]


# # #####################
# # #расчет кол-во элементов


x1 = 100
list_count3 = []

while x < 1000:

    for i in range(0, 1000):
        amount = int_str3.count(x)
        list_count3.append(amount)
        x += 1


# # # #######################
# # # # высчитываем процент
l3_persent = [(i * 100) / len(list_3raz_table_new) for i in list_count3]



# # #######################
# # # высчитываем среднее

summ3 = 0
persent_list3 =[]
x = 0
for i in list_count3:
    summ3 = i * l3_persent[x]/100
    persent_list3.append(summ3)
    x += 1

persent_list3_summ = sum(persent_list3)

res3 = persent_list3_summ * 100 / len(list_3raz_table_new)
res3 = int(res3 * 100) / 100


kr1_to_table3 = tk.Label(frame_main_inform, text=res3, width=14, relief="groove", bg="#F0E68C")
kr1_to_table3.grid(column=3, row=12)



# ####################################################################################################
# # критерий №1 для алгоритмических 1 разряд

list_1raz_algoritm = list_rnd_1raz


# # ####################
# # расчет кол-ва элементов

i = 0
list_count1_alg = []

while i < 10:

    for i in range(0, 10):
        amount = list_1raz_algoritm.count(i)
        list_count1_alg.append(amount)
        i += 1



# #######################
# # высчитываем процент

l1_persent_alg = [(i * 100) / len(list_1raz_algoritm) for i in list_count1_alg]


# #######################
# # высчитываем среднее

summ1_alg = 0
persent_list1_alg =[]
x = 0
for i in list_count1_alg:
    summ1_alg = i * l1_persent_alg[x]/100
    persent_list1_alg.append(summ1_alg)
    x += 1

persent_list1_summ_alg = sum(persent_list1_alg)

res1_alg = persent_list1_summ_alg * 100 / len(list_1raz_algoritm)
res1_alg = int(res1_alg * 100) / 100


kr1_to_alg1 = tk.Label(frame_main_inform, text=res1_alg, width=14, relief="groove", bg="#F0E68C")
kr1_to_alg1.grid(column=4, row=12)


# ##################################################################################################
# # критерий №1 для табличных 2 разряд


list_2raz_algoritm = list_rnd_2raz

# #####################
# #расчет кол-во элементов

x = 10
list_count2_alg = []

while x < 100:

    for i in range(0, 100):
        amount = list_2raz_algoritm.count(x)
        list_count2_alg.append(amount)
        x += 1


#########################
### высчитываем процент

l2_persent_alg = [(i * 100) / len(list_2raz_algoritm) for i in list_count2_alg]


# #######################
# # высчитываем среднее


summ2_alg = 0
persent_list2_alg =[]
x = 0
for i in list_count2_alg:
    summ2_alg = i * l2_persent_alg[x]/100
    persent_list2_alg.append(summ2_alg)
    x += 1

persent_list2_summ_alg = sum(persent_list2_alg)

res2_alg = persent_list2_summ_alg * 100 / len(list_2raz_algoritm)
res2_alg = int(res2_alg * 100) / 100


kr1_to_alg2 = tk.Label(frame_main_inform, text=res2_alg, width=14, relief="groove", bg="#F0E68C")
kr1_to_alg2.grid(column=5, row=12)


# ##################################################################################################
# # критерий №1 для табличных 3 разряд

list_3raz_algoritm = list_rnd_3raz

# # #####################
# # #расчет кол-во элементов

ch3 = 100
list_count3_alg = []

while ch3 < 1000:

    for i in range(0, 1000):
        amount = list_3raz_algoritm.count(ch3)
        list_count3_alg.append(amount)
        ch3 += 1


# # # #######################
# # # # высчитываем процент

l3_persent_alg = [(i * 100) / len(list_3raz_algoritm) for i in list_count3_alg]

# # #######################
# # # высчитываем среднее

summ3_alg = 0
persent_list3_alg =[]
x = 0
for i in list_count3_alg:
    summ3_alg = i * l3_persent_alg[x]/100
    persent_list3_alg.append(summ3_alg)
    x += 1

persent_list3_summ_alg = sum(persent_list3_alg)

res3_alg = persent_list3_summ_alg * 100 / len(list_3raz_algoritm)
res3_alg = int(res3_alg * 100) / 100


kr1_to_alg3 = tk.Label(frame_main_inform, text=res3_alg, width=14, relief="groove", bg="#F0E68C")
kr1_to_alg3.grid(column=6, row=12)


#######################################################################################################
#Критерий для визуальной оценки


frame_vizual = tk.Frame(window, width=250, height=300)
frame_vizual.grid(column=2, row=0)
text_inform1 = tk.Label(window, text="Визуализация 1 разряд. Табличные.", font="Arial 10 bold")
text_inform1.place(relx=0.43, rely=0)
text_inform1 = tk.Label(window, text="Визуализация 1 разряд. Алгоритм.", font="Arial 10 bold")
text_inform1.place(relx=0.43, rely=0.495)
text_inform1 = tk.Label(window, text="Визуализация 2 разряд. Табличные.", font="Arial 10 bold")
text_inform1.place(relx=0.635, rely=0)
text_inform1 = tk.Label(window, text="Визуализация 2 разряд. Алгоритм.", font="Arial 10 bold")
text_inform1.place(relx=0.635, rely=0.495)



frame_vizual2 = tk.Frame(window, width=250, height=300)
frame_vizual2.grid(column=2, row=1)



frame_vizual3_empty = tk.Frame(window, width=50, height=300)
frame_vizual3_empty.grid(column=3, row=0)

frame_vizual3 = tk.Frame(window, width=250, height=300)
frame_vizual3.grid(column=4, row=0)

frame_vizual4 = tk.Frame(window, width=250, height=300)
frame_vizual4.grid(column=4, row=1)


frame_vizual5_empty = tk.Frame(window, width=60, height=300)
frame_vizual5_empty.grid(column=6, row=0)


frame_vizual6 = tk.Frame(window, width=100, height=300)
frame_vizual6.grid(column=7, row=0)

frame_vizual7_empty = tk.Frame(window, width=30, height=300)
frame_vizual7_empty.grid(column=8, row=0)

frame_vizual7 = tk.Frame(window, width=100, height=300)
frame_vizual7.grid(column=9, row=0)

text_inform1 = tk.Label(window, text="Пользовательский ввод.", font="Arial 10 bold")
text_inform1.place(relx=0.85, rely=0.1)




list_colour = ['#CD5C5C', '#ADFF2F', '#FFC0CB', '#FFA07A', '#FFD700', '#E6E6FA', '#FFF8DC', '#000000', '#FF00FF', '#000080',
               '#808080', '#C0C0C0', '#FFFFFF', '#800080', '#FF0000', '#800000', '#FFFF00', '#808000', '#00FF00', '#008000',
               '#00FFFF', '#008080', '#0000FF', '#FFA07A', '#32CD32', '#FF69B4', '#228B22', '#B22222', '#808000', '#008B8B',
               '#DB7093', '#FF4500', '#FF7F50', '#C71585', '#8FBC8F', '#FFDAB9', '#BDB76B', '#7B68EE', '#FFEFD5', '#B0C4DE',
               '#D8BFD8', '#DDA0DD', '#DA70D6', '#BA55D3', '#9370DB', '#8A2BE2', '#9400D3', '#8B008B', '#4B0082', '#6A5ACD',
               '#FFEBCD', '#FFDEAD', '#DEB887', '#BC8F8F', '#F4A460', '#B8860B', '#CD853F', '#D2691E', '#8B4513', '#A0522D',
               '#F5F5DC', '#FAEBD7', '#FFE4E1', '#F0FFF0', '#2F4F4F', '#708090', '#696969', '#A9A9A9', '#00FA9A', '#556B2F',
               '#E0FFFF', '#AFEEEE', '#4682B4', '#5F9EA0', '#7FFFD4', '#FF1493', '#483D8B', '#8B0000', '#FFF0F5', '#FAF0E6',
               '#FDF5E6', '#FFF5EE', '#F0FFFF', '#F5FFFA', '#FFFFF0', '#FFFAF0', '#D3D3D3', '#778899', '#FFE4C4', '#F5DEB3',
               '#D2B48C', '#191970', '#0000CD', '#00BFFF', '#B0E0E6', '#ADD8E6', '#40E0D0', '#48D1CC', '#00CED1', '#90EE90']


nums1_empty = []
colours_empty = []
x = 0


for i in range(len(list_1raz_table_new)):
    if list_1raz_table_new[i] not in nums1_empty:

        nums1_empty.append(list_1raz_table_new[i])
        colours_empty.append(list_colour[x])
        x += 1


i = 0

for col in range(15):
    for row in range(12):
        data = tk.Label(frame_vizual, text=list_1raz_table_new[i], width=2, bg=colours_empty[nums1_empty.index(list_1raz_table_new[i])])

        data.grid(column=col, row=row)
        i += 1



for i in range(len(list_rnd_1raz)):
    if list_rnd_1raz[i] not in nums1_empty:

        nums1_empty.append(list_rnd_1raz[i])
        colours_empty.append(list_colour[x])
        x += 1


i = 0

for col in range(15):
    for row in range(12):
        data = tk.Label(frame_vizual2, text=list_rnd_1raz[i], width=2, bg=colours_empty[nums1_empty.index(list_rnd_1raz[i])])

        data.grid(column=col, row=row)
        i += 1


nums1_empty2 = []
colours_empty2 = []

for i in range(len(list_2sep)):
    if list_2sep[i] not in nums1_empty2:

        nums1_empty2.append(list_2sep[i])
        colours_empty2.append(list_colour[x])
        x += 1


i = 0

for col in range(15):
    for row in range(12):
        data = tk.Label(frame_vizual3, text=list_2sep[i], width=2, bg=colours_empty2[nums1_empty2.index(list_2sep[i])])

        data.grid(column=col, row=row)
        i += 1




for i in range(len(list_rnd_2raz)):
    if list_rnd_2raz[i] not in nums1_empty2:

        nums1_empty2.append(list_rnd_2raz[i])
        colours_empty2.append(list_colour[x])
        x += 1


i = 0

for col in range(15):
    for row in range(12):
        data = tk.Label(frame_vizual4, text=list_rnd_2raz[i], width=2, bg=colours_empty2[nums1_empty2.index(list_rnd_2raz[i])])

        data.grid(column=col, row=row)
        i += 1







window.mainloop()