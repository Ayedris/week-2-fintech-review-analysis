import pandas as pd

def load_reviews():
    path = "data/enriched/"
    boa_df = pd.read_csv(f"{path}enriched_processed_BOA_reviews_20250607_144730_20250607_164611.csv")
    cbe_df = pd.read_csv(f"{path}enriched_processed_CBE_reviews_20250607_144621_20250607_164611.csv")
    dashen_df = pd.read_csv(f"{path}enriched_processed_Dashen_reviews_20250607_145221_20250607_164611.csv")
    return boa_df, cbe_df, dashen_df
