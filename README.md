# RGS
## Introduction
The Random Grid Search (RGS) algorithm is a simple, but surprisingly effective, way to find rectangular cuts. Developed by Harrison Prosper, Chip Stewart, Pushpa Bhat and generalized by Sezen Sekmen to include *two-sided* and *staircase* cuts. A two-sided cut is a cut of the for (x1 < x < x2), while a staircase cut is the OR of two or more one-sided cuts.

## Installation
This package depends on the package [Root](https://root.cern.ch/downloading-root) from CERN and a small package [histutil](https://github.com/hbprosper/histutil) built on top of Root. To install Root follow the instructions at the [Root](https://root.cern.ch/downloading-root) website. The histutil package may be installed in any convenient place using 
```
git clone https://github.com/hbprosper/histutil.git
cd histutil
source setup.sh
cd -
```
Using setup.csh if you are using a non-bash shell. Then do
```
git clone https://github.com/hbprosper/RGS.git
cd RGS
make
source setup.sh
```
Both setups need be done only once per terminal session.

## Examples
There are two examples in the *examples* directory of RGS
### Higgs
This example illustrates three RGS optimizations, HO1, HO2, and HO3, designed isolate Higgs vector boson fusion events. Each optimization can be run by executing the _train.py_ and _analysis.py_ programs. For example,
HO1 can be run as follows
```
cd examples/Higgs/HO1
./train.py
```
which will run RGS and store the results in a file called *HO1.root*. To analyze the results of RGS do
```
./analysis.py
```
which will read the results from *HO1.root*. 

### SUSY
This example illustrates three optimizations, SO1, SO2, SO3, based on a search for the best staircase cut, to search for SUSY events. Switch to the *SUSY* directory and proceed as in the Higgs example. 
