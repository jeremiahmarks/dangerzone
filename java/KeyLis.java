    /* 
    * @Author: Jeremiah Marks
    * @Date:   2014-04-17 17:57:41
    * @Last Modified by:   Jeremiah Marks
    * @Last Modified time: 2014-04-17 20:53:49
    */
    
    import javax.swing.JFrame;
    import javax.swing.JPanel;
    import javax.swing.JLabel;
    import java.awt.*;
    import java.awt.event.*;
    
    public class KeyLis{
	    public static void main(String[] args){
		    JFrame frame=new JFrame("Test Frame");
	        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    
	        frame.getContentPane().add(new KeyTestPanel());
    
	        frame.pack();
	        frame.setVisible(true);

        	    
    
        }
    
    }
    
    class KeyTestPanel extends JPanel{
	    JLabel testLabel;
	    private final int WIDTH=300, HEIGHT=300;
	    private int x=0;
    
	    public KeyTestPanel(){
    		
		    MyKeyListener listener = new MyKeyListener();
		    addKeyListener(listener);
		    setPreferredSize(new Dimension(WIDTH, HEIGHT));
		    setFocusable(true);
		    /*requestFocus();*/
    
		    testLabel = new JLabel("No Key pressed yet");
		    add(testLabel);
		    testLabel.requestFocus();
	    }
    
	    private void TestUpdate(){
		    testLabel.setText("Updated " + Integer.toString(x));
		    x+=1;
	    }
    
	    private class MyKeyListener implements KeyListener{
		    public void keyPressed(KeyEvent e){
			    TestUpdate();
		    }
		    public void keyReleased(KeyEvent e){
			    /*flap();*/
		    }
		    public void keyTyped(KeyEvent e){
			    /*flap();*/
		    }
	    }
    
    }