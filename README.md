# CEEMDAN_LSTM
## Complete Ensemble Empirical Mode Decomposition with Adaptive Noise
An advancement on the EEMD method, Complete Ensemble Empirical Mode Decomposition with Adaptive Noise (CEEMDAN) allows for a granular spectral separation of the Intrinsic Mode Functions and a more precise reconstruction of the original signal (IMFs). I utilize CEEMDAN and LSTM to forecast Ethereum prices multiple steps ahead.

### Novelty and main contribution :
The novelty in this particular scenario is that the residue has been iteratively deconstructed using CEEMDAN until there is no pattern remaining in the residue. The residue is typically ignored by authors in scientific publications, losing valuable data. In order to get rid of the residue, I had to split it down into smaller parts.
This is a novel concept, and it is the responsibility of future researchers to incorporate it into their own work. Please provide a citation to this repository in your work.

### Example:
Figures 1 and 2 illustrate the decomposition of Ethereum time series. The residue depicted in figure 1 has been decomposed on multiple levels, however but I am only including the first decomposition of the residue. Using the preceding iterative process, the residue can be reduced down to the point where no pattern remains.
#### Figure 1
![CEEMDAN](https://github.com/bhaskatripathi/CEEMDAN_LSTM/blob/main/2.jpg)

#### Figure 2
![CEEMDAN](https://github.com/bhaskatripathi/CEEMDAN_LSTM/blob/main/1.jpg)
