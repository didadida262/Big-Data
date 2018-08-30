package cn2.sxt.game;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.Rectangle;

public class GameObject {
	double x,y;
	int speed;
	Image img;
	int width;
	int height;
	
	public void drawSelf(Graphics g) {
		g.drawImage(img, (int)x, (int)y, null);
	}

	public GameObject(double x, double y, int speed, Image img, int width, int height) {
		super();
		this.x = x;
		this.y = y;
		this.speed = speed;
		this.img = img;
		this.width = width;
		this.height = height;
	}

	public GameObject(double x, double y, Image img) {
		super();
		this.x = x;
		this.y = y;
		this.img = img;
	}
	public GameObject() {
		
	}
	
	/**
	 * 返回物体所在的矩形
	 * @return
	 */
	public Rectangle getRect() {
		return new Rectangle((int)x,(int)y,width,height);
	}
	
}
