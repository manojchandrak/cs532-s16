import feedfilter

def main():
  cl=docclass.fisherclassifier(docclass.getwords)
  cl.setdb('allsports.db')
  read('allsports.xml',cl)
  
if __name__ == "__main__":
  main()