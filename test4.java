import java.util.Scanner;
class mncl
{
	public static void main(String[] args)
	{
		Scanner scn=new Scanner(System.in);
		String s=scn.nextLine();
		String[] st = s.split(" ");
		int[] a=new int[st.length];
		for(int i=0;i<st.length;i++)
		{
			a[i]=Integer.parseInt(st[i]);
			System.out.print(a[i]+" ");
		}
	}
}