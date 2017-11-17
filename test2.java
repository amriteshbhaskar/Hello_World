class main_class
{
	public static void main(String[] args)
	{
		test_class tc=new test_class();
		System.out.println(tc.t);
	}
}

class test_class
{
	int t;
	test_class()
	{
		t=2;
	}
}