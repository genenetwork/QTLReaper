#!/usr/bin/python
import sys
import os
import string
import reaper

##Read from genotype file
def read(file_geno, file_pheno, file_result1, file_result2):
	genotype = reaper.Dataset()
	genotype.read(file_geno)

	##open output file
	outputFile = file_result1
	fout = open(outputFile, "wb")
	fout.write("ID\tLocus\tChr\tcM\tLRS\tAdditive\tpValue\n")
	outputFile2 = file_result2
	fout2 = open(outputFile2, "wb")
	fout2.write("ID\tLocus\tChr\tcM\tLRS\tAdditive\tpValue\n")

	##Open Trait File
	DataStart = 1
	fp = open(file_pheno, "rb")
	header = fp.readline()
	header = map(string.strip, header.strip().split("\t"))
	_strains = header[DataStart:]

	##Read input file line by line
	line = fp.readline()
	while line:
		line = map(string.strip, line.strip().split("\t"))
		traitName = line[0]
		print "Calculate Trait %s" % traitName
		_traitData = map(float, line[DataStart:])

		qtlresults = genotype.regression(strains = _strains, trait = _traitData)
		permu = genotype.permutation(strains = _strains, trait = _traitData)

		##Save all the results
		for qtl in qtlresults:
			pvalue = reaper.pvalue(qtl.lrs, permu)
			fout.write("%s\t%s\t%s\t%2.3f\t%2.3f\t%2.3f\t%2.3f\t\n" % (traitName,
				qtl.locus.name, qtl.locus.chr, qtl.locus.cM, qtl.lrs, qtl.additive, pvalue))
		##Save highest LRS only
		maxqtl = max(qtlresults)
		pvalue = reaper.pvalue(maxqtl.lrs, permu)
		fout2.write("%s\t%s\t%s\t%2.3f\t%2.3f\t%2.3f\t%2.3f\t\n" % (traitName,
				maxqtl.locus.name, maxqtl.locus.chr, maxqtl.locus.cM, maxqtl.lrs, maxqtl.additive, pvalue))

		line = fp.readline()

	fp.close()
	fout.close()
	fout2.close()

if __name__ == "__main__":
        print "Usage: file_geno, file_pheno, file_result1, file_result2\n"
	print("command line arguments:\n\t%s" % sys.argv)
	read(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	print("exit successfully")
