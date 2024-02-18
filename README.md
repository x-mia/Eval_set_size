# Eval_set_size

## Evaluation datasets of various sizes and script for evaluating cross-lingual embedding models on the bilingual lexicon induction task

This repository contains datasets of various sizes (3K, 1.5K, 500, and 200 source words) to evaluate cross-lingual embedding models on three language pairs: Estonian-Slovak, Czech-Slovak, and English-Korean on the bilingual lexicon induction task. Each dataset involves folder "500", where is the 3K source-word-dataset split randomly into 6 datasets containing 500 source words. 

### Requirements
* [NumPy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Tqdm](https://tqdm.github.io/)

### Evaluate aligned embeddings
To evaluate aligned embeddings, simply run:
```bash
python eval.py --src_lng SRC_LNG --tgt_lng TGT_LNG --src_path SRC_PATH --tgt_path TGT_PATH --eval_df EVAL_DF --k_num K_NUM --nmax NMAX --output OUTPUT
```
Example:
```bash
python eval.py --src_lng et --tgt_lng sk --src_path vectors-et.txt --tgt_path vectors-sk.txt --eval_df et-sk.200.csv --k_num 1 --nmax 50000 --output df.csv
```

### Annotating the data
To manually annotate the data, simply run:
```bash
python annotate_data.py --src_lng SRC_LNG --tgt_lng TGT_LNG --df_path DF_PATH --output OUTPUT
```
Example:
```bash
python annotate_data.py --src_lng et --tgt_lng sk --df_path et-sk.csv --output annotated_df.csv
```

### References
* Please cite [[1]](https://nlp.fi.muni.cz/raslan/2023/paper3.pdf) if you found the resources in this repository useful.

[1] Denisová, M. and Rychlý, P. (2023). [Does Size Matter?: Comparing Evaluation Dataset Size for the Bilingual Lexicon Induction.](https://nlp.fi.muni.cz/raslan/2023/paper3.pdf) In *Proceedings of the Seventeenth Workshop on Recent Advances in Slavonic Natural Languages Processing, RASLAN 2023*, pp. 47-56. Tribun EU. 

```
@inproceedings{denisova_rychly2023,
   author = {Denisová, Michaela},
   title = {Does Size Matter?: Comparing Evaluation Dataset Size for the Bilingual Lexicon Induction},
   booktitle = {Proceedings of the Seventeenth Workshop on Recent Advances in Slavonic Natural Languages Processing, RASLAN 2023},
   pages = {47--56},
   publisher = {Tribun EU},
   url = {https://nlp.fi.muni.cz/raslan/2023/paper3.pdf},
   year = {2023}
}
```

### Related work
* [A. Conneau, G. Lample, L. Denoyer, MA. Ranzato, H. Jégou - *Word Translation Without Parallel Data*, 2017](https://arxiv.org/pdf/1710.04087.pdf)
