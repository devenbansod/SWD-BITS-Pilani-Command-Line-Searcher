# This is a Command Line SWD,BITS PILANI Searcher (Python)

# Make sure you are connected on BITS,Pilani LAN.

# Make Sure you are using LINUX 

# Run the Python FIle from the Terminal as : python swd_query.py

from splinter import Browser 
import os,splinter

def return_results(browser) :
     
     # Find and click the 'Search' button 
     button = browser.find_by_name('searchBtn') 
     button.click()

     #Handle the Output
     results = browser.find_by_id('searchResultGridView')
     
     return results


sname = str(raw_input("Name or Part of Name to search(May Be Empty) : "))
idno = str(raw_input("Id No to Search : (May Be Empty) : "))     

with Browser('firefox') as browser: 
     
     # Visit URL 
     try :
          url = "http://swd/StudentSearch.aspx"
          browser.visit(url) 
     except : 
          url = "http://www.bits-pilani.ac.in:12349/StudentSearch.aspx"
          browser.visit(url)

     browser.fill('idnoTxt',idno)
     browser.fill('nameTxt',sname)

     try :
          results = return_results(browser)
          print results[0].value
     except splinter.exceptions.ElementDoesNotExist :
          try :
               browser.fill('idnoTxt',idno)
               browser.fill('nameTxt',sname.split(" ")[0])
               results = return_results(browser)
               print results[0].value
          except splinter.exceptions.ElementDoesNotExist :           
               try :
                    browser.fill('idnoTxt',idno)
                    browser.fill('nameTxt',sname.split(" ")[1])
                    results = return_results(browser)
                    print results[0].value
               except splinter.exceptions.ElementDoesNotExist :                   
                    print "No Such Search Result Found"

               except :
                    print "ERROR Occured !! \nPlease Try Again !!"

          except :
               print "ERROR Occured !! \nPlease Try Again !!"
     except :
          print "ERROR Occured !! \nPlease Try Again !!"


#The Following Code should be uncommented if you want the Output in a HTML File  
     
     #f=open('query_results.html',"w");
     #f.write("<html><table>"+results.html+"</table></html>")
     #f.close()


#Output the Results
#os.system("firefox query_results.html")
