print('POLICE STATION-AVERAGE DISTANCE MATRIX')
w,h=18,18
matrix=[[0 for x in range(w)] for y in range(h)]
matrix[0][0]=0
matrix[0][1]=5.35
matrix[0][2]=2.85
matrix[0][3]=4.75
matrix[0][4]=8.75
matrix[0][5]=13.55
matrix[0][6]=7.9
matrix[0][7]=10.9
matrix[0][8]=8.7
matrix[0][9]=9.45
matrix[0][10]=23.55
matrix[0][11]=9.05
matrix[0][12]=15.65
matrix[0][13]=15.1
matrix[0][14]=3.15
matrix[0][15]=21.15
matrix[0][16]=11.1
matrix[0][17]=20.25

matrix[1][0]=5.35
matrix[1][1]=0
matrix[1][2]=3.55
matrix[1][3]=4.45
matrix[1][4]=4.45
matrix[1][5]=9.15
matrix[1][6]=5.1
matrix[1][7]=9.75
matrix[1][8]=10.6
matrix[1][9]=11.3
matrix[1][10]=17.7
matrix[1][11]=13.4
matrix[1][12]=18.05
matrix[1][13]=13.45
matrix[1][14]=7.65
matrix[1][15]=27.1
matrix[1][16]=13.85
matrix[1][17]=19.3

matrix[2][0]=2.85
matrix[2][1]=3.55
matrix[2][2]=0
matrix[2][3]=3.15
matrix[2][4]=7.6
matrix[2][5]=12.15
matrix[2][6]=4.9
matrix[2][7]=10.7
matrix[2][8]=7.15
matrix[2][9]=11.95
matrix[2][10]=18.85
matrix[2][11]=9.9
matrix[2][12]=15.6
matrix[2][13]=13.5
matrix[2][14]=4.35
matrix[2][15]=23.65
matrix[2][16]=13.9
matrix[2][17]=20.2

matrix[3][0]=4.75
matrix[3][1]=4.45
matrix[3][2]=3.15
matrix[3][3]=0
matrix[3][4]=8.05
matrix[3][5]=13.45
matrix[3][6]=4.05
matrix[3][7]=13.15
matrix[3][8]=7
matrix[3][9]=13.65
matrix[3][10]=21.55
matrix[3][11]=12.65
matrix[3][12]=14.25
matrix[3][13]=12.25
matrix[3][14]=6.8
matrix[3][15]=24.95
matrix[3][16]=14.9
matrix[3][17]=23.45

matrix[4][0]=8.75
matrix[4][1]=4.45
matrix[4][2]=7.6
matrix[4][3]=8.05
matrix[4][4]=0
matrix[4][5]=5.45
matrix[4][6]=9.8
matrix[4][7]=4
matrix[4][8]=16.6
matrix[4][9]=8.65
matrix[4][10]=9.6
matrix[4][11]=22
matrix[4][12]=6.4
matrix[4][13]=16.
matrix[4][14]=15.15
matrix[4][15]=34.75
matrix[4][16]=22.45
matrix[4][17]=13.4

matrix[5][0]=13.55
matrix[5][1]=9.15
matrix[5][2]=12.15
matrix[5][3]=13.45
matrix[5][4]=5.45
matrix[5][5]=0
matrix[5][6]=9.5
matrix[5][7]=9.4
matrix[5][8]=16.35
matrix[5][9]=13
matrix[5][10]=13.65
matrix[5][11]=21.85
matrix[5][12]=24.95
matrix[5][13]=14
matrix[5][14]=17.95
matrix[5][15]=38.95
matrix[5][16]=25.8
matrix[5][17]=15.9

matrix[6][0]=7.9
matrix[6][1]=5.1
matrix[6][2]=4.9
matrix[6][3]=4.05
matrix[6][4]=9.8
matrix[6][5]=9.5
matrix[6][6]=0
matrix[6][7]=14.2
matrix[6][8]=9.9
matrix[6][9]=16.45
matrix[6][10]=21.75
matrix[6][11]=17.25
matrix[6][12]=17.85
matrix[6][13]=7.5
matrix[6][14]=11
matrix[6][15]=27.6
matrix[6][16]=17.7
matrix[6][17]=23.75

matrix[7][0]=10.9
matrix[7][1]=9.75
matrix[7][2]=10.7
matrix[7][3]=13.15
matrix[7][4]=4
matrix[7][5]=9.4
matrix[7][6]=14.2
matrix[7][7]=0
matrix[7][8]=18.7
matrix[7][9]=4.7
matrix[7][10]=6.7
matrix[7][11]=19.7
matrix[7][12]=25.25
matrix[7][13]=20.8
matrix[7][14]=14.4
matrix[7][15]=32.49
matrix[7][16]=18.90
matrix[7][17]=8.6

matrix[8][0]=8.7
matrix[8][1]=10.6
matrix[8][2]=7.15
matrix[8][3]=7
matrix[8][4]=16.6
matrix[8][5]=16.35
matrix[8][6]=9.9
matrix[8][7]=18.7
matrix[8][8]=0
matrix[8][9]=17.8
matrix[8][10]=25.2
matrix[8][11]=14.2
matrix[8][12]=8.0
matrix[8][13]=13.2
matrix[8][14]=10.7
matrix[8][15]=29.7
matrix[8][16]=19.2
matrix[8][17]=26.6

