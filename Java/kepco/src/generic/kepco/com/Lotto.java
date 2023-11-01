package generic.kepco.com;

import java.util.Random;

public class Lotto {
	private Random rd =null;
	private int[] lotto = new int[6];
	
	public void makeLotto() {
		rd = new Random();
		lotto[0]=rd.nextInt(45)+1;
		for(int i=1; i<6;i++) {
			int temp = rd.nextInt(45)+1;
			lotto[i]=temp;	
//			결과는 나오지만 필요없는 for문이 돌고 있음
//			for( int j=0; j<i; j++) {
//				if(lotto[j]==temp) {
//					i--;
//				}
//			}			
			for( int j=0; j<i; j++) {
				if(lotto[j]==temp) {
					i--;
					break;
				}
			}						
		}		
		for(int value : lotto) {
			System.out.print("["+value+"]");
		}
		System.out.println();
	}

	public static void main(String[] args) {
//		new Lotto().makeLotto();
		Lotto lo = new Lotto();
		lo.makeLotto();
		lo.makeLotto();
		lo.makeLotto();
		lo.makeLotto();
		lo.makeLotto();
		
	}

}
