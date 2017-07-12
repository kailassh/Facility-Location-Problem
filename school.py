print('SCHOOL-MAXIMUM DISTANCE MATRIX')
w,h=18,18
matrix=[[0 for x in range(w)] for y in range(h)]
matrix[0][0]=0
matrix[0][1]=5.8
matrix[0][2]=3.1
matrix[0][3]=4.8
matrix[0][4]=9.1
matrix[0][5]=14.2
matrix[0][6]=9.4
matrix[0][7]=11.1
matrix[0][8]=9.2
matrix[0][9]=10.1
matrix[0][10]=30.3
matrix[0][11]=10.3
matrix[0][12]=16.2
matrix[0][13]=16.6
matrix[0][14]=3.5
matrix[0][15]=23.1
matrix[0][16]=14
matrix[0][17]=21.8

matrix[1][0]=5.8
matrix[1][1]=0
matrix[1][2]=3.9
matrix[1][3]=4.8
matrix[1][4]=4.9
matrix[1][5]=10.2
matrix[1][6]=5.3
matrix[1][7]=11.1
matrix[1][8]=11.2
matrix[1][9]=12.4
matrix[1][10]=20.9
matrix[1][11]=13.9
matrix[1][12]=19
matrix[1][13]=14.8
matrix[1][14]=7.9
matrix[1][15]=30.3
matrix[1][16]=14.5
matrix[1][17]=21.8

matrix[2][0]=3.1
matrix[2][1]=3.9
matrix[2][2]=0
matrix[2][3]=3.5
matrix[2][4]=8.1
matrix[2][5]=13
matrix[2][6]=4.9
matrix[2][7]=11.7
matrix[2][8]=8
matrix[2][9]=13.4
matrix[2][10]=21.1
matrix[2][11]=10
matrix[2][12]=17.3
matrix[2][13]=14.9
matrix[2][14]=4.4
matrix[2][15]=25.6
matrix[2][16]=16.5
matrix[2][17]=22

matrix[3][0]=4.8
matrix[3][1]=4.8
matrix[3][2]=3.5
matrix[3][3]=0
matrix[3][4]=8.5
matrix[3][5]=15.2
matrix[3][6]=4.2
matrix[3][7]=13.8
matrix[3][8]=7.2
matrix[3][9]=14.8
matrix[3][10]=24.6
matrix[3][11]=13.7
matrix[3][12]=15.3
matrix[3][13]=13.4
matrix[3][14]=7.6
matrix[3][15]=26.9
matrix[3][16]=16.5
matrix[3][17]=26.5

matrix[4][0]=9.1
matrix[4][1]=4.9
matrix[4][2]=8.1
matrix[4][3]=8.5
matrix[4][4]=0
matrix[4][5]=6.1
matrix[4][6]=11.4
matrix[4][7]=4
matrix[4][8]=18.5
matrix[4][9]=10.2
matrix[4][10]=9.6
matrix[4][11]=24.1
matrix[4][12]=6.4
matrix[4][13]=16.8
matrix[4][14]=16
matrix[4][15]=40.5
matrix[4][16]=27.5
matrix[4][17]=15.3

matrix[5][0]=14.2
matrix[5][1]=10.2
matrix[5][2]=13
matrix[5][3]=15.2
matrix[5][4]=6.1
matrix[5][5]=0
matrix[5][6]=10.4
matrix[5][7]=10.8
matrix[5][8]=17.6
matrix[5][9]=14.9
matrix[5][10]=14.1
matrix[5][11]=23.9
matrix[5][12]=26.9
matrix[5][13]=15.9
matrix[5][14]=20
matrix[5][15]=45
matrix[5][16]=32
matrix[5][17]=15.9

matrix[6][0]=9.4
matrix[6][1]=5.3
matrix[6][2]=4.9
matrix[6][3]=4.2
matrix[6][4]=11.4
matrix[6][5]=10.4
matrix[6][6]=0
matrix[6][7]=15.1
matrix[6][8]=11.8
matrix[6][9]=17.8
matrix[6][10]=24.1
matrix[6][11]=18.2
matrix[6][12]=19.8
matrix[6][13]=7.5
matrix[6][14]=11.8
matrix[6][15]=29.5
matrix[6][16]=19.5
matrix[6][17]=25.9

