# D2Rec
Code for **Causal Disentanglement with Network Information for Debiased Recommendations**
Recommender systems suffer from biases that may misguide the system when learning user preferences. Under the causal lens, the user’s exposure to items can be seen as the treatment assignment, the ratings of the items are the observed outcome, and the different biases act as confounding factors. Therefore, to infer debiased preferences and to capture the causal relationship between exposure and the observed ratings, it is essential to account for any hidden confounders. To this end, we propose a novel causal disentanglement framework that decomposes latent representations into three independent factors, responsible for (a) modeling the exposure of an item, (b) predicting ratings, and (c) controlling for hidden confounders. Experiments on real-world datasets validate the effectiveness of the proposed \textit{Causal Disentanglement for DeBiased Recommendations} (D2Rec) model in debiasing recommendations.
 



# Setup
This repository consists of multiple folders.

Ciao data - consists of all data required for Ciao dataset\
Epinions_data - consists of all data required for Epinions dataset\
utils - consists of two python files\
•	node2vec.py --- for generating the Node2vec embeddings for user and item for D2Rec model.\
•	testgenerator.py --- that generates the pseudo-unbiased test sets.\
Baselines – consists of all the baselines as mentioned in the paper\
CIRS folder - consists of two files.\n
	* cirs_baseline.py --- contains the code for the Causal Inference For Recommender System baseline.
	*poisson_factorization.py --- contains the code for creating the user and item latent variables which will be used in cirs_baseline.py.
Graphrec folder - consists of two files.
	* graphrec.py --- contains the code for the GraphRec baseline.
	* pickle generator.py--- contains the code for creating the pickle dataset that is required for creating the pickle file which is needed to run graphrec.py.
ips_mf.py --- contains the code to run Inverse Propensity Score Matrix Factorization baseline.
ncf.py --- contains the code to run Neural Collaborative Filtering baseline.
pmf_baseline.py --- contains the code to run Probablistic Matrix Factorization baseline.
socialmf.py --- contains the code to run Social Matrix Factorization baseline.



All the code was written in google colab. To run the code, change the data path given in the python files to appropriate data paths and run it. We have also provided a csv file named results.csv that contains all the results displayed in the paper.

