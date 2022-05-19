def generate_headfoot(name):
  with open(name) as fp:
    for line in fp:
       print(line.strip("\n"))
  return
  


def generate_html(entries, years_covered):
  generate_headfoot("publications.head")

  for yr in years_covered:  
    print("     <h3>"+yr+"</h3>\n")     

    for entry in entries[yr]:
     
      print("     <div class=\"publications-item\">\n" +
            "       <h4>" + entry["title"] + "</h4>\n" +
            "       <p>" + entry["authors"] + "</p>\n" + 
            "       <p>" + entry["info"] + "</p>\n" +
            "       <ul class=\"list-inline publication-icons\">\n")
      if(not entry["paper"].startswith("-")):
         print("         <li class=\"list-inline-item\">\n" +
               "         <a href=\""+entry["paper"]+"\">\n" + 
               "         <i class=\"fa fa-file-text-o\" aria-hidden=\"true\"></i>\n" +
               "         </a>\n" + 
               "         </li>\n")
      if(not entry["slides"].startswith("-")):
         print("         <li class=\"list-inline-item\">\n" +
               "         <a href=\""+entry["slides"]+"\">\n" + 
               "         <i class=\"fa fa-television\" aria-hidden=\"true\"></i>\n" +
               "         </a>\n" + 
               "         </li>\n")
      if(not entry["video"].startswith("-")):
         print("         <li class=\"list-inline-item\">\n" +
               "         <a href=\""+entry["video"]+"\">\n" + 
               "         <i class=\"fa fa-file-video-o\" aria-hidden=\"true\"></i>\n" +
               "         </a>\n" + 
               "         </li>\n")

      print("       </ul>\n" + 
            "     </div>\n\n")
  generate_headfoot("publications.foot")
  return 

def main():
  # all entries are 8 lines 
  # year 
  # title
  # authors
  # conf info 
  # paper
  # slides 
  # video 
  # blank line 

  with open('papers.txt') as fp:
    lines = fp.readlines()
    lines = [x.strip('\n') for x in lines] 

  allentries = {}
  years_covered = ["2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2004", "2003", "2002", "2001", "2000"]
  for yr in years_covered:
     allentries[yr] = []
     
  for i in range(0, len(lines), 8):
    # print(i)  
    year = lines[i].rstrip()
    entry = {}
    entry["title"] = lines[i+1].rstrip()
    entry["authors"] = lines[i+2].rstrip()
    entry["info"] = lines[i+3].rstrip()
    entry["paper"] = lines[i+4].rstrip()
    entry["slides"] = lines[i+5].rstrip()
    entry["video"] = lines[i+6].rstrip()
    # blank line
    allentries[year].append(entry)
    
  generate_html(allentries, years_covered)
      

      
      
if __name__ == "__main__":
    main()