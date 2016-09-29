import reaper
geno = reaper.Dataset()
geno.read("test/data/input/AXB.geno")
print geno.type
print list(geno.prgy)
