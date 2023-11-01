package generic.kepco.com;

public class StringTest {
	
	public void test() {
		String a = "test";
		String b = "test";
		String c=a;
		String d= new String("test");
		
		System.out.println(a);
//		Object 클래스에 선언되어 있는 equals()는 ==과 같음 (참조값을 비교함)
		System.out.println(a.equals(c));
		System.out.println(a.equals(b));
		System.out.println(a.equals(d));
		System.out.println(a==b);		
		System.out.println(a==d);
	}

	public static void main(String[] args) {
		new StringTest().test();
	}

}