matrix[7][0]=11.1
matrix[7][1]=11.1
matrix[7][2]=11.7
matrix[7][3]=13.8
matrix[7][4]=4
matrix[7][5]=10.8
matrix[7][6]=15.1
matrix[7][7]=0
matrix[7][8]=20.6
matrix[7][9]=4.7
matrix[7][10]=6.7
matrix[7][11]=20.1
matrix[7][12]=26.8
matrix[7][13]=22.6
matrix[7][14]=14.4
matrix[7][15]=37.6
matrix[7][16]=24.6
matrix[7][17]=8.6

matrix[8][0]=9.2
matrix[8][1]=11.2
matrix[8][2]=8
matrix[8][3]=7.2
matrix[8][4]=18.5
matrix[8][5]=17.6
matrix[8][6]=11.8
matrix[8][7]=20.6
matrix[8][8]=0
matrix[8][9]=18.8
matrix[8][10]=27.5
matrix[8][11]=14.8
matrix[8][12]=8
matrix[8][13]=14.1
matrix[8][14]=12.8
matrix[8][15]=32.1
matrix[8][16]=20.8
matrix[8][17]=28.4

matrix[9][0]=10.1
matrix[9][1]=12.4
matrix[9][2]=13.4
matrix[9][3]=14.8
matrix[9][4]=10.2
matrix[9][5]=14.9
matrix[9][6]=17.8
matrix[9][7]=4.7
matrix[9][8]=18.8
matrix[9][9]=0
matrix[9][10]=11.1
matrix[9][11]=18.6
matrix[9][12]=28.3
matrix[9][13]=21.7
matrix[9][14]=16.9
matrix[9][15]=26.7
matrix[9][16]=16.4
matrix[9][17]=15.6

matrix[10][0]=30.3
matrix[10][1]=20.9
matrix[10][2]=21.1
matrix[10][3]=24.6
matrix[10][4]=9.6
matrix[10][5]=14.1
matrix[10][6]=24.1
matrix[10][7]=6.7
matrix[10][8]=27.5
matrix[10][9]=11.1
matrix[10][10]=0
matrix[10][11]=32.6
matrix[10][12]=35.5
matrix[10][13]=31.8
matrix[10][14]=32.7
matrix[10][15]=40.6
matrix[10][16]=19.1
matrix[10][17]=4.6

matrix[11][0]=10.3
matrix[11][1]=13.9
matrix[11][2]=10
matrix[11][3]=13.7
matrix[11][4]=24.1
matrix[11][5]=23.9
matrix[11][6]=18.2
matrix[11][7]=20.1
matrix[11][8]=14.8
matrix[11][9]=18.6
matrix[11][10]=32.6
matrix[11][11]=0
matrix[11][12]=17.3
matrix[11][13]=23.5
matrix[11][14]=8.5
matrix[11][15]=13.6
matrix[11][16]=13
matrix[11][17]=33.5

matrix[12][0]=16.2
matrix[12][1]=19
matrix[12][2]=17.3
matrix[12][3]=15.3
matrix[12][4]=6.4
matrix[12][5]=26.9
matrix[12][6]=19.8
matrix[12][7]=26.8
matrix[12][8]=8
matrix[12][9]=28.3
matrix[12][10]=35.5
matrix[12][11]=17.3
matrix[12][12]=0
matrix[12][13]=22
matrix[12][14]=15.6
matrix[12][15]=32.9
matrix[12][16]=24.7
matrix[12][17]=36.6

matrix[13][0]=16.6
matrix[13][1]=14.8
matrix[13][2]=14.9
matrix[13][3]=13.4
matrix[13][4]=16.8
matrix[13][5]=15.9
matrix[13][6]=7.5
matrix[13][7]=22.6
matrix[13][8]=14.1
matrix[13][9]=21.7
matrix[13][10]=31.8
matrix[13][11]=23.5
matrix[13][12]=22
matrix[13][13]=0
matrix[13][14]=14.7
matrix[13][15]=32.9
matrix[13][16]=22.3
matrix[13][17]=24.3

