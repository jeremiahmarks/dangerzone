// Bouncing Ball example

import java.awt.event.*;
import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.Timer;

public class Ball
{
   // execute application
   public static void main( String args[] )
   {
      JFrame frame = new JFrame( "Bouncing Ball" );
      frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );

      BallPanel bp = new BallPanel(); 
      frame.add( bp );
      frame.setSize( 300, 300 ); // set frame size
      frame.setVisible( true ); // display frame
   } // end main
}


// class BallPanel

class BallPanel extends JPanel implements ActionListener
{
   private int delay = 100;
   protected Timer timer;

   private int x = 0;		// x position
   private int y = 0;		// y position
   private int radius = 15;	// ball radius

   private int dx = 2;		// increment amount (x coord)
   private int dy = 2;		// increment amount (y coord)

   public BallPanel()
   {
      timer = new Timer(delay, this);
	timer.start();		// start the timer
   }

   public void actionPerformed(ActionEvent e)
   // will run when the timer fires
   {
	repaint();
   }

   // draw rectangles and arcs
   public void paintComponent( Graphics g )
   {
      super.paintComponent( g ); // call superclass's paintComponent 
	g.setColor(Color.red);

	// check for boundaries
	if (x < radius)			dx = Math.abs(dx);
	if (x > getWidth() - radius)	dx = -Math.abs(dx);
	if (y < radius)			dy = Math.abs(dy);
	if (y > getHeight() - radius)	dy = -Math.abs(dy);

	// adjust ball position
	x += dx;
	y += dy;
	g.fillOval(x - radius, y - radius, radius*2, radius*2);
   }

}
