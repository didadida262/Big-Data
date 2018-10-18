package cn.sxt.game;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.Rectangle;

public class GameObject {
	double x,y;
	int width,height;
	int speed;
	Image img;
	
	public void drawself(Graphics g) {
		g.drawImage(img,(int) x,(int) y,null);
	}
	
	public GameObject(Image img,double x,double y,int width,int height,int speed) {
		this.img = img;
		this.speed = speed;
		this.width = width;
		this.height = height;
		this.x = x;
		this.y = y;
	}
	
	public GameObject(Image img,double x,double y) {
		this.img = img;
		this.x = x;
		this.y =y;
	}
	
	public GameObject() {
		
	}
	
	public Rectangle getRect() {
		return new Rectangle((int)x,(int)y,width,height);
	}
	
	
}