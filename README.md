# file-send-nd-checker
## Feature 1:
1. Code to check only 2 files are sent. 
2. Code to check from these 2 files - 1 is JSON and 1 is pdf. 
3. Kindly make sure these are python scripts and include classes and functions.

## How to run
1. clone repo: ```https://github.com/ashokgarsulla/file-send-nd-checker.git ```
2. go to the dir: file-send-nd-checker
3. run App.py
4. File can change using: add_file_to_send(<filename_or_dir>)
``` python
    file1  = "Files/mock_data.json"
    file2 = "Files/kect108.pdf"
    file3 = "Files/react.png"

    test = FileSendChecker()
    test.add_file_to_send(file1)
    test.add_file_to_send(file2)
```

## Feature 2:
- Develop code to scrap normal transactions
- https://bscscan.com/txs

## How to run
1. clone repo: ```https://github.com/ashokgarsulla/file-send-nd-checker.git ```
2. go to the dir: file-send-nd-checker
> **Warning** Please change before run ``` bscscan_scrap.py ``` range of page 
``` python 
for page in range(1,10001):
    req = requests.get(bscscan + str(page),headers=headers) 
```
3. run ``` bscscan_scrap.py ```  

5. scrapped data will be saved in csv file with name ``` current date and time ``` Eg: ``` 21102022170222.csv ```

### Demo
- pre scrapped data upto 1800 pages
- for demo open https://raw.githubusercontent.com/ashokgarsulla/file-send-nd-checker/master/21102022170222.csv
