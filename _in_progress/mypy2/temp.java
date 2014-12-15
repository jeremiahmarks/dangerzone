import java.util.Scanner;
public class temp{
public static void main(String[] args)
{
	Scanner scan = new Scanner(System.in);
	double[] tempereture = new double[5];

// populate the temperature array

	for(int i=0; i < tempereture.length ; i++)
		tempereture[i] = scan.nextDouble();

	// find the heighest temperature

	int maxIndex = 0;
	int lowIndex=0;
	int freezing=0;
	double average=0;
	for(int i=0; i < tempereture.length ; i++)
	{
		if(tempereture[i] > tempereture[maxIndex])
			maxIndex = i;
		if(tempereture[i]<tempereture[lowIndex])
			lowIndex=i;
		average+=(tempereture[i]/tempereture.length);
		if(tempereture[i]<=0)
			freezing++;

	}
	System.out.println("heighest temperature is " + tempereture[maxIndex] +"lowest: " + tempereture[lowIndex]+
		"Average: "+average);
	System.out.println("Days above zero: "+(tempereture.length-freezing)+"\nDays Freezing: "+freezing);
}
}

