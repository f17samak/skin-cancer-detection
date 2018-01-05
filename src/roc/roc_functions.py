from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def plotROC(pred_labels, test_labels):
    """
    Plots roc curve
    :param pred_labels: List of predicted labels
    :param test_labels: List of true labels
    :return: ROC graph
    """
    false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, pred_labels)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    plt.title('Receiver Operating Characteristic')
    plt.plot(false_positive_rate, true_positive_rate, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.2])
    plt.ylim([-0.1, 1.2])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    print("ROC-Curve plotted")
    plt.show()


def getANNResults(pred_labels):
    """
    Get number of maligne and benigne predicted labels
    :param labels: Labels
    :return: maligne, benigne : Number of maligne and benigne prediction
    """
    maligne = 0
    benigne = 0
    for label in pred_labels:
        if label == 1:
            maligne+=1
        else:
            benigne+=1
    return maligne, benigne

# Ermittelt AUC der Vorhersage
# In: Vorhergesagte Labels, Testlabels
# Out: AUC der Vorhersage
def getAUC(pred_labels, test_labels):
    """
    Compute AUC of prediction
    :param pred_labels:
    :param test_labels:
    :return: roc_auc - AUC of prediction
    """
    false_positive_rate, true_positive_rate, thresholds = roc_curve(test_labels, pred_labels)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    return roc_auc


test = [1,0,0,1,0,1,0,1]
pred = [1,1,0,1,0,1,0,1]

print("ANN predicted %s maligne and %s benigne. AUC = %s" % (getANNResults(pred)[0], getANNResults(pred)[1], getAUC(pred, test)))
plotROC(pred, test)