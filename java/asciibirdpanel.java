/*
* @Author: Jeremiah Marks
* @Date:   2014-04-15 21:38:39
* @Last Modified by:   jlmarks
* @Last Modified time: 2014-04-21 19:50:28
*/

/*
################################################################################
################################################################################
##
##	shortened instructions:
##	
## The board will be 10 rows high by 20 columns.
##
## delta x = 2 columns per row
## delta y = input of 0-4 (0=-2)
## do not allow bird to raise above top column
## if bird avoids obsticle then point +=1
##
################################################################################
################################################################################
##
##	approach: use a Jlabel to hold the game board.
## first jlabel will only be bird with empty sky
##	every third turn add a obsticle
##		obsticles alternate between from above or below
##		obsticles can have random height 1<=height<=40% of total height

##
################################################################################
################################################################################
##
## Approach:
	the loop:

	playfield(nextY)
	thisY=nextY
	if thisY<=2
		nextY=0
	else
		nextY=thisY-1
	wait{
		if button pressed:
			flap();
		}
	end loop






	FLAP()
		{
			if nextY-thisY<2
			{
				if nextY<topofmap
				{
					nextY+=1
				}
			}
		}
	}
##
################################################################################
################################################################################
##
## New Approach

## Currently the thisY and nextY values are not changing at all. 



*/


import javax.swing.JPanel;
import javax.swing.JLabel;
import java.awt.*;
import java.awt.event.*;
import javax.swing.Timer;

public class asciibirdpanel extends JPanel{
	private final int WIDTH=300, HEIGHT=300;
	private final int PLAYWIDTH=20, PLAYHEIGHT=10;
	private int thisY=PLAYHEIGHT/2;
	private int nextY=thisY-2;
	private int delay=1000;
	private String playField = new String();
	protected Timer timer;
	JLabel fieldLabel, testLabel, tylabel, nylabel;
	private int x=0;

	public asciibirdpanel(){

		MyKeyListener listener = new MyKeyListener();
		MyTimerListener looper = new MyTimerListener();
		/*theASCIIBird gamebird = new theASCIIBird();*/
		addKeyListener(listener);
		setFocusable(true);
		setPreferredSize(new Dimension(WIDTH, HEIGHT));
		timer = new Timer(delay, looper);
		setBackground(Color.black);
		playField=StringGen(thisY);
		fieldLabel = new JLabel(playField);
		testLabel = new JLabel(Integer.toString(x));
		tylabel = new JLabel("TY " + Integer.toString(thisY));
		nylabel = new JLabel("NY " + Integer.toString(nextY));
		add(fieldLabel);
		add(testLabel);
		add(nylabel);
		add(tylabel);
		timer.start();



		

	}



	private String StringGen( int birdYPos){
		
		String toReturn = new String("<html><tt>");
		for (int i=PLAYHEIGHT; i>0; i--){
			if (birdYPos==i){
				toReturn+="@";
			} else{
				toReturn+="*";
			}
			for (int j=1; j<PLAYWIDTH; j++){
				toReturn+="*";
			}
			toReturn+="<br>";

		}
		toReturn+="</tt></html>";
		return toReturn;


	}

	private void nextLoop(){
		x+=1;
		playField=new String(StringGen(nextY));
		fieldLabel.setText(playField);
		testLabel.setText(Integer.toString(x));
		thisY=nextY;

		if (thisY<=3){
			nextY=1;
		} else{
			nextY = thisY - 2;
		}
		tylabel.setText("This Y position: " + Integer.toString(thisY));
		nylabel.setText("Next Y position: " + Integer.toString(nextY));		
	}
	private void flap(){
		if (nextY-thisY<2){
			if (nextY<PLAYHEIGHT){
				nextY+=1;
			}
		}
		tylabel.setText("This Y position: " + Integer.toString(thisY));
		nylabel.setText("Next Y position: " + Integer.toString(nextY));
	}

	private class MyTimerListener implements ActionListener{
		public void actionPerformed(ActionEvent e){
			nextLoop();
		}
	}


	private class MyKeyListener implements KeyListener{
		public void keyPressed(KeyEvent e){
			flap();
		}
		public void keyReleased(KeyEvent e){
			/*flap();*/
		}
		public void keyTyped(KeyEvent e){
			/*flap();*/
		}
	}
}