matrix[9][0]=9.45
matrix[9][1]=11.3
matrix[9][2]=11.95
matrix[9][3]=13.65
matrix[9][4]=8.65
matrix[9][5]=13
matrix[9][6]=16.45
matrix[9][7]=4.7
matrix[9][8]=17.8
matrix[9][9]=0
matrix[9][10]=10.2
matrix[9][11]=17.65
matrix[9][12]=26.4
matrix[9][13]=21.45
matrix[9][14]=14.65
matrix[9][15]=25.3
matrix[9][16]=12.45
matrix[9][17]=13.8

matrix[10][0]=23.55
matrix[10][1]=17.7
matrix[10][2]=18.85
matrix[10][3]=21.55
matrix[10][4]=9.6
matrix[10][5]=13.65
matrix[10][6]=21.75
matrix[10][7]=6.7
matrix[10][8]=25.2
matrix[10][9]=10.2
matrix[10][10]=0
matrix[10][11]=28.4
matrix[10][12]=32.55
matrix[10][13]=28.35
matrix[10][14]=26.5
matrix[10][15]=36.35
matrix[10][16]=18.3
matrix[10][17]=4.15

matrix[11][0]=9.05
matrix[11][1]=13.4
matrix[11][2]=9.9
matrix[11][3]=12.65
matrix[11][4]=22
matrix[11][5]=21.85
matrix[11][6]=17.25
matrix[11][7]=19.7
matrix[11][8]=14.2
matrix[11][9]=17.65
matrix[11][10]=28.4
matrix[11][11]=0
matrix[11][12]=15.6
matrix[11][13]=22.35
matrix[11][14]=7.8
matrix[11][15]=13.6
matrix[11][16]=12.1
matrix[11][17]=30.15

matrix[12][0]=15.85
matrix[12][1]=18.05
matrix[12][2]=15.6
matrix[12][3]=14.25
matrix[12][4]=6.4
matrix[12][5]=24.95
matrix[12][6]=17.85
matrix[12][7]=25.25
matrix[12][8]=8
matrix[12][9]=26.4
matrix[12][10]=32.55
matrix[12][11]=15.6
matrix[12][12]=0
matrix[12][13]=20.7
matrix[12][14]=14.55
matrix[12][15]=29.65
matrix[12][16]=23.2
matrix[12][17]=34.7

matrix[13][0]=15.1
matrix[13][1]=13.45
matrix[13][2]=13.5
matrix[13][3]=12.25
matrix[13][4]=16.1
matrix[13][5]=14
matrix[13][6]=7.5
matrix[13][7]=20.8
matrix[13][8]=13.2
matrix[13][9]=21.45
matrix[13][10]=28.35
matrix[13][11]=22.35
matrix[13][12]=20.7
matrix[13][13]=0
matrix[13][14]=14.15
matrix[13][15]=30.95
matrix[13][16]=20.45
matrix[13][17]=24.05

matrix[14][0]=3.15
matrix[14][1]=7.65
matrix[14][2]=4.35
matrix[14][3]=6.8
matrix[14][4]=15.15
matrix[14][5]=17.95
matrix[14][6]=11
matrix[14][7]=14.4
matrix[14][8]=10.7
matrix[14][9]=14.65
matrix[14][10]=26.5
matrix[14][11]=7.8
matrix[14][12]=14.55
matrix[14][13]=14.15
matrix[14][14]=0
matrix[14][15]=22.85
matrix[14][16]=13.75
matrix[14][17]=28.15

matrix[15][0]=21.15
matrix[15][1]=27.1
matrix[15][2]=23.65
matrix[15][3]=24.95
matrix[15][4]=34.75
matrix[15][5]=38.95
matrix[15][6]=27.6
matrix[15][7]=32.49
matrix[15][8]=29.7
matrix[15][9]=25.3
matrix[15][10]=36.35
matrix[15][11]=13.6
matrix[15][12]=29.65
matrix[15][13]=30.95
matrix[15][14]=22.85
matrix[15][15]=0
matrix[15][16]=21.8
matrix[15][17]=33.4

matrix[16][0]=11.1
matrix[16][1]=13.85
matrix[16][2]=13.9
matrix[16][3]=134.9
matrix[16][4]=22.45
matrix[16][5]=25.8
matrix[16][6]=17.7
matrix[16][7]=18.9
matrix[16][8]=19.2
matrix[16][9]=12.45
matrix[16][10]=18.3
matrix[16][11]=11.1
matrix[16][12]=23.2
matrix[16][13]=20.45
matrix[16][14]=13.75
matrix[16][15]=21.8
matrix[16][16]=0
matrix[16][17]=21.7

matrix[17][0]=20.25
matrix[17][1]=19.3
matrix[17][2]=20.2
matrix[17][3]=23.45
matrix[17][4]=13.5
matrix[17][5]=15.9
matrix[17][6]=23.75
matrix[17][7]=8.6
matrix[17][8]=26.6
matrix[17][9]=13.8
matrix[17][10]=4.15
matrix[17][11]=30.15
matrix[17][12]=34.7
matrix[17][13]=24.05
matrix[17][14]=28.15
matrix[17][15]=33.4
matrix[17][16]=21.7
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
