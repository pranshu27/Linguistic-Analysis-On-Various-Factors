I have used Anaconda 4.10.3, (Python 3.8.10) interpretor and the packeges used are as follows:-

- pandas
- xlrd
- openpyxl
- warnings
- scipy

The files/datasets used are:-
1) https://censusindia.gov.in/2011census/C-17.html
2) https://censusindia.gov.in/2011Census/Language-2011/DDW-C18-0000.xlsx
3) https://censusindia.gov.in/2011Census/Language-2011/DDW-C19-0000.xlsx
4) https://censusindia.gov.in/2011census/C-series/C-14.html
5) https://censusindia.gov.in/2011census/C-series/C08.html


Steps to run:

1. After extracting the contents please install the packages mentioned above. PS: Some of them may not come pre-installed with Anaconda.
2. Open a terminal window in the folder '2111048_assign2' created after the extraction process
3. In order to run the entire assignment at once, use the command './assign2.sh'
4. In order to run an individual question, use the '.sh' file corresponding to that particular question, example, './percent-india.sh'
5. Please have some patience. It takes ~3 seconds to run the entire assignment









Description and names of files generated in each question:

1) The output file generated is 
	1. ‘percent-india.csv’. 

2) In this part, I have calculated  the percentage of rural and urban people sho speak:
	1. ‘Three or more language’, 
	2. ‘Exactly two languages’ and 
	3. ‘Only one language’ 
	
using [2] and [1]. 

Afterwards I have calculated the ‘p-value’ by finding the ‘urban to rural’ ratio for ‘Three or more language’, ‘Exactly two languages’, ‘Only one language’ and ‘Total ratio of urban to rural’. 
This data was then used '1-sample t-test' to compute the ‘P value’.

The files created after execution of the code are:
	1. ‘gender-india-a.csv’  
	2. ‘gender-india-b.csv’
	3. ‘gender-india-c.csv’.

3) In this part, I have calculated  the percentage of rural and urban people sho speak:
	1. ‘Three or more language’, 
	2. ‘Exactly two languages’ and 
	3. ‘Only one language’ 
	
using [2] and [4]. 

Afterwards I have calculated the ‘p-value’ by finding the ‘urban to rural’ ratio for ‘Three or more language’, ‘Exactly two languages’, ‘Only one language’ and ‘Total ratio of urban to rural’. 
This data was then used '1-sample t-test' to compute the ‘P value’. 

The files generated are 
	1. ‘geography-india-a.csv’
	2. ‘geography-india-b.csv’
	3. ‘geography-india-c.csv’.

4) For part 'a', the output file is named 
	1. '3-to-2-ratio.csv' 

and for part 'b', the file generated is:
	1. '2-to-1-ratio.csv'

5) The name of the output file is:
	1. ‘age-india.csv’.
	
6) Here, the file generated is:
	1. 'literacy-india.csv'

7) The output files generated here are:
	1. 'region-india-a.csv'
	2. 'region-india-b.csv'

8) The files generated are:
	1. 'age-gender-a.csv'
	2. 'age-gender-b.csv'
	3. 'age-gender-c.csv'

9) The files generated are:
	1. 'literacy-gender-a.csv'
	2. 'literacy-gender-b.csv'
	3. 'literacy-gender-c.csv' 





Results:

1. There are exactly 19 '.csv' files created after all the '.sh' files are executed.
2. These files are visible in the 'output' directory



