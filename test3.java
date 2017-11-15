import java.util.Scanner;



class main_class extends second
{
	
	public static void main(String[] args)
	{
		second f = new second();
		Scanner a=new Scanner(System.in);
		System.out.println(a.nextLine()+f.h);
		f.hello();
	}
}

class first
{
	public static int h=1;
	public void hello()
	{
		System.out.println("Hello");
	}
}

class second extends first
{
	public void hello()
	{
		System.out.println("Wow");
	}
}