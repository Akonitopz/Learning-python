#include <stdio.h>
#include <math.h>
#define pi 3.1416

int main()
{
	float area,length,width,hypotenuse, perim,rad,a,b,side;
	int choice;
	
	
	printf("This Program can perform various task according to your choice.");
	printf("\n Select tasks you want to perform below.");
	printf("\n\nAvailable tasks: \n1. Compute the area and perimeter of a right triangle \n2. Compute the area and perimeter of a rectangle. \n3. Compute the area and perimeter of a square.  \n4. Compute the area and circumference of a circle.");
	printf("\n\nChosen Task {1-4}->");
	scanf("%1d",&choice);
	
	if (choice==1){
		
		do{
		
     	printf("input your leg a:");
		   scanf("%f",&a);
		printf("input your leg b:");
	       scanf("%f",&b); 
	            
			    area = 0.5 * a * b;
				hypotenuse = sqrt((a*a)+(b*b)); 
		        perim = a + b + hypotenuse;
		printf("\nThe Area of a right trangle is: %f ",area);	
    	printf("\nThe Perimeter of a right trangle is: %.2f ",perim);
    
		printf("\n\nDo you want to repeat this operation?");
		printf("\nPress (1) to repeat and any NUMBER to close: "); 
	            scanf("%1d",&choice);
		       }   
        while(choice==1);    		
	}
    	
  	else if(choice==2){
	  do{
	  
		printf("input your length:");
		   scanf("%f",&length);
		printf("input your width:");
	       scanf("%f",&width);
		        
				area = width*length;
				perim = (width + length)*2;	
		printf("\nThe Area of a rectangle is: %f ",area);	
    	printf("\nThe Perimeter of a rectangle is: %.2f ",perim);
		printf("\n\nDo you want to repeat this operation?");
		printf("\nPress (1) to repeat and any NUMBER to close: "); 
	            scanf("%1d",&choice);
		       }   
        while(choice==1);   		
    }
    	
	else if(choice==3){
	do{
	
		printf("Input the measurement of your side:");
		   scanf("%f",&side);
	
		        
				area = pow(side,2);
				perim = 4*side;	
		printf("\nThe Area of a Square is: %f ",area);	
    	printf("\nThe Perimeter of a Square is: %.2f ",perim);
		
	    printf("\n\nDo you want to repeat this operation?");
		printf("\nPress (1) to repeat and any NUMBER to close: "); 
	            scanf("%1d",&choice);
		       }   
        while(choice==1);        				
				
				 }
	else if(choice==4){
			do{
	 
		   	printf("input your radius:");
		   scanf("%f",&rad);
	
				area = pi*(rad*rad);	
		        perim = (rad*pi)*2;	
		printf("\nThe Area of a circle is: %f ",area);	
    	printf("\nThe Circumference of a circle is: %.2f ",perim);
	   	
		   printf("\n\nDo you want to repeat this operation?");
		printf("\nPress (1) to repeat and any NUMBER to close: "); 
	            scanf("%1d",&choice);
		       }   
        while(choice==1);
		
	 }
    else{

	     printf("\nINVALID CHOICE!!! please choose number from 1-4 only."); 

 
   }
 
         printf("\nThankYou for using this program! Have a good day."); 
}