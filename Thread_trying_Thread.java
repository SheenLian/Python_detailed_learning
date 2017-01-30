package thread;

public class Thread_trying_Thread extends Thread{
	private Thread th;
	private String thname;
	
	public Thread_trying_Thread(String name){
		this.thname = name;
		System.out.println(">Creating " +  this.thname );
	}
	
	public void run(){
		System.out.println(">Running "+ this.thname);
		try{
			for(int i = 1; i<10; i++){
				System.out.println(this.thname+": "+i);
				Thread.sleep(50);
			}
		}catch(InterruptedException e){
			System.out.println("Thread " +  this.thname + " interrupted.");
		}
		System.out.println("Thread " +  this.thname + " exiting.");
	}
	public void start(){
		System.out.println("Starting " +  this.thname );
	      if (th == null) {
	         th = new Thread (this, thname);
	         th.start ();
	      }
	}

}
