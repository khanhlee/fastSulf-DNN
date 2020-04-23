# fastSulf-DNN
## Using deep neural networks and biological sub-words to detect protein S-sulfenylation sites

Protein S-sulfenylation is one kind of crucial post-translational modifications (PTMs) in which the hydroxyl group covalently binds to the thiol of cysteine. Some recent studies have shown that this modification plays an important role in signaling transduction, transcriptional regulation, and apoptosis. To date, the dynamic of sulfenic acids in proteins remains unclear because of its fleeting nature. Identifying S-sulfenylation sites, therefore, could be the key to decipher its mysterious structures and functions which are important in cell biology and diseases. However, due to the lack of effective methods, scientists in this field tend to be limited in merely a handful of some wet-lab techniques that are time-consuming and not cost-effective. Thus, this motivated us to develop an In Silico model for detecting S-sulfenylation sites from protein sequence information only. In this study, protein sequences served as natural language sentences comprising biological sub-words. The deep neural network was consequentially employed to perform classification. The performance statistics within the independent dataset including sensitivity, specificity, accuracy, MCC, as well as AUC rates achieved 85.71%, 69.47%. 77.09%, 0.5554, and 0.833, respectively. Our results suggested that the proposed method (fastSulf-DNN) achieved excellent performance in predicting S-sulfenylation sites compared to other well-known tools on a benchmark dataset.

### Step 1
Install FastText package via the instructions here: https://github.com/facebookresearch/fastText
Install Keras package via the instructions here: https://keras.io/#installation

### Step 2
Use "fasttext_generated.py" file to transform FASTA sequence into FastText format
- *python fasttext_generated.py fasta_file fasttext_file*

### Step 3
Print vectors using FastText model:
- *fasttext print-sentence-vectors model.bin < fasttext_file > vector_file*

### Step 4
Use "fastSulf_DNN.py" to evaluate the generated file:
- *python fastSulf_DNN.py vector_file*
