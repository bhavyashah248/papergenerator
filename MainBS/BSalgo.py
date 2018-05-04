import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","BSProject.settings")
django.setup()
from MainBS.models import Question

# sub = Subject.objects.all()
# for each in sub:
#     print(each.value)

def algo (marks = None,typePattern = None, chapPattern = None, sub = None, tchapters = None):
    if not typePattern == None and not chapPattern == None and not marks == None and not sub == None and not tchapters == None:
        Result = []
        for eachtype in typePattern:
            type = eachtype[0]
            noOfQue = int(eachtype[1])
            weightage = int(eachtype[2])
            nTypeQue = Question.objects.filter(subject=sub, type=type)
            m = max(chapPattern)
            max_index = [i for i, j in enumerate(chapPattern) if j == m]
            noOfChap = len(chapPattern)

        #     under construction
            while noOfQue > 0:
                for index in max_index:
                    chap = tchapters[index]
                    candidates = []
                    for each in nTypeQue:
                        # print("each3  ", each[3], " chap ", chap)
                        # print(each.chapter.name + '$$$$$$$' + chap.name)
                        if each.chapter.name == chap.name:
                            candidates.append(each)
                    winnerWinnerChickenDinner = Question(subject=sub, chapter=chap, type=type, question="winnerWinnerChickenDinner?", prob='0', answer="Better Luck Next Time! #100/100")
                    # print("can $$$$ ",candidates)
                    for eachCan in candidates:
                        if int(eachCan.prob) > int(winnerWinnerChickenDinner.prob):
                            winnerWinnerChickenDinner = eachCan
                        # print(eachCan.prob + " $$$ " + winnerWinnerChickenDinner.prob)
                    # print("Winner ==>",winnerWinnerChickenDinner)
                    # if int(winnerWinnerChickenDinner.prob) != 0:
                    Result.append(winnerWinnerChickenDinner)
                    print("original ==>" + str(winnerWinnerChickenDinner.id))
                    # reduce(id=winnerWinnerChickenDinner.id)
                    chapPattern[index] -= weightage
                    noOfQue -= 1
                    if noOfQue == 0:
                        break
                m = max(chapPattern)
                max_index = [i for i, j in enumerate(chapPattern) if j == m]

        # end of construction
        return Result
    else:
        return "You left a field empty"

def increase(id,prob=30):
    que = Question.objects.get(id=id)
    que.prob = str(int(que.prob) + prob)
    que.save()


def reduce(id,prob=10):
    que = Question.objects.get(id=id)
    que.prob = str(int(que.prob) - prob)
    print("new ==>" + str(que.prob))

    que.save()
