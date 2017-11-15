import java.util.Scanner;
class mainclass
{
	public static int GCD(int a,int b)
	{
		if(b==0)
			return a;
		else
			return GCD(b,a%b);
	}


	public static void main(String[] args)
	{
		Scanner a=new Scanner(System.in);
		int x=a.nextInt();
		int y=a.nextInt();
		System.out.println(GCD(x,y));
	}
}