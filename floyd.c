#include <stdio.h>
#include <stdlib.h>
#define MAX 10

int main()
{
	//set A
	int na,no,i,d,c,j,k;
	int a[MAX],mat[MAX][MAX];
	for(i=0;i<MAX;i++)
	{
		for(j=0;j<MAX;j++)
			mat[i][j]=0;
	}
	printf("How many elements are in set?\n");
    scanf("%d",&na);
    printf("\nEnter elements of set A\n");
	 for(i=0;i<na;++i)
        scanf("%d",&a[i]);

    printf("Elements of set are :");
    for(i=0;i<na;++i)
        printf("%d ",a[i]);

	printf("\nEnter the number of ordered pairs :\n");
	scanf("%d",&no);
	
	printf("\nEnter the ordered pairs :\n");
	for(i=0;i<no;i++)
	{
		scanf("%d,%d",&d,&c);
		mat[d][c]=1;
	}
	
	for(i=0;i<na;i++)
	{
		for(j=0;j<na;j++)
			mat[i][j]=mat[a[i]][a[j]];	
	}
	
	printf("matrix is\n");
	for(i=0;i<na;i++)
	{
		for(j=0;j<na;j++)
			printf("%d ",mat[i][j]);
		printf("\n");
	}
	
	for(k=0;k<na;k++) //Floyd's Algorithm.
 	 for(i=0;i<na;i++)
  	  for(j=0;j<na;j++)
		if((mat[i][k] + mat[k][j]) < mat[i][j])
            mat[i][j] = mat[i][k] + mat[k][j];


	printf("Shortest paths\n { ");
	for(i=0;i<na;i++)
	{
		for(j=0;j<na;j++)
			if(mat[i][j]==1 && mat[a[i]][a[j]]!=1 && i!=j) 
			{
				printf("(%d,%d),",a[i],a[j]);
			}
	}
	printf("}");
}
