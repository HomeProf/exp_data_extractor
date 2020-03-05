import re

# extracts three in a row exponetial data tuples per line
# and save it to csv file.

#@author: Benedikt Hofrichter,
#         benedikt.hofrichter@benespira.com

class extractor:

    source_filepath = "CV_Initial.txt"
    target_filepath = "csv_data.csv"

    # def __init(self):
        # self.source_filepath = "CV_Initial.txt"
        # self.target_filepath = "csv_data.csv"

    def is_exp_expression(self, val):
            p = re.compile("[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?")
            isMatch = p.match(val)
            if(isMatch == None):
                return False
            else:
                return True


    def is_tiple_exp_line(self, unqual_line):
        #print(unqual_line)
        cols = unqual_line.split(' ')
        result = []
        cols = list(filter(None, cols))
        print(cols)
        for val in cols:
            val_stripped = val.strip()
            if (self.is_exp_expression(val_stripped) == False):
                return False
            result.append(val_stripped)
        if(len(result)<3):
            return False
        return result



    def check_and_write_to_CSV(self, line_array, tf):
            for val in line_array:
                  tf.write('{0}{1}'.format(val, ", "))
            tf.write('\n')


    def process(self):
           with open(self.source_filepath, 'r') as fp, open(self.target_filepath, "w") as tf:
                for line in fp.readlines():
                        qual_array = self.is_tiple_exp_line(line)
                        if isinstance(qual_array, list):
                            self.check_and_write_to_CSV(qual_array, tf)


processor = toCSV()
processor.process()
