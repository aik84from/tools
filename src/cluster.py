from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


def cluster(data, eps, min_samples):
    X = StandardScaler().fit_transform(data)
    return DBSCAN(eps=eps, min_samples=min_samples).fit_predict(X)

