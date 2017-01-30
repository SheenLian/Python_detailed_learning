package thread;

public class Test_Thread {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread_trying_Runnable T1 = new Thread_trying_Runnable("Sheen");
		Thread_trying_Runnable T2 = new Thread_trying_Runnable("Lily");
		T1.start();
		T2.start();
		
		Thread_trying_Thread T3 = new Thread_trying_Thread("sheen");
		Thread_trying_Thread T4 = new Thread_trying_Thread("lily");
		T3.start();
		T4.start();

	}

}
