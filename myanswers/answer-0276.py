import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from itertools import combinations


def lsh_candidatos_df(matriz_firmas_np, num_bandas):
    n_hashes, n_docs = matriz_firmas_np.shape
    filas_por_banda = n_hashes // num_bandas

    candidatos = set()

    for b in range(num_bandas):
        banda = matriz_firmas_np[b * filas_por_banda:(b + 1) * filas_por_banda, :]
        strings_banda = ["-".join(map(str, banda[:, d])) for d in range(n_docs)]

        le = LabelEncoder()
        buckets = le.fit_transform(strings_banda)

        for bucket_id in np.unique(buckets):
            docs_in_bucket = np.where(buckets == bucket_id)[0]
            if len(docs_in_bucket) > 1:
                for par in combinations(sorted(docs_in_bucket), 2):
                    candidatos.add(par)

    df_out = (
        pd.DataFrame(list(candidatos), columns=["doc_A", "doc_B"])
        .sort_values(by=["doc_A", "doc_B"])
        .reset_index(drop=True)
    )

    return df_out
