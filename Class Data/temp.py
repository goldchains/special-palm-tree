# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn import linear_model

#BCOFInalMarks2018
xl = pd.ExcelFile("BCOFinalMarks2018.xlsx")
df = xl.parse("Sheet1")

df = df.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7'], axis=1)
df.columns = ['StudentNo', 'Test1', 'Test2', 'ClassMark', 'ExamMark', 'FinalMark']
df = df.drop(df.index[:10], axis=0)
df = df.drop(df.index[329:], axis=0)

df.reset_index(drop=True, inplace=True)

df['Outcome'] = (df['FinalMark'] >= 50)

#BCOFinalMarks-2017
xla = pd.ExcelFile("BCOFinalMarks-2017.xls")
dfa = xla.parse("Sheet1")
dfa = dfa.drop(['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 5', 'Unnamed: 7','Unnamed: 10'], axis=1)
dfa.columns = ['StudentNo', 'Test1', 'Test2', 'ClassMark', 'ExamMark', 'FinalMark']
dfa = dfa.drop(dfa.index[:10], axis=0)
dfa = dfa.drop(dfa.index[232:], axis=0)

dfa.reset_index(drop=True, inplace=True)

dfa['Outcome'] = (dfa['FinalMark'] >= 50)

#BCOFinalMarks2016
xlb = pd.ExcelFile("COMS1015(BCO)FinalMarks2016.xls")
dfb = xlb.parse("report")

dfb = dfb.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7'], axis=1)
dfb.columns = ['StudentNo', 'Test1', 'Test2', 'ClassMark', 'ExamMark', 'FinalMark']
dfb = dfb.drop(dfb.index[:10], axis=0)
dfb = dfb.drop(dfb.index[241:], axis=0)
dfb.reset_index(drop=True, inplace=True)

dfb['Outcome'] = (dfb['FinalMark'] >= 50)

#BCOFinalMarks2015
xlc = pd.ExcelFile("BCOFinalMarks2015.xls")
#print(xlc.sheet_names)
dfc = xlc.parse("report")

dfc = dfc.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7'], axis=1)
dfc.columns = ['StudentNo', 'Test1', 'Test2', 'ClassMark', 'ExamMark', 'FinalMark']
dfc = dfc.drop(dfc.index[:10], axis=0)
dfc = dfc.drop(dfc.index[149:], axis=0)
dfc.reset_index(drop=True, inplace=True)

dfc['Outcome'] = (dfc['FinalMark'] >= 50)


#BCO Final Marks-2014
xld = pd.ExcelFile("BCO Final Marks-2014.xls")
#print(xld.sheet_names)
dfd = xld.parse("report")

dfd = dfd.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7'], axis=1)
dfd.columns = ['StudentNo', 'Test1', 'Test2', 'ClassMark', 'ExamMark', 'FinalMark']
dfd = dfd.drop(dfd.index[:10], axis=0)
dfd = dfd.drop(dfd.index[161:], axis=0)
dfd.reset_index(drop=True, inplace=True)

dfd['Outcome'] = (dfd['FinalMark'] >= 50)


#BCOFinalMarks2013
xle = pd.ExcelFile("BCOFinalMarksOfficial2013.xls")
#print(xle.sheet_names)
dfe = xle.parse("report (3)")

dfe = dfe.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7'], axis=1)
dfe.columns = ['StudentNo', 'Test1', 'Test2', 'ClassMark', 'ExamMark', 'FinalMark']
dfe = dfe.drop(dfe.index[:10], axis=0)
dfe = dfe.drop(dfe.index[128:], axis=0)
dfe.reset_index(drop=True, inplace=True)

dfe['Outcome'] = (dfe['FinalMark'] >= 50)


#IAPFinalMarks2018
xlf = pd.ExcelFile("IAPFinalMarks2018(Final).xlsx")
#print(xlf.sheet_names)
dff = xlf.parse("report")

dff = dff.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 9', 'Unnamed: 10',  'Unnamed: 11', 'Unnamed: 13', 'Unnamed: 15', 'Unnamed: 16'], axis=1)
dff.columns = ['StudentNo', 'Test1','LabTest1', 'Test2', 'LabTest2', 'ClassMark','LabExam', 'ExamMark', 'FinalMark']
dff = dff.drop(dff.index[:9], axis=0)
dff = dff.drop(dff.index[317:], axis=0)
dff.reset_index(drop=True, inplace=True)

dff['Outcome'] = (dff['FinalMark'] >= 50)


#IAPFinalMarks2017
xlg = pd.ExcelFile("IAPFinalMarks2017.xlsx")
#print(xlg.sheet_names)
dfg = xlg.parse("report")

