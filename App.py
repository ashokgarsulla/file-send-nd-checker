import os

class FileChecker:
    def extension(self,file_dir):
        name, extension = os.path.splitext(file_dir)
        return extension


class FileSendChecker(FileChecker):

    no_of_files = []
# It allow only add two file to send : If more than two files are added than raise an error 
    def add_file_to_send(self,dir):
        if(len(self.no_of_files) < 2):
            self.no_of_files.append(dir)
        else:
            raise "Only two files can be sent"

# It will check that 1 pdf and 1 json file
    def check_sent_file(self):
        if len(self.no_of_files) == 2:
            if self.extension(self.no_of_files[0]) == '.json' and self.extension(self.no_of_files[1]) == '.pdf':
                print(" 1 pdf and 1 json files are sent respectively")
            elif self.extension(self.no_of_files[0] )== '.pdf' and self.extension(self.no_of_files[1]) == '.json':
                print("1 json and 1 pdf files are sent respectively")
            else:
                print("please select 1 json and 1 pdf file")
        else :
            print("Something went wrong.....Try again!")

    def get_all_files(self):
        return self.no_of_files



# main function------------------------
def main():

    # files
    file  = "C/work/workiing.json"
    file2 = "D/working/test.pdf"

    test = FileSendChecker()
    test.add_file_to_send(file)
    test.add_file_to_send(file)

    test.check_sent_file()   


if __name__ == "__main__":
    main()