matrix[14][0]=3.5
matrix[14][1]=7.9
matrix[14][2]=4.4
matrix[14][3]=7.6
matrix[14][4]=16
matrix[14][5]=20
matrix[14][6]=11.8
matrix[14][7]=14.4
matrix[14][8]=12.8
matrix[14][9]=16.9
matrix[14][10]=32.7
matrix[14][11]=8.5
matrix[14][12]=15.6
matrix[14][13]=14.7
matrix[14][14]=0
matrix[14][15]=25.4
matrix[14][16]=16.4
matrix[14][17]=33.6

matrix[15][0]=23.1
matrix[15][1]=30.3
matrix[15][2]=25.6
matrix[15][3]=26.9
matrix[15][4]=40.5
matrix[15][5]=45
matrix[15][6]=29.5
matrix[15][7]=37.6
matrix[15][8]=32.1
matrix[15][9]=26.7
matrix[15][10]=40.6
matrix[15][11]=13.6
matrix[15][12]=32.9
matrix[15][13]=32.9
matrix[15][14]=25.4
matrix[15][15]=0
matrix[15][16]=25.3
matrix[15][17]=33.4

matrix[16][0]=14
matrix[16][1]=14.5
matrix[16][2]=16.5
matrix[16][3]=16.5
matrix[16][4]=27.5
matrix[16][5]=32
matrix[16][6]=19.5
matrix[16][7]=24.6
matrix[16][8]=20.8
matrix[16][9]=6.4
matrix[16][10]=19.1
matrix[16][11]=13
matrix[16][12]=24.7
matrix[16][13]=22.3
matrix[16][14]=16.4
matrix[16][15]=25.3
matrix[16][16]=0
matrix[16][17]=23.4

matrix[17][0]=21.8
matrix[17][1]=21.8
matrix[17][2]=22
matrix[17][3]=26.5
matrix[17][4]=15.3
matrix[17][5]=15.9
matrix[17][6]=25.9
matrix[17][7]=8.6
matrix[17][8]=28.4
matrix[17][9]=15.6
matrix[17][10]=4.6
matrix[17][11]=33.5
matrix[17][12]=36.6
matrix[17][13]=24.3
matrix[17][14]=33.6
matrix[17][15]=33.4
matrix[17][16]=23.4
matrix[17][17]=0

