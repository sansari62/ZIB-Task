# ZIB-Task



Modeling real covid data in Germany with SIR model:
In this code first of all the number of active infected cases are read from input file,
then this data subdevided to 8 tim window, each one follow a special distribution.
since we model it with use of SIR epiemic model,for each distribution there are 2 different 
beta and delta rates, beta is the transmission rate and delta is recovery rate.
after fitting data, different fitted curves are plotted at the end. 

for each state in Germany, just need to change this line in code:
M_New = M.iloc[9,1:367] 
9 is shows the index of the row for that state, for example 6 is Berlin, 9 is HMBURG, 3 IS Bayern and 20 is the whole Germany

The title of plot can be customized for each state via this line:
fig1.suptitle ('Active infected − Hamburg',fontsize =14,
fontweight ='bold')

and mor eimportant the data file is Fallzahlen_Kum_Tab_aktuell.xlsx that I downloaded it from RKI
