def report():

    amt_of_scores = int(raw_input("How many scores are there?"))

    top_average = 0
    bottom_average = amt_of_scores

    for i  in range (0, amt_of_scores):
        score_i = int(raw_input("Score = "))

        top_average = score_i + top_average

    average = top_average / bottom_average

    #Report

    print ("--------- Report ---------")
    print ("    Amount of scores: " + str(amt_of_scores))
    print ("    Average:  " + str(average))

report()
