#!/usr/bin/env python
# coding: utf-8


# # Data Annotator
# Importing

import argparse
import pandas as pd
import numpy as np



def annotate_data(df, src_lng, tgt_lng):
    df['correctness'] = pd.Series(dtype='str')

    for i, row in df.iterrows():
            src_word = row[src_lng]
            print(src_word)
            trg_word = row[tgt_lng]
            print(trg_word)

            correct = input("correct: ")
            df.at[i, 'correctness'] = correct

    return df


def computing_precision(df):
    yes = df[df['correctness'] == "yes"]
    precision = len(yes)/len(df)
    print("Precision is: ", precision)


def main(src_lng, tgt_lng, df_path, output):
    print("Loading the dataframe.")
    df = pd.read_csv(df_path)
    print("Annotating data...")
    df = annotate_data(df, src_lng, tgt_lng)
    print("Computing results...")
    computing_precision(df)
    print("Saving the dataframe.")
    df.to_csv(output, index=False)
    ("Done.")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluating aligned word embeddings")
    parser.add_argument("--src_lng", type=str, help="Code of the source language")
    parser.add_argument("--tgt_lng", type=str, help="Code of the target language")
    parser.add_argument("--df_path", type=str, help="Path to the dataframe")
    parser.add_argument("--output", type=str, help="Path to save annotated dataframe")

    args = parser.parse_args()

    main(args.src_lng, args.tgt_lng, args.df_path, args.output)

