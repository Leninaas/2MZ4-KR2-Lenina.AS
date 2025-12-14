
import operator

a = {"Декабрь": 37.1, "Январь": 33.7, "Февраль": 26.4, "Март": 40}

print(sorted(a.items(), key = operator.itemgetter(1)))
