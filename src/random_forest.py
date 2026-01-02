from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import cross_val_score


def random_forest_classifier(target, data, n_estimators, max_depth):
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    return cross_val_score(model, data, target, cv=5, scoring="f1")

def random_forest_regressor(target, data, n_estimators, max_depth):
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
    return cross_val_score(model, data, target, cv=5)

