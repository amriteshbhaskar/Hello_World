import java.util.Scanner;
class myclass
{
	static int fact(int n)
	{
		if(n==1 || n==0)
			return 1;
		else
			return fact(n-1)*n;
	}


	public static void main(String[] args)
	{
		c_2 o=new c_2();
		System.out.println("Hello World");
		Scanner n=new Scanner(System.in);
		System.out.println(fact(n.nextInt()));
		o.print();
    }
}


class c_1
{
	static void print()
	{
		System.out.println("\nIt works11111");
	}
}

class c_2 extends c_1
{
	static String h;
	c_2()
	{
		h="hello";
		System.out.println("Hello");
	}
}
