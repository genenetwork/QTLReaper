from setuptools import setup, Extension

module1 = Extension('reaper',
                    include_dirs = ["Include"],
                    sources = ["Src/blas_lite.c", "Src/chromosome.c",
                               "Src/dataset.c", "Src/dlapack_lite.c", "Src/f2c_lite.c",
                               "Src/geneutil.c", "Src/locus.c", "Src/normprob.c",
                               "Src/qtlobject.c", "Src/regression.c"],
                    extra_compile_args=["-Wfatal-errors", "-Werror=implicit-function-declaration"]
                    # extra_compile_args=["-Wfatal-errors", "-Werror"]
)

setup(name='qtlreaper-gn2',
      version='1.1',
      author = "The GeneNetwork Team",
      author_email='pjotr.guix@thebird.nl',
      url = "https://github.com/genenetwork/",
      description = 'Scan expression data for QTLs.',
      ext_modules = [module1]
)
