# QTLReaper

QTL Reaper is software, written in C and compiled as a Python module, for rapidly scanning microarray expression data for QTLs. It is essentially the batch-oriented version of WebQTL. It requires, as input, expression data from members of a set of recombinant inbred lines and genotype information for the same lines. It searches for an association between each expression trait and all genotypes and evaluates that association by a permutation test. For the permutation test, it performs only as many permutations as are necessary to define the empirical P-value to a reasonable precision. It also performs bootstrap resampling to estimate the confidence region for the location of a putative QTL.

####Installation

To compile qtlreaper module, execute:

	python setup.py build

To install qtlreaper module, execute:

	python setup.py install

## License

The QTLReaper source code is released under the GNU General Public License version 2.0 (GPLv2). See [here](http://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html).
