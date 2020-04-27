# fastSulf-DNN
## Using deep neural networks and biological sub-words to detect protein S-sulfenylation sites

Protein S-sulfenylation is one kind of crucial post-translational modifications (PTMs) in which the hydroxyl group covalently binds to the thiol of cysteine. Some recent studies have shown that this modification plays an important role in signaling transduction, transcriptional regulation, and apoptosis. To date, the dynamic of sulfenic acids in proteins remains unclear because of its fleeting nature. Identifying S-sulfenylation sites, therefore, could be the key to decipher its mysterious structures and functions which are important in cell biology and diseases. However, due to the lack of effective methods, scientists in this field tend to be limited in merely a handful of some wet-lab techniques that are time-consuming and not cost-effective. Thus, this motivated us to develop an In Silico model for detecting S-sulfenylation sites from protein sequence information only. In this study, protein sequences served as natural language sentences comprising biological sub-words. The deep neural network was consequentially employed to perform classification. The performance statistics within the independent dataset including sensitivity, specificity, accuracy, MCC, as well as AUC rates achieved 85.71%, 69.47%. 77.09%, 0.5554, and 0.833, respectively. Our results suggested that the proposed method (fastSulf-DNN) achieved excellent performance in predicting S-sulfenylation sites compared to other well-known tools on a benchmark dataset.

### Dependencies
- Python 3
- fastText: https://github.com/facebookresearch/fastText
- Keras 2: https://keras.io/#installation

### Prediction step-by-step:
### Step 1
Use "fasttext_generated.py" file to transform FASTA sequence into FastText format
- *python fasttext_generated.py fasta_file fasttext_file*

### Step 2
Print vectors using FastText model:
- *fasttext print-sentence-vectors model.bin < fasttext_file > vector_file*

### Step 3
Use "fastSulf_DNN.py" to evaluate the generated file:
- *python fastSulf_DNN.py vector_file*

### Step 4
Read the prediction results:
- "1": S-sulfenylation site
- "0": non S-sulfenylation site
