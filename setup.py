from setuptools import setup, Extension

module1 = Extension('reaper',
                    include_dirs = ["Include"],
                    sources = ["Src/dataset.c",
                               "Src/chromosome.c",
                               "Src/geneutil.c",
                               "Src/locus.c",
                               "Src/normprob.c",
                               "Src/qtlobject.c",
                               "Src/regression.c",
                               "Src/f2c_lite.c",
                               "Src/blas_lite.c",
                               "Src/dlapack_lite.c",
                    ],
                    # extra_compile_args=["-Wfatal-errors", "-Werror"]
                    extra_compile_args=["-g", "-O0", "-Wfatal-errors", "-Werror=implicit-function-declaration"],
                    undef_macros=['NDEBUG'], # enable assertions!
)

setup(name='qtlreaper-gn2',
      version='1.1',
      author = "The GeneNetwork Team",
      author_email='pjotr.guix@thebird.nl',
      url = "https://github.com/genenetwork/",
      description = 'Scan expression data for QTLs.',
      ext_modules = [module1]
)
