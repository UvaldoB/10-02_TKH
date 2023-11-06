import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
           data_row = row[1:]
           y = [] 
           for x in data_row:
               try:
                   y.append(float(x))
               except ValueError:
                   continue 
           average = stats.mean(y)
           rounded_average = round(average, 3)
           averages.append(rounded_average)                                  


        return averages

    def median02(self):
        """pt2
        """
        medians = []
        for row in self.data:
           data_row = row[1:]
           b = [] 
           for a in data_row:
               try:
                   b.append(float(a))
               except ValueError:
                   continue 
           median = stats.median(b)
           rounded_median = round(median, 3)
           medians.append(rounded_median) 

    
    def stddev03(self):
        """pt3
        """
        stddev = [] 
        for row in self.data:
           data_row = row[1:]
           d = [] 
           for c in data_row:
               try:
                   d.append(float(c))
               except ValueError:
                   continue 
           stddev = stats.stddev(d)
           rounded_stddev = round(stddev, 3)
           stddev.append(rounded_stddev) 
