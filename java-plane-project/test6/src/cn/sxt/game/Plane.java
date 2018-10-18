package cn.sxt.game;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.KeyEvent;

public class Plane extends GameObject {
	double degree;
	int speed = 3;
	boolean left,right,up,down;
	boolean live =true;
	
	public void drawself(Graphics g) {
	if(live) {
		g.drawImage(img, (int)x,(int) y,null);
		if(left)
			x = x-speed;
		if(right)
			x = x+speed;
		if(up)
			y = y-speed;
		if(down)
			y = y+speed;
	}
	}
	
	public Plane(Image img,double x,double y) {
		this.x = x;
		this.y = y;
		this.img = img;
		this.width = img.getHeight(null);
		this.height = img.getWidth(null);
	}
	
	public void addDirection(KeyEvent e) {
		switch(e.getKeyCode()) {
		case KeyEvent.VK_LEFT:
			left = true;
			break;
		case KeyEvent.VK_RIGHT:
			right = true;
			break;
		case KeyEvent.VK_UP:
			up = true;
			break;
		case KeyEvent.VK_DOWN:
			down = true;
			break;

		}
	}
	
	public void minusDirection(KeyEvent e) {
		switch(e.getKeyCode()) {
		case KeyEvent.VK_LEFT:
			left = false;
			break;
		case KeyEvent.VK_RIGHT:
			right = false;
			break;
		case KeyEvent.VK_UP:
			up = false;
			break;
		case KeyEvent.VK_DOWN:
			down = false;
			break;

		}
	}
}
