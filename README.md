# fastSulf-DNN
## Using deep neural networks and biological sub-words to detect protein S-sulfenylation sites

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