dfg = dfg.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 9', 'Unnamed: 10',  'Unnamed: 11', 'Unnamed: 13', 'Unnamed: 15', 'Unnamed: 16'], axis=1)
dfg.columns = ['StudentNo', 'LabTest1','Test1', 'LabTest2', 'Labs', 'ClassMark','LabExam', 'ExamMark', 'FinalMark']
dfg = dfg.drop(dfg.index[:9], axis=0)
dfg = dfg.drop(dfg.index[244:], axis=0)
dfg.reset_index(drop=True, inplace=True)

dfg['Outcome'] = (dfg['FinalMark'] >= 50)





#IAPFinalMarks2016
xlh = pd.ExcelFile("COMS1018(IAP)FinalMarks2016.xls")
#print(xlh.sheet_names)
dfh = xlh.parse("report")

dfh = dfh.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 9', 'Unnamed: 10',  'Unnamed: 11', 'Unnamed: 13'], axis=1)
dfh.columns = ['StudentNo', 'Test1','Test2', 'LabTest', 'Assign', 'ExamMark', 'FinalMark']
dfh = dfh.drop(dfh.index[:9], axis=0)
dfh = dfh.drop(dfh.index[239:], axis=0)
dfh.reset_index(drop=True, inplace=True)

dfh['Outcome'] = (dfh['FinalMark'] >= 50)



#IAPFinalMarks2015
xli = pd.ExcelFile("IAP FinalMarks2015.xls")
#print(xli.sheet_names)
dfi = xli.parse("report")

dfi = dfi.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 9',  'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15'], axis=1)
dfi.columns = ['StudentNo', 'Test1','Test2', 'LabTest', 'ClassMark', 'ExamMark', 'FinalMark']
dfi = dfi.drop(dfi.index[:10], axis=0)
dfi = dfi.drop(dfi.index[146:], axis=0)
dfi.reset_index(drop=True, inplace=True)

dfi['Outcome'] = (dfi['FinalMark'] >= 50)


#IAPFinalMarks2014
xlj = pd.ExcelFile("IAP FinalMarks-2014.xls")
#print(xlj.sheet_names)
dfj = xlj.parse("report")

dfj = dfj.drop(['Unnamed: 1', 'Unnamed: 3',  'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 9',  'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15'], axis=1)
dfj.columns = ['StudentNo', 'Test1','Test2', 'Labtest', 'ClassMark', 'ExamMark', 'FinalMark']
dfj = dfj.drop(dfj.index[:10], axis=0)
dfj = dfj.drop(dfj.index[129:], axis=0)
dfj.reset_index(drop=True, inplace=True)

dfj['Outcome'] = (dfj['FinalMark'] >= 50)


#Combining DataFrames For BCO
frames = [df, dfa, dfb, dfc, dfd, dfe]
result = pd.concat(frames)
result.reset_index(drop=True, inplace=True)
result.dropna(inplace=True)
#Model
train = result.sample(frac=0.8,random_state=200)
test = result.drop(train.index)

clf = LinearSVC(random_state=0)
clf.fit(np.array(train.Test1).reshape(-1, 1),train.Outcome)
predictions = clf.predict(np.array(test.Test1).reshape(-1, 1))

print(classification_report(test.Outcome,predictions))
print(accuracy_score(test.Outcome,predictions))

clf = LinearSVC(random_state=0)
clf.fit(train[['Test1','Test2']],train.Outcome)
predictions = clf.predict(test[['Test1','Test2']])

print(classification_report(test.Outcome,predictions))
print(accuracy_score(test.Outcome,predictions))

clf = LinearSVC(random_state=0)
clf.fit(np.array(train.ClassMark).reshape(-1, 1),train.Outcome)
predictions = clf.predict(np.array(test.ClassMark).reshape(-1, 1))

print(classification_report(test.Outcome,predictions))
print(accuracy_score(test.Outcome,predictions))


#Model Logistic Regression
logreg = linear_model.LogisticRegression()
logreg.fit(np.array(train.Test1).reshape(-1, 1),train.Outcome)
predictions = logreg.predict(np.array(test.Test1).reshape(-1, 1))

print(classification_report(test.Outcome,predictions))
print(accuracy_score(test.Outcome,predictions))



logreg.fit(train[['Test1','Test2']],train.Outcome)
predictions = logreg.predict(test[['Test1','Test2']])

print(classification_report(test.Outcome,predictions))
print(accuracy_score(test.Outcome,predictions))


logreg.fit(np.array(train.ClassMark).reshape(-1, 1),train.Outcome)
predictions = logreg.predict(np.array(test.ClassMark).reshape(-1, 1))

print(classification_report(test.Outcome,predictions))
print(accuracy_score(test.Outcome,predictions))


























































































































