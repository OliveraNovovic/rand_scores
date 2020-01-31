# rand_scores

Calculating random scores (adjusted random index) for clustering results. ARI is calculated between different versions 
of clustering for the same day (clustering is done over same graph multiple times to evaluate the stability of 
Louvain algorithm), between sequential days, and for the same day (november 08) between the results obtained when different 
filtering level is applied (no filter as ground truth, filtering with alpha 0.05, 0.01, 0.001).
