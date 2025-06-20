
db = { 
  "ATGT": "geneA",  # 3/4 = 75%
  "ATGC": "geneB",  # 4/4 = 100%
  "TTAC": "geneC",  # 1/4 = 25%
  "ATGG": "geneD",  # 3/4 = 75%
  "ATCC": "geneE",  # 3/4 = 75%
  "AGGC": "geneF",  # 2/4 = 50%
  "GTGC": "geneG",  # 3/4 = 75%
  "TTGC": "geneH",  # 3/4 = 75%
  "GGGG": "geneI",  # 0/4 = 0%
  "ATGA": "geneJ"   # 3/4 = 75%
}
def generate_report(seq,db):
    count_g=0
    count_c=0
    if seq in db:
        id=db[seq]
    for i in seq:
        count_c=seq.count(i)
        count_g=seq.count(i)
gc_count=(count_g+count_c+)/len(seq)*100
if(gc_count>=80):
    status="good match"
elif(gc_count>=50 and gc_count<80):
