package cn.sxt.game;

import java.awt.Color;
import java.awt.Graphics;


public class Shell extends GameObject{
	double degree;
	public Shell() {
		x= 200;
		y= 200;
		width = 10;
		height =10;
		speed = 2;
		degree = Math.PI*2*Math.random();
	}
	
	public void draw(Graphics g) {
		Color c =g.getColor();
		g.setColor(Color.YELLOW);
		g.fillOval((int)x, (int)y, width, height);
		x = x + speed*Math.cos(degree);
		y= y + speed*Math.sin(degree);
		
		if(x<0||x>Constant.GAME_WIDTH)
			degree = 2*Math.PI -degree;
		if(y<0||y>Constant.GAME_HEIGHT)
			degree = -degree;
		g.setColor(c);
	}
}
