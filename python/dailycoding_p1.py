def problem1(liste, k):
    resu = []
    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            if (liste[i] + liste[j]) == k:
                resu.append([liste[i], liste[j]])
    return resu
