# Addition of Addition
Score = int(input("Enter the digit: "))
score_h = 1
times = int(input("How many time? "))
for i in range(times):
    Score *= 2
    score_h = Score / 2
    print("{} + {} =".format(score_h, score_h), Score)
