def report():

    amt_of_scores = int(raw_input("How many scores are there?"))

    scores = {}
    class_name = raw_input("What is the name of the class?")
    score = int(raw_input("What is the first score?"))
    scores[class_name] = score

    #recording all of the scores
    for i in range(amt_of_scores):
        another = raw_input("Is there another score?")
        if another.lower() == "yes":
            class_name_next = raw_input("What is the name of the class?")
            score_next = float(raw_input("What is the next score?"))
            scores[class_name_next] = score_next

    #calculating the scores into the report
    score = float(score)
    report = sum(scores.values()) / amt_of_scores
    scores_keys = str(scores.keys())
    scores_keys = scores_keys.replace("[", "")
    scores_keys = scores_keys.replace("]", "")
    scores_keys = scores_keys.replace("'", "")
    scores_values = str(scores.values())
    scores_values = scores_values.replace("[", "")
    scores_values = scores_values.replace("]", "")
    print ("--------------Report Card---------------")
    print (scores_keys + "\n" + scores_values)
    print "Average"
    print report

report()
