package thread;

public class Thread_trying_Runnable implements Runnable{
	
	private Thread th;
	private String thname;
	public Thread_trying_Runnable(String name){
		this.thname = name;
		System.out.println(">Creating thread: "+ this.thname);
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		System.out.println(">Running thread: "+ this.thname);
		
		try{
			for(int i = 1; i<10 ; i++){
				System.out.println("Thread: "+ this.thname+","+i);
				Thread.sleep(50);
			}
		}catch(InterruptedException e){
			System.out.println("Thread: "+ this.thname+"interrupted");
		}
		System.out.println("Thread: "+ this.thname+"exiting");
	}
	public void start(){
		System.out.println("Starting " +  thname );
	      if (th == null) {
	         th = new Thread (this, thname);
	         th.start ();
	      }
	}

}