class result1:
    def __init__(self):
        self.sum=0
        self.sum1=0
        self.avg=0
        self.minintra=0
        self.maxinter=0
        self.dunn=0
    def cluster0(self):
        self.sum=matrix[6][5]+matrix[6][0]+matrix[6][13]+matrix[6][4]+matrix[6][1]+matrix[6][8]+matrix[6][3]+matrix[6][2]
        self.sum1=matrix[6][10]+matrix[6][17]+matrix[6][9]+matrix[6][7]+matrix[6][11]+matrix[6][15]+matrix[6][16]+matrix[6][14]+matrix[6][12]
        self.minintra=min([matrix[6][5],matrix[6][0],matrix[6][13],matrix[6][4],matrix[6][1],matrix[6][8],matrix[6][3],matrix[6][2]])
        self.maxinter=max([matrix[6][10],matrix[6][17],matrix[6][9],matrix[6][7],matrix[6][11],matrix[6][15],matrix[6][16],matrix[6][14],matrix[6][12]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/8
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
    def cluster1(self):
        self.sum=matrix[10][17]+matrix[10][9]+matrix[10][7]
        self.sum1=matrix[10][6]+matrix[10][5]+matrix[10][0]+matrix[10][13]+matrix[10][4]+matrix[10][1]+matrix[10][8]+matrix[10][3]+matrix[10][2]+matrix[10][11]+matrix[10][15]+matrix[10][16]+matrix[10][14]+matrix[10][12]
        self.minintra=min([matrix[10][17],matrix[10][9],matrix[10][7]])
        self.maxinter=max([matrix[10][6],matrix[10][5],matrix[10][0],matrix[10][13],matrix[10][4],matrix[10][1],matrix[10][8],matrix[10][3],matrix[10][2],matrix[10][11],matrix[10][15],matrix[10][16],matrix[10][14],matrix[10][12]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/3
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
    def cluster2(self):
        self.sum=matrix[11][15]+matrix[11][12]+matrix[11][16]+matrix[11][14]
        self.sum1=matrix[11][6]+matrix[11][5]+matrix[11][0]+matrix[11][13]+matrix[11][4]+matrix[11][1]+matrix[11][8]+matrix[11][3]+matrix[11][2]+matrix[11][10]+matrix[11][17]+matrix[11][9]+matrix[11][7]
        self.minintra=min([matrix[11][15]+matrix[11][12]+matrix[11][16]+matrix[11][14]])
        self.maxinter=max([matrix[11][6],matrix[11][5],matrix[11][0],matrix[11][13],matrix[11][4],matrix[11][1],matrix[11][8],matrix[11][3],matrix[11][2],matrix[11][10],matrix[11][17],matrix[11][9],matrix[11][7]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/4
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
        
class result2:
    def __init__(self):
        self.sum=0
        self.sum1=0
        self.avg=0
        self.minintra=0
        self.maxinter=0
        self.dunn=0
    def cluster0(self):
        self.sum=matrix[2][0]+matrix[2][16]+matrix[2][9]+matrix[2][14]+matrix[2][12]+matrix[2][1]+matrix[2][8]+matrix[2][3]
        self.sum1=matrix[2][6]+matrix[2][5]+matrix[2][17]+matrix[2][13]+matrix[2][4]+matrix[2][10]+matrix[2][7]+matrix[2][15]+matrix[2][11]
        self.minintra=min([matrix[2][0]+matrix[2][16]+matrix[2][9]+matrix[2][14]+matrix[2][12]+matrix[2][1]+matrix[2][8]+matrix[2][3]])
        self.maxinter=max([matrix[2][6],matrix[2][5],matrix[2][17],matrix[2][13],matrix[2][4],matrix[2][10],matrix[2][7],matrix[2][15],matrix[2][11]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/8
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
    def cluster1(self):
        self.sum=matrix[6][5]+matrix[6][17]+matrix[6][13]+matrix[6][4]+matrix[6][10]+matrix[6][7]
        self.sum1=matrix[6][2]+matrix[6][0]+matrix[6][16]+matrix[6][9]+matrix[6][14]+matrix[6][12]+matrix[6][1]+matrix[6][8]+matrix[6][3]+matrix[6][15]+matrix[6][11]
        self.minintra=min([matrix[6][5]+matrix[6][17]+matrix[6][13]+matrix[6][4]+matrix[6][10]+matrix[6][7]])
        self.maxinter=max([matrix[6][2],matrix[6][0],matrix[6][16],matrix[6][9],matrix[6][14],matrix[6][12],matrix[6][1],matrix[6][8],matrix[6][3],matrix[6][15],matrix[6][11]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/6
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
    def cluster2(self):
        self.sum=matrix[15][11]
        self.sum1=matrix[15][2]+matrix[15][0]+matrix[15][16]+matrix[15][9]+matrix[15][14]+matrix[15][12]+matrix[15][1]+matrix[15][8]+matrix[15][3]+matrix[15][6]+matrix[15][5]+matrix[15][17]+matrix[15][13]+matrix[15][4]+matrix[15][10]+matrix[15][7]
        self.minintra=matrix[15][11]
        self.maxinter=max([matrix[15][2],matrix[15][0],matrix[15][16],matrix[15][9],matrix[15][14],matrix[15][12],matrix[15][1],matrix[15][8],matrix[15][3],matrix[15][6],matrix[15][5],matrix[15][17],matrix[15][13],matrix[15][4],matrix[15][10],matrix[15][7]])                                                                                                                                                                                                                                            
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/1
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
class result3:
    def __init__(self):
        self.sum=0
        self.sum1=0
        self.avg=0
        self.minintra=0
        self.maxinter=0
        self.dunn=0
    def cluster0(self):
        self.sum=matrix[11][16]+matrix[11][12]
        self.sum1=matrix[11][6]+matrix[11][5]+matrix[11][0]+matrix[11][17]+matrix[11][9]+matrix[11][13]+matrix[11][4]+matrix[11][10]+matrix[11][1]+matrix[11][8]+matrix[11][3]+matrix[11][2]+matrix[11][7]+matrix[11][15]
        self.minintra=min([matrix[11][16]+matrix[11][12]])
        self.maxinter=max([matrix[11][6],matrix[11][5],matrix[11][0],matrix[11][17],matrix[11][9],matrix[11][13],matrix[11][4],matrix[11][10],matrix[11][1],matrix[11][8],matrix[11][3],matrix[11][2],matrix[11][7],matrix[11][15]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/2
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
    def cluster1(self):
        self.sum=matrix[6][5]+matrix[6][0]+matrix[6][17]+matrix[6][9]+matrix[6][13]+matrix[6][4]+matrix[6][10]+matrix[6][1]+matrix[6][8]+matrix[6][3]+matrix[6][2]+matrix[6][7]
        self.sum1=matrix[6][11]+matrix[6][16]+matrix[6][14]+matrix[6][12]+matrix[6][15]
        self.minintra=min([matrix[6][5]+matrix[6][0]+matrix[6][17]+matrix[6][9]+matrix[6][13]+matrix[6][4]+matrix[6][10]+matrix[6][1]+matrix[6][8]+matrix[6][3]+matrix[6][2]+matrix[6][7]])
        self.maxinter=max([matrix[6][11],matrix[6][16],matrix[6][14],matrix[6][12],matrix[6][15]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/12
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
    def cluster2(self):
        self.sum=matrix[15][15]
        self.sum1=matrix[15][11]+matrix[15][16]+matrix[15][14]+matrix[15][12]+matrix[15][6]+matrix[15][5]+matrix[15][0]+matrix[15][17]+matrix[15][9]+matrix[15][13]+matrix[15][4]+matrix[15][10]+matrix[15][1]+matrix[15][8]+matrix[15][3]+matrix[15][2]+matrix[15][7]
        self.minintra=matrix[15][15]
        self.maxinter=max([matrix[15][11],matrix[15][16],matrix[15][14],matrix[15][12],matrix[15][6],matrix[15][5],matrix[15][0],matrix[15][17],matrix[15][9],matrix[15][13],matrix[15][4],matrix[15][10],matrix[15][1],matrix[15][8],matrix[15][3],matrix[15][2],matrix[15][7]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/1
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
class result4:
    def __init__(self):
        self.sum=0
        self.sum1=0
        self.avg=0
        self.minintra=0
        self.maxinter=0
        self.dunn=0
    def cluster0(self):
        self.sum=matrix[11][15]+matrix[11][12]+matrix[11][16]+matrix[11][14]
        self.sum1=matrix[11][6]+matrix[11][5]+matrix[11][0]+matrix[11][13]+matrix[11][4]+matrix[11][1]+matrix[11][8]+matrix[11][3]+matrix[11][2]+matrix[11][17]+matrix[11][9]+matrix[11][10]+matrix[11][7]
        self.minintra=min([matrix[11][15]+matrix[11][12]+matrix[11][16]+matrix[11][14]])
        self.maxinter=max([matrix[11][6],matrix[11][5],matrix[11][0],matrix[11][13],matrix[11][4],matrix[11][1],matrix[11][8],matrix[11][3],matrix[11][2],matrix[11][17],matrix[11][9],matrix[11][10],matrix[11][7]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/4
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
    def cluster1(self):
        self.sum=matrix[6][0]+matrix[6][5]+matrix[6][13]+matrix[6][4]+matrix[6][1]+matrix[6][8]+matrix[6][3]+matrix[6][2]
        self.sum1=matrix[6][11]+matrix[6][15]+matrix[6][16]+matrix[6][14]+matrix[6][12]+matrix[6][17]+matrix[6][9]+matrix[6][10]+matrix[6][7]
        self.minintra=min([matrix[6][0]+matrix[6][5]+matrix[6][13]+matrix[6][4]+matrix[6][1]+matrix[6][8]+matrix[6][3]+matrix[6][2]])
        self.maxinter=max([matrix[6][11],matrix[6][15],matrix[6][16],matrix[6][14],matrix[6][12],matrix[6][17],matrix[6][9],matrix[6][10],matrix[6][7]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/8
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
    def cluster2(self):
        self.sum=matrix[17][9]+matrix[17][10]+matrix[17][7]
        self.sum1=matrix[17][11]+matrix[17][15]+matrix[17][16]+matrix[17][14]+matrix[17][12]+matrix[17][6]+matrix[17][5]+matrix[17][0]+matrix[17][13]+matrix[17][4]+matrix[17][1]+matrix[17][8]+matrix[17][3]+matrix[17][2]
        self.minintra=min([matrix[17][9]+matrix[17][10]+matrix[17][7]])
        self.maxinter=max([matrix[17][11],matrix[17][15],matrix[17][16],matrix[17][14],matrix[17][12],matrix[17][6],matrix[17][5],matrix[17][0],matrix[17][13],matrix[17][4],matrix[17][1],matrix[17][8],matrix[17][3],matrix[17][2]])
        self.dunn=self.minintra/self.maxinter
        self.avg=self.sum/3
        return (self.sum,self.avg,self.minintra,self.maxinter,self.dunn,self.sum1)
r1=result1()
totsum1=r1.cluster0()[0]+r1.cluster1()[0]+r1.cluster2()[0]
totsum11=r1.cluster0()[5]+r1.cluster1()[5]+r1.cluster2()[5]
print('SET 1 INTRA-CLUSTER COST:',totsum1)
print('SET 1 INTER-CLUSTER COST:',totsum11)
res1=max([(r1.cluster0()[1]+r1.cluster1()[1])/24.1,(r1.cluster1()[1]+r1.cluster2()[1])/32.6,(r1.cluster2()[1]+r1.cluster0()[1])/18.2])
print('SET 1 DB INDEX:',res1)
res11=r1.cluster0()[4]+r1.cluster1()[4]+r1.cluster2()[4]
print('SET 1 DUNN INDEX:',res11)
r2=result2()
totsum2=r2.cluster0()[0]+r2.cluster1()[0]+r2.cluster2()[0]
totsum22=r2.cluster0()[5]+r2.cluster1()[5]+r2.cluster2()[5]
print('SET 2 INTRA-CLUSTER COST:',totsum2)
print('SET 2 INTER-CLUSTER COST:',totsum22)
res2=max([(r2.cluster0()[1]+r2.cluster1()[1])/4.9,(r2.cluster1()[1]+r2.cluster2()[1])/29.5,(r2.cluster2()[1]+r2.cluster0()[1])/25.6])
print('SET 2 DB INDEX:',res2)
res22=r2.cluster0()[4]+r2.cluster1()[4]+r2.cluster2()[4]
print('SET 2 DUNN INDEX:',res22)
r3=result3()
totsum3=r3.cluster0()[0]+r3.cluster1()[0]+r3.cluster2()[0]
totsum33=r3.cluster0()[5]+r3.cluster1()[5]+r3.cluster2()[5]
print('SET 3 INTRA-CLUSTER COST:',totsum3)
print('SET 3 INTER-CLUSTER COST:',totsum33)
res3=max([(r3.cluster0()[1]+r3.cluster1()[1])/18.2,(r3.cluster1()[1]+r3.cluster2()[1])/29.5,(r3.cluster2()[1]+r3.cluster0()[1])/13.6])
print('SET 3 DB INDEX:',res3)
res33=r3.cluster0()[4]+r3.cluster1()[4]+r3.cluster2()[4]
print('SET 3 DUNN INDEX:',res33)
r4=result4()
totsum4=r4.cluster0()[0]+r4.cluster1()[0]+r4.cluster2()[0]
totsum44=r4.cluster0()[5]+r4.cluster1()[5]+r4.cluster2()[5]
print('SET 4 INTRA-CLUSTER COST:',totsum4)
print('SET 4 INTER-CLUSTER COST:',totsum44)
res4=max([(r4.cluster0()[1]+r4.cluster1()[1])/18.2,(r4.cluster1()[1]+r4.cluster2()[1])/25.9,(r4.cluster2()[1]+r4.cluster0()[1])/33.5])
print('SET 4 DB INDEX:',res4)
res44=r4.cluster0()[4]+r4.cluster1()[4]+r4.cluster2()[4]
print('SET 4 DUNN INDEX:',res44)








