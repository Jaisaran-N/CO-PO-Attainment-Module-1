import streamlit as st
import pandas as pd
def main():
    st.title("CO-PO ATTAINMENT CALCULATION")
    menu=["Mid Sem One","Mid Sem Two","Preparatory"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=="Mid Sem One":
        st.subheader("Mid Sem One")
        data_file=st.file_uploader("Upload Your Mid Sem 1 Excel",type=["xlsx","csv"])
        if data_file is not None:
            #st.write(type(data_file))
            #file_details={"filename":data_file.name,"filetype":data_file.type,"filesize":data_file.size}
            #st.write(file_details)
            df=pd.read_excel(data_file)
            #st.dataframe(df)
            index_RegNo1=df.columns.get_loc('Reg No')
            index_CO1=df.columns.get_loc('CO1')
            index_CO1_1=df.columns.get_loc('CO1.1')
            index_CO1_2=df.columns.get_loc('CO1.2')
            index_CO1_3=df.columns.get_loc('CO1.3')
            index_CO1_4=df.columns.get_loc('CO1.4')
            index_CO1_5=df.columns.get_loc('CO1.5')
            index_CO1_6=df.columns.get_loc('CO1.6')
            index_CO1_7=df.columns.get_loc('CO1.7')
            index_CO2=df.columns.get_loc('CO2')
            index_CO2_1=df.columns.get_loc('CO2.1')
            index_CO2_2=df.columns.get_loc('CO2.2')
            index_CO2_3=df.columns.get_loc('CO2.3')
            index_CO2_4=df.columns.get_loc('CO2.4')
            index_CO2_5=df.columns.get_loc('CO2.5')
            index_CO2_6=df.columns.get_loc('CO2.6')
            index_CO2_7=df.columns.get_loc('CO2.7')
            index_CO1S=df.columns.get_loc('CO1S')
            index_CO2S=df.columns.get_loc('CO2S')
            index_Total=df.columns.get_loc('Total')
            index_Name=df.columns.get_loc("Name")
            if st.button('Details'):
                def printing():
                    a=df.iloc[1:,[0,1]]
                    st.write(a)
                printing()
            df['CO1'] = df['CO1'].fillna(0)
            df['CO1.1'] = df['CO1.1'].fillna(0)
            df['CO1.2'] = df['CO1.2'].fillna(0)
            df['CO1.3'] = df['CO1.3'].fillna(0)
            df['CO1.4'] = df['CO1.4'].fillna(0)
            df['CO1.5'] = df['CO1.5'].fillna(0)
            df['CO1.6'] = df['CO1.6'].fillna(0)
            df['CO1.7'] = df['CO1.7'].fillna(0)
            df['CO1'] = df['CO1'].fillna(0)
            df['CO2.1'] = df['CO2.1'].fillna(0)
            df['CO2.2'] = df['CO2.2'].fillna(0)
            df['CO2.3'] = df['CO2.3'].fillna(0)
            df['CO2.4'] = df['CO2.4'].fillna(0)
            df['CO2.5'] = df['CO2.5'].fillna(0)
            df['CO2.6'] = df['CO2.6'].fillna(0)
            df['CO2.7'] = df['CO2.7'].fillna(0)
            df['CO2S'] = df['CO2S'].fillna(0)
            df['CO1S'] = df['CO1S'].fillna(0)
            df['Total'] = df['Total'].fillna(0)
            #st.dataframe(df)
            for row in range(1, len(df)):
	            df.iat[row, index_CO1S] = df.iat[row,index_CO1] + df.iat[row,index_CO1_1]+df.iat[row,index_CO1_2] + df.iat[row,index_CO1_3]+df.iat[row,index_CO1_4]+df.iat[row,index_CO1_5]+df.iat[row,index_CO1_6]+df.iat[row,index_CO1_7]
            for row in range(1, len(df)):
	            df.iat[row, index_CO2S] = df.iat[row,index_CO2] + df.iat[row,index_CO2_1]+ df.iat[row,index_CO2_2] + df.iat[row,index_CO2_3]+df.iat[row,index_CO2_4]+df.iat[row,index_CO2_5]+df.iat[row,index_CO2_6]+df.iat[row,index_CO2_7]
            for row in range(1,len(df)):
	            df.iat[row,index_Total]=df.iat[row,index_CO1S]+df.iat[row,index_CO2S]
            def detail():
                name=[]
                user_input=st.text_input("Enter The Student Name:","Eg.DEEBAN N")
                name.append(user_input)
                deto=df.loc[df['Name'].isin(name),['Name','Reg No','CO1S','CO2S','Total']]
                if deto is not None:
                    st.write(deto)
                else:
                    st.write("Try Again")
            detail() 
            threshold1 = st.slider("Threshold For CO1")
            st.write("Threshold Value:",threshold1)
            if st.button('Threshold CO1'):
                def thres():
                    ar=[]
                    count=0
                    row=-1
                    df.iat[row+1, index_CO1S] = df.iat[row+1,index_CO1] + df.iat[row+1,index_CO1_1]+df.iat[row+1,index_CO1_2] + df.iat[row+1,index_CO1_3]+df.iat[row+1,index_CO1_4]+df.iat[row+1,index_CO1_5]+df.iat[row+1,index_CO1_6]+df.iat[row+1,index_CO1_7]
                    df.iat[row+1, index_CO2S] = df.iat[row+1,index_CO2] + df.iat[row+1,index_CO2_1]+ df.iat[row+1,index_CO2_2] + df.iat[row+1,index_CO2_3]+df.iat[row+1,index_CO2_4]+df.iat[row+1,index_CO2_5]+df.iat[row+1,index_CO2_6]+df.iat[row+1,index_CO2_7]
                    pass_mark=(threshold1/100)*df.iat[row+1, index_CO1S]
                    st.write(pass_mark)
                    for i in range(1,len(df)):
                        ar.append(df['CO1S'].gt(pass_mark))
                    for j in range(1,len(ar)+1):
            	        if(df.iat[j,index_CO1S]>pass_mark):
            		        st.write(df.iat[j,index_Name],df.iat[j,index_RegNo1],df.iat[j,index_CO1S])
            		        count=count+1
                    st.write("Pass Count:",count)
                    passper=(count/len(df))*100
                    st.write("Pass Percentage:",passper)
                thres()
            threshold1_1 = st.slider("Threshold For CO2 ")
            st.write("Threshold Value:",threshold1_1)
            if st.button('Threshold CO2'):
                def thres1():
                    ar1=[]
                    count1=0
                    row=-1
                    df.iat[row+1, index_CO2S] = df.iat[row+1,index_CO2] + df.iat[row+1,index_CO2_1]+ df.iat[row+1,index_CO2_2] + df.iat[row+1,index_CO2_3]+df.iat[row+1,index_CO2_4]+df.iat[row+1,index_CO2_5]+df.iat[row+1,index_CO2_6]+df.iat[row+1,index_CO2_7]
                    pass_mark1=(threshold1_1/100)*df.iat[row+1, index_CO2S]
                    st.write(pass_mark1)
                    for i in range(1,len(df)):
            	        ar1.append(df['CO2S'].gt(pass_mark1))
                    for j in range(1,len(ar1)+1):
            	        if(df.iat[j,index_CO2S]>pass_mark1):
            		        st.write(df.iat[j,index_Name],df.iat[j,index_RegNo1],df.iat[j,index_CO2S])
            		        count1=count1+1
                    st.write("Pass Count:",count1)
                    passper1=(count1/len(df))*100
                    st.write("Pass Percentage:",passper1)
                thres1()
    if choice=="Mid Sem Two":
        st.subheader("Mid Sem Two")
        data_file2=st.file_uploader("Upload Your Mid Sem 2 Excel",type=["xlsx","csv"])
        if data_file2 is not None:
            #st.write(type(data_file))
            #file_details={"filename":data_file.name,"filetype":data_file.type,"filesize":data_file.size}
            #st.write(file_details)
            df2=pd.read_excel(data_file2)
            #st.dataframe(df)
            index_RegNo2=df2.columns.get_loc('Reg No')
            index_CO3=df2.columns.get_loc('CO3')
            index_CO3_1=df2.columns.get_loc('CO3.1')
            index_CO3_2=df2.columns.get_loc('CO3.2')
            index_CO3_3=df2.columns.get_loc('CO3.3')
            index_CO3_4=df2.columns.get_loc('CO3.4')
            index_CO3_5=df2.columns.get_loc('CO3.5')
            index_CO3_6=df2.columns.get_loc('CO3.6')
            index_CO3_7=df2.columns.get_loc('CO3.7')
            index_CO4=df2.columns.get_loc('CO4')
            index_CO4_1=df2.columns.get_loc('CO4.1')
            index_CO4_2=df2.columns.get_loc('CO4.2')
            index_CO4_3=df2.columns.get_loc('CO4.3')
            index_CO4_4=df2.columns.get_loc('CO4.4')
            index_CO4_5=df2.columns.get_loc('CO4.5')
            index_CO4_6=df2.columns.get_loc('CO4.6')
            index_CO4_7=df2.columns.get_loc('CO4.7')
            index_CO3S=df2.columns.get_loc('CO3S')
            index_CO4S=df2.columns.get_loc('CO4S')
            index_Total2=df2.columns.get_loc('Total')
            index_Name2=df2.columns.get_loc("Name")
            if st.button('Details'):
                def printing2():
                    a2=df2.iloc[1:,[0,1]]
                    st.write(a2)
                printing2()
            df2['CO3'] = df2['CO3'].fillna(0)
            df2['CO3.1'] = df2['CO3.1'].fillna(0)
            df2['CO3.2'] = df2['CO3.2'].fillna(0)
            df2['CO3.3'] = df2['CO3.3'].fillna(0)
            df2['CO3.4'] = df2['CO3.4'].fillna(0)
            df2['CO3.5'] = df2['CO3.5'].fillna(0)
            df2['CO3.6'] = df2['CO3.6'].fillna(0)
            df2['CO3.7'] = df2['CO3.7'].fillna(0)
            df2['CO4'] = df2['CO4'].fillna(0)
            df2['CO4.1'] = df2['CO4.1'].fillna(0)
            df2['CO4.2'] = df2['CO4.2'].fillna(0)
            df2['CO4.3'] = df2['CO4.3'].fillna(0)
            df2['CO4.4'] = df2['CO4.4'].fillna(0)
            df2['CO4.5'] = df2['CO4.5'].fillna(0)
            df2['CO4.6'] = df2['CO4.6'].fillna(0)
            df2['CO4.7'] = df2['CO4.7'].fillna(0)
            df2['CO3S'] = df2['CO3S'].fillna(0)
            df2['CO4S'] = df2['CO4S'].fillna(0)
            df2['Total'] = df2['Total'].fillna(0)
            for row in range(1, len(df2)):
	            df2.iat[row, index_CO3S] = df2.iat[row,index_CO3] + df2.iat[row,index_CO3_1]+df2.iat[row,index_CO3_2] + df2.iat[row,index_CO3_3]+df2.iat[row,index_CO3_4]+df2.iat[row,index_CO3_5]+df2.iat[row,index_CO3_6]+df2.iat[row,index_CO3_7]
            for row in range(1, len(df2)):
	            df2.iat[row, index_CO4S] = df2.iat[row,index_CO4] + df2.iat[row,index_CO4_1]+ df2.iat[row,index_CO4_2] + df2.iat[row,index_CO4_3]+df2.iat[row,index_CO4_4]+df2.iat[row,index_CO4_5]+df2.iat[row,index_CO4_6]+df2.iat[row,index_CO4_7]
            for row in range(1,len(df2)):
	            df2.iat[row,index_Total2]=df2.iat[row,index_CO3S]+df2.iat[row,index_CO4S]
            def detail2():
                name2=[]
                user_input2=st.text_input("Enter The Student Name:","Eg.DEEBAN N")
                name2.append(user_input2)
                deto2=df2.loc[df2['Name'].isin(name2),['Name','Reg No','CO3S','CO4S','Total']]
                if deto2 is not None:
                    st.write(deto2)
                else:
                    st.write("Try Again")
            detail2() 
            threshold2 = st.slider("Threshold For CO3")
            st.write("Threshold Value:",threshold2)
            if st.button('Threshold C03'):
                def thres2():
                    ar2=[]
                    count2=0
                    row=-1
                    df2.iat[row+1, index_CO3S] = df2.iat[row+1,index_CO3] + df2.iat[row+1,index_CO3_1]+df2.iat[row+1,index_CO3_2] + df2.iat[row+1,index_CO3_3]+df2.iat[row+1,index_CO3_4]+df2.iat[row+1,index_CO3_5]+df2.iat[row+1,index_CO3_6]+df2.iat[row+1,index_CO3_7]
                    df2.iat[row+1, index_CO4S] = df2.iat[row+1,index_CO4] + df2.iat[row+1,index_CO4_1]+ df2.iat[row+1,index_CO4_2] + df2.iat[row+1,index_CO4_3]+df2.iat[row+1,index_CO4_4]+df2.iat[row+1,index_CO4_5]+df2.iat[row+1,index_CO4_6]+df2.iat[row+1,index_CO4_7]
                    pass_mark2=(threshold2/100)*df2.iat[row+1, index_CO3S]
                    st.write(pass_mark2)
                    for i in range(1,len(df2)):
                        ar2.append(df2['CO3S'].gt(pass_mark2))
                    for j in range(1,len(ar2)+1):
            	        if(df2.iat[j,index_CO3S]>pass_mark2):
            		        st.write(df2.iat[j,index_Name2],df2.iat[j,index_RegNo2],df2.iat[j,index_CO3S])
            		        count2=count2+1
                    st.write("Pass Count:",count2)
                    passper2=(count2/len(df2))*100
                    st.write("Pass Percentage:",passper2)
                thres2()
            threshold2_1 = st.slider("Threshold For CO4 ")
            st.write("Threshold Value:",threshold2_1)
            if st.button('Threshold CO4'):
                def thres3():
                    ar3=[]
                    count3=0
                    row=-1
                    df2.iat[row+1, index_CO4S] = df2.iat[row+1,index_CO4] + df2.iat[row+1,index_CO4_1]+ df2.iat[row+1,index_CO4_2] + df2.iat[row+1,index_CO4_3]+df2.iat[row+1,index_CO4_4]+df2.iat[row+1,index_CO4_5]+df2.iat[row+1,index_CO4_6]+df2.iat[row+1,index_CO4_7]
                    pass_mark3=(threshold2_1/100)*df2.iat[row+1, index_CO4S]
                    st.write(pass_mark3)
                    for i in range(1,len(df2)):
            	        ar3.append(df2['CO4S'].gt(pass_mark3))
                    for j in range(1,len(ar3)):
            	        if(df2.iat[j,index_CO4S]>pass_mark3):
            		        st.write(df2.iat[j,index_Name2],df2.iat[j,index_RegNo2],df2.iat[j,index_CO4S])
            		        count3=count3+1
                    st.write("Pass Count:",count3)
                    passper3=(count3/len(df2))*100
                    st.write("Pass Percentage:",passper3)
                thres3() 
    if choice=="Preparatory":
        st.subheader("Preparatory")
        data_file3=st.file_uploader("Upload Your Preparatory Excel",type=["xlsx","csv"])
        if data_file3 is not None:
            #st.write(type(data_file))
            #file_details={"filename":data_file.name,"filetype":data_file.type,"filesize":data_file.size}
            #st.write(file_details)
            df3=pd.read_excel(data_file3)
            #st.dataframe(df)
            index_RegNo3=df3.columns.get_loc('Reg No')
            index_CO11=df3.columns.get_loc('CO1')
            index_CO11_1=df3.columns.get_loc('CO1.1')
            index_CO22=df3.columns.get_loc('CO2')
            index_CO22_1=df3.columns.get_loc('CO2.1')
            index_CO33=df3.columns.get_loc('CO3')
            index_CO33_1=df3.columns.get_loc('CO3.1')
            index_CO44=df3.columns.get_loc('CO4')
            index_CO44_1=df3.columns.get_loc('CO4.1')
            index_CO55=df3.columns.get_loc('CO5')
            index_CO55_1=df3.columns.get_loc('CO5.1')
            index_CO11_2=df3.columns.get_loc('CO1.2')
            index_CO22_2=df3.columns.get_loc('CO2.2')
            index_CO33_2=df3.columns.get_loc('CO3.2')
            index_CO44_2=df3.columns.get_loc('CO4.2')
            index_CO55_2=df3.columns.get_loc('CO5.2')
            index_CO1S=df3.columns.get_loc('CO1S')
            index_CO2S=df3.columns.get_loc('CO2S')
            index_CO3S=df3.columns.get_loc('CO3S')
            index_CO4S=df3.columns.get_loc('CO4S')
            index_CO5S=df3.columns.get_loc('CO5S')
            index_Total3=df3.columns.get_loc('Total')
            index_Name3=df3.columns.get_loc("Name")
            if st.button('Details'):
                def printing3():
                    a3=df3.iloc[1:,[0,1]]
                    st.write(a3)
                printing3()
            df3['CO1'] = df3['CO1'].fillna(0)
            df3['CO1.1'] = df3['CO1.1'].fillna(0)
            df3['CO2'] = df3['CO2'].fillna(0)
            df3['CO2.1'] = df3['CO2.1'].fillna(0)
            df3['CO3'] = df3['CO3'].fillna(0)
            df3['CO3.1'] = df3['CO3.1'].fillna(0)
            df3['CO4'] = df3['CO4'].fillna(0)
            df3['CO4.1'] = df3['CO4.1'].fillna(0)
            df3['CO5'] = df3['CO5'].fillna(0)
            df3['CO5.1'] = df3['CO5.1'].fillna(0)
            df3['CO1.2'] = df3['CO1.2'].fillna(0)
            df3['CO2.2'] = df3['CO2.2'].fillna(0)
            df3['CO3.2'] = df3['CO3.2'].fillna(0)
            df3['CO4.2'] = df3['CO4.2'].fillna(0)
            df3['CO5.2'] = df3['CO5.2'].fillna(0)
            df3['CO1S'] = df3['CO1S'].fillna(0)
            df3['CO2S'] = df3['CO2S'].fillna(0)
            df3['CO3S'] = df3['CO3S'].fillna(0)
            df3['CO4S'] = df3['CO4S'].fillna(0)
            df3['CO5S'] = df3['CO5S'].fillna(0)
            df3['Total'] = df3['Total'].fillna(0)
            for row in range(1, len(df3)):
	            df3.iat[row, index_CO1S] = df3.iat[row,index_CO11] + df3.iat[row,index_CO11_1]+df3.iat[row,index_CO11_2]
            for row in range(1, len(df3)):
	            df3.iat[row, index_CO2S] = df3.iat[row,index_CO22] + df3.iat[row,index_CO22_1]+df3.iat[row,index_CO22_2]
            for row in range(1, len(df3)):
	            df3.iat[row, index_CO3S] = df3.iat[row,index_CO33] + df3.iat[row,index_CO33_1]+df3.iat[row,index_CO33_2]
            for row in range(1, len(df3)):
	            df3.iat[row, index_CO4S] = df3.iat[row,index_CO44] + df3.iat[row,index_CO44_1]+ df3.iat[row,index_CO44_2] 
            for row in range(1, len(df3)):
	            df3.iat[row, index_CO5S] = df3.iat[row,index_CO55] + df3.iat[row,index_CO55_1]+df3.iat[row,index_CO55_2]
            for row in range(1,len(df3)):
	            df3.iat[row,index_Total3]=df3.iat[row,index_CO1S]+df3.iat[row,index_CO2S]+df3.iat[row,index_CO3S]+df3.iat[row,index_CO4S]+df3.iat[row,index_CO5S]
            def detail3():
                name3=[]
                user_input3=st.text_input("Enter The Student Name:","Eg.DEEBAN N")
                name3.append(user_input3)
                deto3=df3.loc[df3['Name'].isin(name3),['Name','Reg No','CO1S','CO2S','CO3S','CO4S','CO5S','Total']]
                if deto3 is not None:
                    st.write(deto3)
                else:
                    st.write("Try Again")
            detail3() 
            threshold3 = st.slider("Threshold For CO1")
            st.write("Threshold Value:",threshold3)
            if st.button('Threshold C01'):
                def thres3():
                    ar3=[]
                    count3=0
                    row=-1
                    df3.iat[row+1, index_CO1S] = df3.iat[row+1,index_CO11] + df3.iat[row+1,index_CO11_1]+df3.iat[row+1,index_CO11_2] 
                    pass_mark3=(threshold3/100)*df3.iat[row+1, index_CO1S]
                    st.write(pass_mark3)
                    for i in range(1,len(df3)):
                        ar3.append(df3['CO1S'].gt(pass_mark3))
                    for j in range(1,len(ar3)+1):
            	        if(df3.iat[j,index_CO1S]>pass_mark3):
            		        st.write(df3.iat[j,index_Name3],df3.iat[j,index_RegNo3],df3.iat[j,index_CO1S])
            		        count3=count3+1
                    st.write("Pass Count:",count3)
                    passper3=(count3/len(df3))*100
                    st.write("Pass Percentage:",passper3)
                thres3()
            threshold4 = st.slider("Threshold For CO2")
            st.write("Threshold Value:",threshold4)
            if st.button('Threshold C02'):
                def thres4():
                    ar4=[]
                    count4=0
                    row=-1
                    df3.iat[row+1, index_CO2S] = df3.iat[row+1,index_CO22] + df3.iat[row+1,index_CO22_1]+df3.iat[row+1,index_CO22_2] 
                    pass_mark4=(threshold4/100)*df3.iat[row+1, index_CO2S]
                    st.write(pass_mark4)
                    for i in range(1,len(df3)):
                        ar4.append(df3['CO2S'].gt(pass_mark4))
                    for j in range(1,len(ar4)+1):
            	        if(df3.iat[j,index_CO2S]>pass_mark4):
            		        st.write(df3.iat[j,index_Name3],df3.iat[j,index_RegNo3],df3.iat[j,index_CO2S])
            		        count4=count4+1
                    st.write("Pass Count:",count4)
                    passper4=(count4/len(df3))*100
                    st.write("Pass Percentage:",passper4)
                thres4() 
            threshold5 = st.slider("Threshold For CO3")
            st.write("Threshold Value:",threshold5)
            if st.button('Threshold C03'):
                def thres5():
                    ar5=[]
                    count5=0
                    row=-1
                    df3.iat[row+1, index_CO3S] = df3.iat[row+1,index_CO33] + df3.iat[row+1,index_CO33_1]+df3.iat[row+1,index_CO33_2] 
                    pass_mark5=(threshold5/100)*df3.iat[row+1, index_CO3S]
                    st.write(pass_mark5)
                    for i in range(1,len(df3)):
                        ar5.append(df3['CO3S'].gt(pass_mark5))
                    for j in range(1,len(ar5)+1):
                        if(df3.iat[j,index_CO3S]>pass_mark5):
                            st.write(df3.iat[j,index_Name3],df3.iat[j,index_RegNo3],df3.iat[j,index_CO3S])
                            count5=count5+1
                    st.write("Pass Count:",count5)
                    passper5=(count5/len(df3))*100
                    st.write("Pass Percentage:",passper5)
                thres5()
            threshold6 = st.slider("Threshold For CO4")
            st.write("Threshold Value:",threshold6)
            if st.button('Threshold C04'):
                def thres6():
                    ar6=[]
                    count6=0
                    row=-1
                    df3.iat[row+1, index_CO4S] = df3.iat[row+1,index_CO44] + df3.iat[row+1,index_CO44_1]+df3.iat[row+1,index_CO44_2] 
                    pass_mark6=(threshold6/100)*df3.iat[row+1, index_CO4S]
                    st.write(pass_mark6)
                    for i in range(1,len(df3)):
                        ar6.append(df3['CO4S'].gt(pass_mark6))
                    for j in range(1,len(ar6)+1):
            	        if(df3.iat[j,index_CO4S]>pass_mark6):
            		        st.write(df3.iat[j,index_Name3],df3.iat[j,index_RegNo3],df3.iat[j,index_CO4S])
            		        count6=count6+1
                    st.write("Pass Count:",count6)
                    passper6=(count6/len(df3))*100
                    st.write("Pass Percentage:",passper6)
                thres6()
            threshold7 = st.slider("Threshold For CO5")
            st.write("Threshold Value:",threshold7)
            if st.button('Threshold C05'):
                def thres7():
                    ar7=[]
                    count7=0
                    row=-1
                    df3.iat[row+1, index_CO5S] = df3.iat[row+1,index_CO55] + df3.iat[row+1,index_CO55_1]+df3.iat[row+1,index_CO55_2] 
                    pass_mark7=(threshold7/100)*df3.iat[row+1, index_CO5S]
                    st.write(pass_mark7)
                    for i in range(1,len(df3)):
                        ar7.append(df3['CO5S'].gt(pass_mark7))
                    for j in range(1,len(ar7)+1):
            	        if(df3.iat[j,index_CO5S]>pass_mark7):
            		        st.write(df3.iat[j,index_Name3],df3.iat[j,index_RegNo3],df3.iat[j,index_CO5S])
            		        count7=count7+1
                    st.write("Pass Count:",count7)
                    passper7=(count7/len(df3))*100
                    st.write("Pass Percentage:",passper7)
                thres7()
                
            
    else:
        print("Thank You")
    
if __name__=='__main__':
    main()

