from __future__ import annotations
import numpy as np
from sklearn.metrics import pairwise_distances

class KMedoids:
    """
    Implementação simples do K-Medóides (PAM-like).

    Parâmetros
    ----------
    n_clusters : int
        Número de clusters.
    max_iter : int
        Número máximo de iterações.
    metric : str
        Métrica de distância para pairwise_distances (ex.: 'euclidean', 'manhattan').
    random_state : int | None
        Semente aleatória.

    Atributos (após fit)
    --------------------
    medoid_indices_ : np.ndarray de shape (k,)
        Índices das amostras escolhidas como medóides.
    labels_ : np.ndarray de shape (n_samples,)
        Atribuição de cluster por amostra.
    inertia_ : float
        Soma das distâncias amostra→medóide (objetivo minimizado).
    """

    def __init__(self, n_clusters=3, max_iter=300, metric='euclidean', random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.metric = metric
        self.random_state = random_state

    def fit(self, X: np.ndarray):
        rng = np.random.default_rng(self.random_state)
        n = X.shape[0]
        # inicializa medóides com amostras distintas aleatórias
        medoid_indices = rng.choice(n, size=self.n_clusters, replace=False)
        D = pairwise_distances(X, X, metric=self.metric)

        for _ in range(self.max_iter):
            labels = np.argmin(D[:, medoid_indices], axis=1)
            current_cost = np.sum(D[np.arange(n), medoid_indices[labels]])
            improved = False

            # tenta trocar cada medóide por um não-medóide
            for i in range(self.n_clusters):
                for candidate in range(n):
                    if candidate in medoid_indices:
                        continue
                    trial_medoids = medoid_indices.copy()
                    trial_medoids[i] = candidate
                    trial_cost = np.sum(np.min(D[:, trial_medoids], axis=1))
                    if trial_cost + 1e-9 < current_cost:
                        medoid_indices = trial_medoids
                        current_cost = trial_cost
                        improved = True
            if not improved:
                break

        self.medoid_indices_ = medoid_indices
        self.labels_ = np.argmin(D[:, medoid_indices], axis=1)
        self.inertia_ = np.sum(np.min(D[:, medoid_indices], axis=1))
        return self

    def predict(self, X_new: np.ndarray, X_train: np.ndarray):
        """Prediz rótulos de X_new usando os medóides obtidos do fit em X_train."""
        from sklearn.metrics import pairwise_distances
        medoids = X_train[self.medoid_indices_]
        D = pairwise_distances(X_new, medoids, metric=self.metric)
        return np.argmin(D, axis=1)
