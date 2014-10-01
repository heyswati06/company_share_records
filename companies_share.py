import csv  # module used to read the csv file
import itertools # module used for readers
import heapq # module used for reducing the complexity while sorting on the company_share_price
import os # module jused to exit from the program if data in csv file is inappropriate while validating
import doctest
from pprint import pprint

class Stock(object):
    """ Abstract class for building company share price of different companies for specific month and year"""
    def __init__(self, data, index):
        self.year = data[0]
        self.month = data[1]
        self.price = data[index]
        
class CompanyHighestSharePrice(object):
    """
    The methods in this class helps to find list for each Company
    year and month in which the share price was highest.
    """

    def __init__(self):
        self.companies_data = self.read_file()
    
    def read_file(self):
        """Loads a Memory loadable CSV File to the program, which
           contains stock data of multiple companies since 1990.
        """
        datafile = open('companies_data.csv', 'r')
        reader1, reader2 = itertools.tee(csv.reader(datafile))
        
        return reader1, reader2, datafile

    def get_total_rows_and_cols(self):
        """ get total number of rows and cols of CSV file.
        """
        reader1, reader2, datafile = self.companies_data
        
        ## Find number of columns in csv file
        num_cols = len(next(reader1))
        data = list(reader2)
            
        ## Find number of rows in csv file
        num_rows = (sum(1 for row in data)) -1
        
        ## validate data from csv file before computation
        self.validate_data(num_rows, num_cols, data)
        
        return num_rows, num_cols, datafile
    
    def validate_data(self, num_rows, num_cols, data):
        """ validations to check year, month and prices in csv file """
        ## 'quit_value' is a variable to keep a track of the position where data in csv file is unacceptable
        quit_value = 0
        for row_value in range(num_rows):
            ## Check if the values in 'YEAR' column of csv file are not blank. Once all values are filled, the program continues
            if not data[row_value][0]:
                print "Value of YEAR for row "+str(row_value+1)+" is empty. Please enter a value before proceeding"
                quit_value = 1
            ## Check if the values in 'MONTH' column of csv file are not blank. Once all values are filled, the program continues
            if not data[row_value][1]:
                print "Value of MONTH for row "+str(row_value+1)+" is empty. Please enter a value before proceeding"
                quit_value = 1
            ## Check if the company SHARE column values ('share_cols') are not blank and are digits.  Once all values are filled, the program continues 
            for share_cols in range(2,num_cols):
                if not str(data[row_value+1][share_cols]):
                    data[row_value][share_cols]=0
                            
                
                if not str(data[row_value+1][share_cols]).isdigit():
                    print "Value of COMPANY SHARE for row "+str(row_value+2)+" is not a number. Please enter a value before proceeding"
                    quit_value = 1
        ## program quits when 'quit_value' is 1            
        if quit_value == 1 :
            os._exit(0)
            
    
    def get_highest_share_price(self):
        """ return list for each Company, Year and Month in which
            the share price was highest.
        """
        best_company_records = {}
        num_rows, num_cols, datafile = self.get_total_rows_and_cols()
        
        ## company data starts from 'column_index' 2
        company_index = 2
    
        ## Resetting the read position of the file object ('datafile') to it's beginning.
        datafile.seek(0)
    
        ## outer loop to iterate over all the company share prices, column-wise
        while(company_index < num_cols):
             ## 'temp_reader' is used to read rows for EACH company
             temp_reader = csv.reader(datafile)         
             ## 'company_record' is a list object which is getting prices for particular company1, company2...company1 each time
             company_record = [] 
             ## "Stock" OBJECT is created for EACH row of the current 'company_index'
             row_records = [Stock(row,company_index) for row in temp_reader]
             ## loop for EACH row of the STOCK object for current 'company_index' (excluding the first header row)
             for row in row_records[1:]:
                ## 'dict_company_stock' is a dictionary with key values : 'year','month','price'
                dict_company_stock = {}
                dict_company_stock['year'],dict_company_stock['month'],dict_company_stock['price']  = row.year, row.month, int(row.price)
                ## 'company_record' is a list of 'dict_company_stock' for particular company
                company_record.append(dict_company_stock)  
                ## 'highest_share' is used to calculate highest share 'price' using HEAPQ for each company with its respective 'year' and 'month'
             highest_share = heapq.nlargest(1, company_record, key=lambda s: s['price'])[0]
                         
             company_name = 'Company_'+ str(company_index-2)
       
             best_company_records[company_name] = {}
             best_company_records[company_name] = highest_share
             ## Resetting the read position of the file object ('datafile') to it's beginning.
             datafile.seek(0)
             company_index=company_index+1
         
        ## close the file after use
        datafile.close()
        return best_company_records
        
    
             
if __name__ == '__main__':
    doctest.testmod()
    try:
        share_price = CompanyHighestSharePrice()
        results = share_price.get_highest_share_price()
        pprint(results)
    except IOError:
        print 'No such  csv data file found'