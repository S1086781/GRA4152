import argparse
#creating argparse argument parser
parser=argparse.ArgumentParser(description="The function does logistic regression. The function takes 4 inputs: penalty, bias or intercept, maximum iterations and tolerance. Penalty must be chosen from a list. The fit_intercept is a boolean variable. The max_iter is an integer while tol is a float. ", epilog="The website of the original function is: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html")

#specifying arguments
parser.add_argument('--penalty', default='l2', choices=['l2','l1', 'elasticnet', 'None'], help="Specify the norm of the penalty.")
parser.add_argument('--fit_intercept', action='store_true', help="Specify if a constant (a.k.a. bias or intercept) should be added to the decision function.")
parser.add_argument('--max_iter', default=100,type=int, help="Maximum number of iterations taken for the solvers to converge.")
parser.add_argument('--tol', default=1e-4, type=float, help="Tolerance for stopping criteria.")
args=parser.parse_args()




def my_logistic_regression(penalty , fit_intercept , max_iter , tol):
    
    from sklearn.linear_model import LogisticRegression
    # define a logistic regression object with your input params
    clf = LogisticRegression(penalty=penalty , fit_intercept= fit_intercept , max_iter=max_iter , tol=tol)
    return clf

clf=my_logistic_regression(args.penalty, args.fit_intercept, args.max_iter, args.tol)

#print the arguments
print(args)

#print the original function output
print(clf)