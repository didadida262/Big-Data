package cn2.sxt.game;

import javax.swing.JFrame;
import java.awt.Image;
import java.awt.Color;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Date;

public class MyGameFrame extends Frame {
	/**
	 * 线程刷新
	 * @author didadida262
	 *
	 */
	class PaintThread extends Thread{
		public void run() {
			while(true) {
				//System.out.println("窗口打印一次");
				repaint();
				try {
					Thread.sleep(40);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
	}
	
	/**
	 * 按键更改
	 * @author didadida262
	 *
	 */
	class KeyMonitor extends KeyAdapter{

		@Override
		public void keyPressed(KeyEvent e) {
			plane.addDirection(e);
		}

		@Override
		public void keyReleased(KeyEvent e) {
			plane.minusDirection(e);
		}
		
	}
	
	Image bg = GameUtil.getImage("images/bg.png");
	Image planeImg = GameUtil.getImage("images/plane.png");
	Plane plane = new Plane(planeImg,250,250);
	Explode bao;
	Shell[] shells = new Shell[50];
	Date startTime = new Date();
	Date endTime;
	float period;

	
	public void paint(Graphics g) {
		super.paint(g);
		g.drawImage(bg, 0, 0, null);
		plane.drawSelf(g);
		
		for(int i=0;i<shells.length;i++) {
			shells[i].draw(g);
			boolean peng = shells[i].getRect().intersects(plane.getRect());
			if(peng) {
				plane.live = false;
				
				if(bao == null) {
					bao = new Explode(plane.x,plane.y);
					endTime = new Date();
					period = ((endTime.getTime()-startTime.getTime())/1000);
				}
				bao.draw(g);
			
			}
			
			if(!plane.live) {
				g.setColor(Color.red);
				g.drawString("时间：" + period + '秒', (int)plane.x, (int)plane.y);
				
			}
			
		}
		
	}
	
	public void launchFrame(){
		
		this.setTitle("打飞机");
		this.setVisible(true);
		this.setSize(Constant.GAME_WIDTH, Constant.GAME_HEIGHT);
		this.setLocation(300, 300);
		this.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});
		new PaintThread().start();
		addKeyListener(new KeyMonitor());
		
		/*
		 * 初始化50个炮弹
		 */
		for(int i = 0;i<shells.length;i++) {
			shells[i] = new Shell();
		}
	}
	
	public static void main(String[] args){
		MyGameFrame f = new MyGameFrame();
		
		f.launchFrame();
	}
	//用双缓存解决抖动
	private Image offScreenImage = null;
	 
	public void update(Graphics g) {
	    if(offScreenImage == null)
	        offScreenImage = this.createImage(Constant.GAME_WIDTH,Constant.GAME_HEIGHT);//这是游戏窗口的宽度和高度
	     
	    Graphics gOff = offScreenImage.getGraphics();
	    paint(gOff);
	    g.drawImage(offScreenImage, 0, 0, null);
	}  
	
}
