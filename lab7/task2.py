
diag1 = {"заміна мастила", "заміна фільтрів", "діагностика ходової", "розвал-сходження"}
diag2 = {"діагностика ходової", "заміна гальмівних колодок", "промивка інжектора", "заміна мастила"}

print("Роботи першої діагностики:", diag1)
print("Роботи другої діагностики:", diag2)

common_jobs = diag1.intersection(diag2)
print("Спільні роботи:", common_jobs)

only_first = diag1.difference(diag2)
print("Роботи лише першої діагностики:", only_first)

all_jobs = diag1.union(diag2)
print("Повний набір робіт:", all_jobs)
