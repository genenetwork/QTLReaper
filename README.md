# QTLReaper

QTL Reaper is software, written in C and compiled as a Python module, for rapidly scanning microarray expression data for QTLs. It is essentially the batch-oriented version of WebQTL. It requires, as input, expression data from members of a set of recombinant inbred lines and genotype information for the same lines. It searches for an association between each expression trait and all genotypes and evaluates that association by a permutation test. For the permutation test, it performs only as many permutations as are necessary to define the empirical P-value to a reasonable precision. It also performs bootstrap resampling to estimate the confidence region for the location of a putative QTL.

## Install and run

To compile qtlreaper module, execute:

	python setup.py build

To install qtlreaper module, execute:

	python setup.py install

For a local test

    python setup.py test

which does

```python
import reaper
geno = reaper.Dataset()
geno.read("test/data/input/AXB.geno")
print geno.type
  riset
print list(geno.prgy)
  ['AXB1', 'AXB2', 'AXB3', 'AXB4', 'AXB5', 'AXB6', 'AXB7', 'AXB8', 'AXB9', 'AXB10', 'AXB11', 'AXB12', 'AXB13', 'AXB14', 'AXB15', 'AXB17', 'AXB19', 'AXB21', 'AXB23', 'AXB2']
```

Examples are

    env PYTHONPATH=./build/lib.linux-x86_64-2.7/ python ./test/example1.py
    env PYTHONPATH=./build/lib.linux-x86_64-2.7/ python ./test/example2.py test/data/input/BXD.txt test/data/input/trait.txt output.txt highest.txt

For a local installation

    python setup.py install --prefix=$HOME/tmp

and prepend that to the PYTHONPATH

    env PYTHONPATH=/home/wrk/tmp/lib/python2.7/site-packages:$PYTHONPATH python

### Installing with GNU Guix

QTLreaper has a package definition in https://gitlab.com/genenetwork/guix-bioinformatics and can be
installed with

    env GUIX_PACKAGE_PATH=~/guix-bioinformatics guix package -i python-qtlreaper

after cloning that repository.

Alternatively check out the source tree and use a Guix environment

    guix environment bash -C --pure --ad-hoc gcc python --no-grafts
    python3 setup.py build
    python3 setup.py install --user

## Debug

Build the extension with

    extra_compile_args=["-g", "-O0", "-Wfatal-errors", "-Werror=implicit-function-declaration"]

in setup.by and start gdb with

    gdb --args  python3 test/example1.py

if you have built Python with symbol information add

    env PYTHONMALLOCSTATS=1 gdb --args  python3 test/example1.py
    symbol-file /gnu/store/97zc8nprz8sif91gbcz8jfsqk3mjx9i2-python-debug-3.5.3-debug/lib/debug/gnu/store/hkhfs...-debug-3.5.3/bin/python3.5.debug

## License

The QTLReaper source code is released under the GNU General Public License version 2.0 (GPLv2). See [here](https://www.gnu.org/licenses/gpl-2.0.html).

## Author

Jintao Wang and Ken Manly with compatibility and range checking updates by Pjotr Prins and Lei Yan
