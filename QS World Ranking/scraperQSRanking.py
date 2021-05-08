from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlsxwriter
import time





# INITIALIZING VARIABLES
PATH = '<exact path to your chrome webdriver>'
TIME = 3
NEXT_PAGE_ITER = 0 





# CREATING WEB DRIVER
driver = webdriver.Chrome(PATH)
driver.get('https://www.topuniversities.com/university-rankings/world-university-rankings/2021')
print(driver.title)
time.sleep(TIME)





# INDICATOR BUTTON
rankingIndicatorBtn = driver.find_element_by_css_selector('.nav-item.last')
rankingIndicatorBtn.click()
time.sleep(TIME+2)





# TO SHOW TOP 100 LIST
dropdown = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[3]/div[1]/div[2]/i')
dropdown.click()
time.sleep(TIME)
no100 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[3]/div[1]/div[2]/div[2]/div[4]')
no100.click()
time.sleep(TIME+10)





# TO GO TO THE NEXT PAGE
for i in range(NEXT_PAGE_ITER):
    nextBtn = driver.find_element_by_css_selector('.page-link.next')
    nextBtn.click()
    time.sleep(TIME+8)
time.sleep(TIME+10)





# EXTRACTING DATA

time.sleep(TIME)
ranks = driver.find_elements_by_css_selector('._univ-rank')
time.sleep(TIME)
ranks = [elem.text for elem in ranks][200:]
print(ranks)

uniList = driver.find_elements_by_class_name('uni-link')
uniList = [elem.text for elem in uniList][100:]
print(uniList)

overallScore = driver.find_elements_by_css_selector('.overall-score-span-ind.overall')
overallScore = [elem.text for elem in overallScore]

IntStudRatio = driver.find_elements_by_css_selector('.overall-score-span-ind.ind_14')
IntStudRatio = [elem.text for elem in IntStudRatio]

IntFacRatio = driver.find_elements_by_css_selector('.overall-score-span-ind.ind_18')
IntFacRatio = [elem.text for elem in IntFacRatio]

FacStudRatio = driver.find_elements_by_css_selector('.overall-score-span-ind.ind_36')
FacStudRatio = [elem.text for elem in FacStudRatio]

citationsPerFac = driver.find_elements_by_css_selector('.overall-score-span-ind.ind_73')
citationsPerFac = [elem.text for elem in citationsPerFac]

academicReputation = driver.find_elements_by_css_selector('.overall-score-span-ind.ind_76')
academicReputation = [elem.text for elem in academicReputation]

employerReputation = driver.find_elements_by_css_selector('.overall-score-span-ind.ind_77')
employerReputation = [elem.text for elem in employerReputation]

driver.quit()





# PRINTING DATA STORED IN THE VARIABLES
print(ranks)
print(uniList)
print(overallScore)
print(IntStudRatio)
print(IntFacRatio)
print(FacStudRatio)
print(citationsPerFac)
print(academicReputation)
print(employerReputation)





# SAVING DATA IN AN EXCEL FILE
wb = xlsxwriter.Workbook(r'exact path to the excel file where you want to store the data')
ws = wb.add_worksheet()

headings = ['Rank', 'University', 'Overall Score', 'International Students Ratio', 'International Faculty Ratio', 'Faculty Student Ratio', 'Citations per Faculty', 'Academic Reputation', 'Employer Reputation']
for head in range(len(headings)):
    ws.write(0, head, headings[head])

# print(uniqueId, schoolName, queryNo, regDate, subCategory, mailOfComplaint, state, phone, fileData, queryDetails, remark, status, finalStatus)
for item in range(len(employerReputation)):
    ws.write(item+1, 0, ranks[item])
    ws.write(item+1, 1, uniList[item])
    ws.write(item+1, 2, overallScore[item])
    ws.write(item+1, 3, IntStudRatio[item])
    ws.write(item+1, 4, IntFacRatio[item])
    ws.write(item+1, 5, FacStudRatio[item])
    ws.write(item+1, 6, citationsPerFac[item])
    ws.write(item+1, 7, academicReputation[item])
    ws.write(item+1, 8, employerReputation[item])

wb.close()