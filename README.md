#Gender Analysis of Business Owners in the City of Chicago

##Introduction
The entrepreneurship gender gap persists. A census from 2012 revealed that 10% of American men ran their own business, while only 7% of women ran their own business.  Today, despite the fact that women comprise almost half of the workforce, they hold only 10% of S&P executive positions, and a mere 3% of Fortune 500 companies are run by
women. While we have data that demonstrates that women are underrepresented in higher positions in large companies, is the ratio similar in small and medium businesses? The City of Chicago offers data on business owners information for all the accounts listed in Business License Dataset. The city's latest statistics on business ownership dates to 2007, reporting 123,852 men-owned firms (58%), and 92,119 women-owned firms (41%). The dataset analyzed in this project was most recently updated on March 10th, 2016. 


##Methodology and caveats
The source of the data: [Data.gov](https://data.cityofchicago.org/api/views/ezma-pppn/rows.csv?accessType=DOWNLOAD)
The data contains information on 252,287 business owners in the City of Chicago. The CSV includes details such as business account number, businesss name, owner first name, owner last name, and title.   
To classify gender, I will use the detect_gender() function. For all names with suffix or middle names or other keys non-detectable by the detect_gender() function, I will use extract_usable_name(). 
This data only shows position titles. Ideally, salary for each business owner would have been interesting to analyze, although this information is not provided. Additionally, titles are difficult to sort, as businesses are run differently. In one firm, the President may truly hold more power, whereas in another, it may be the CEO. Cognizant of this, we code "President," "CEO," and "Sole Proprietor" as a higher positions. 
Another caveat is that some individuals are entered into the database more than once. Looking at the data, these individuals are owners for multiple businesses or multiple stores in a chain. 


##Past research and articles
- [The Business Benefits of Closing the Gender Gap](http://www.ddiworld.com/ddi/media/trend-research/womenatworkgendergap_br_ddi.pdf)
- [City of Chicago Statistics](http://www.census.gov/quickfacts/table/PST045215/1714000)
- ['Jarring' Gender Gap Exists for Women Business Owners](http://www.inc.com/associated-press/women-business-owners-facing-gender-gap.html)
- [Closing the Business-Ownership Gender Gap](http://www.entrepreneur.com/article/231115)
- [What's The Status Of Women's Equality In Illinois?](http://progressillinois.com/quick-hits/content/2015/08/24/whats-status-womens-equality-illinois)
- [Number of Women In Senior Management Stagnant At 24%](http://www.forbes.com/sites/forbesasia/2014/03/06/number-of-women-in-senior-management-stagnant-at-24/#fde9d424d60d)

##How to this program
To run this program, please run these scripts in the following order: 
* _fetch_data.py_ Running this script will download a large files from the Data.gov website and store them in tempdata/
* _wrangle_data.py_ Running this script will trim this large file into wrangle_Biz.csv
* _fetch_gender_data.py_ Running this script will download all of the baby names data from the Social Security Administration and store it to tempdata/names.zip
* _wrangle_gender_data.py_ Running this script will reshape the babynames files from 1950 to 2014 to optimize for use in a gender-detecting program, and store it as wrangledbabynames.csv. This script will also convert the wrangled baby nanmes csv into a json format, stored as wrangledbabynames.json. 
* _classify.py_ Running this script creates a new data file with gender classification to the Chicago Business Owners data, stored to tempdata/classified_Biz.csv. It also establishes that the name being run through our gender dectector function is a viable name (ie. not a first initial or a first and middle name). 
* _analyze.py_ Running this function will open and read the tempdata/classified_Biz.csv and apply some analyses. 

**Ancillary files**
* _gender.py_ This script loads the wrangledbabynames.json file and applies the gender detector function, returning a dictionary that identifies the name in the tempdata/wrangledbabynames.json and supplies each name with gender and ratio. Code not needed to run, but will be called upon by classify.py. 

##Analysis
The total demographic breakout of business owners in the city of Chicago reveals that 62% are male and 38% female. While these numbers are similar to the 2007 statistics of 58% male and 41% female, it is a smaller gender gap. At the national level, a [study](http://www.forbes.com/sites/forbesasia/2014/03/06/number-of-women-in-senior-management-stagnant-at-24/#fde9d424d60d) found that senior business roles held by women has remained stagnant from 2007-2014. The 3% increase in the city of Chicago is a hopeful sign. Indeed, Illinois is the third most equal state for women according to personal finance website [WalletHub](http://progressillinois.com/quick-hits/content/2015/08/24/whats-status-womens-equality-illinois). 

While this data already sorts out low-level jobs, it is interesting to notice that ranks of business owners. Some postitions are considered more senior than others. According to our analysis, I conclude that of 243,694 business owners, 113,551 (46%) are more senior titles. 

Additionally, women holding this more senior roles reports 28%, compared to men in more senior roles at 62%. This is a much larger gender gap, manifesting that as we move further up the management ladder, women are increasingly underrepresented. This is troubling, as a report by [McKinsey & Company](http://www.ddiworld.com/ddi/media/trend-research/womenatworkgendergap_br_ddi.pdf) evidenced that "having a critical mass of at least 30% percent women in higher-level leadership positions significantly improves financial performance." This source also found that women in senior-level positions in fact dropped 5% from 2009 to 2011. Unfortunately, data for women in senior positions in 2007 could not be found for comparison. 

This dataset not only reported managerial positions, but also listed "Shareholders." In my analysis, I found that no women were indexed as a shareholder. This is significant, as the (Kauffman Foundation)[http://www.huffingtonpost.com/claudia-viek/another-gender-gap-business-ownership_b_5846620.html]'s findings show that women entrepreneurs "receive approximately 80% less capital and receive only 5% of equity capital annually compared to male-owned businesses." With more female shareholders, women may have more equal access to capital. 

Overall, we can be pleased to see an increase in females as business owners in 2016 compared to 2007. We may hope that this increase in the city of Chicago is represented across the nation, or that Chicago's numbers are instigating a national trend. Still, these numbers demonstrate that the gender gap persists. 


