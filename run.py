import naive_bayes


if __name__ == '__main__':
    nb = naive_bayes.NaiveBayes('naive_bayes_data.txt')
    nb.train()
    nb.test()

    tp = len(nb.tp)
    tn = len(nb.tn)
    fp = len(nb.fp)
    fn = len(nb.fn)

    accuracy = (tp+tn)/(tp+fp+fn+tn)
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = 2*recall*precision/(recall+precision)

    print("Accuracy: {} %".format(accuracy*100))
    print("Precision: {}".format(precision))
    print("Recall: {}".format(recall))
    print("F1 Measure: {}".format(f1))
