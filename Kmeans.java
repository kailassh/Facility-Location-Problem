package cluster;

class KMeans
{
	 int min;  static int k=0,k1=0,k2=0;
	 public static double Eu(double x,double y,double x1,double y1)
	 {
		double x2=x-x1;
		double y2=y-y1;
		double a=(x2*x2)+(y2*y2);
		return Math.sqrt(a);
	 }
	 public static int min(double a,double b,double c)
	 {
		 double min1=a;
		 if(b<min1)
		  min1=b;
		 if(c<min1)
		 min1=c;
		 if(min1==a)
			 return 1;
		 if(min1==b)
			 return 2;
		 if(min1==c)
			 return 3;
		 return 0;
	 }
    public static void main(String[] args)
    {
    	double SAMPLES[][] = new double[][] {{1089,7690}, 
            {1107,7700}, 
            {1099,7695}, 
            {1094,7693}, 
            {1106,7708}, 
            {1095,7700}, 
            {1099,7703},
            {1108,7694},
            {1104,7700},
            {1104,7707},
            {1099,7693},
            {1098,7684},
            {1102,7696},
            {1104,7694},
            {1102,7689},
            {1102,7694},
            {1101,7694},
            {1103,7702}};
    	    double ob1x=1094,ob1y=7693;
    	    double ob2x=1104,ob2y=7694;
    	    double ob3x=1106,ob3y=7708;
    	    double a2[][]=new double[15][10];
    	    double a3[][]=new double[15][10];
    	    double a4[][]=new double[15][10];
    	    System.out.println("INITIAL CENTROIDS:");
    	    a2[k][0]=ob1x;
    		a2[k][1]=ob1y;
    	     k++;
    		a3[k1][0]=ob2x;
    		a3[k1][1]=ob2y;
    		k1++;
    		a4[k2][0]=ob3x;
    		a4[k2][1]=ob3y;
    		k2++;
    		System.out.print("{"+a2[0][0]+","+a2[0][1]+"}");
	        System.out.println();
	        System.out.print("{"+a3[0][0]+","+a3[0][1]+"}");
	        System.out.println();
	        System.out.print("{"+a4[0][0]+","+a4[0][1]+"}");
	        System.out.println();
    	   int m;
    	    for(int i=0;i<18;i++)
    	    {
    	    	m=0;
    	    	double dis1=Eu(ob1x,ob1y,SAMPLES[i][0],SAMPLES[i][1]);
    	    	double dis2=Eu(ob2x,ob2y,SAMPLES[i][0],SAMPLES[i][1]);
    	    	double dis3=Eu(ob3x,ob3y,SAMPLES[i][0],SAMPLES[i][1]);
    	    	if(dis1>0&&dis2>0&&dis3>0)
    	    	m=min(dis1,dis2,dis3);
    	    	if(m==1)
    	    	{
    	    		a2[k][0]=SAMPLES[i][0];
    	    		a2[k][1]=SAMPLES[i][1];
    	    		k++;
    	    	}
    	    	if(m==2)
    	    	{
    	    		a3[k1][0]=SAMPLES[i][0];
    	    		a3[k1][1]=SAMPLES[i][1];
    	    		k1++;
    	    	}
    	    	if(m==3)
    	    	{
    	    		a4[k2][0]=SAMPLES[i][0];
    	    		a4[k2][1]=SAMPLES[i][1];
    	    		k2++;
    	    	}
    	     }
    	    float sumx=0.0f;float sumy=0.0f;
    	    float sum1x=0.0f;float sum1y=0.0f;
    	    float sum2x=0.0f;float sum2y=0.0f;
    	    if(k>0)
    	    {
    	    	System.out.println("CLUSTER-1");
    	    	for(int i=0;i<k;i++)
    	    	{
    	    		System.out.print("{"+a2[i][0]+","+a2[i][1]+"}");
    	    		System.out.println();
    	    	     sumx+=a2[i][0];
    	    	     sumy+=a2[i][1];
    	    	}
    	    }
    	    if(k1>0)
    	    {
    	     System.out.println("CLUSTER-2");
    	    	for(int i=0;i<k1;i++)
    	    	{
    	    		System.out.print("{"+a3[i][0]+","+a3[i][1]+"}");
    	    		System.out.println();
    	    		sum1x+=a3[i][0];
   	    	        sum1y+=a3[i][1];
    	    	}
    	    }
    	    if(k2>0)
    	    {
    	    	System.out.println("CLUSTER-3");
    	    	for(int i=0;i<k2;i++)
    	    	{
    	    		System.out.print("{"+a4[i][0]+","+a4[i][1]+"}");
    	    		System.out.println();
    	    		sum2x+=a4[i][0];
   	    	        sum2y+=a4[i][1];
    	    	}
    	    }
    	    System.out.println("FINAL CENTROIDS:");
    	    System.out.print("{"+sumx/k+","+sum1y/k+"}");
    		System.out.println();
    		System.out.print("{"+sum1x/k1+","+sum1y/k1+"}");
    		System.out.println();
    		System.out.print("{"+sum2x/k2+","+sum2y/k2+"}");
    		System.out.println();
    }
}