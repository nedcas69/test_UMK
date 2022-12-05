import random


keys = []
i = 0
    # questions = {}
    # answers = {}
while i < 10:
    key = random.randint(1,11)
    # if Question.objects.get(pk=key):
    if key not in keys:
        keys.append(key)
        i += 1
    else:
        continue
        # else:
        #     continue

print(keys)