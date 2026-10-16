import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    merged=anon_df.merge(aux_df, on=["age","zip3","gender"])
    #links the two tables on the age zip 3 and gender
    unique= merged.drop_duplicates(subset=["anon_id"],keep=False)
    #gets rid of all the dupliacate ids
    unique=unique.rename(columns={"name": "matched_name"})
    unique=unique[["anon_id", "matched_name"]]
    return unique

    raise NotImplementedError


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    matched_length=len(matches_df)
    anon_df_length=len(anon_df)

    deanonymizationr=matched_length/anon_df_length

    return deanonymizationr

    raise NotImplementedError
