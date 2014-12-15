/* 
* @Author: Jeremiah Marks
* @Contact:	Jeremiah@jlmarks.org
* @Date:   2014-04-11 22:44:11
* @Last Modified by:   Jeremiah Marks
* @Last Modified time: 2014-04-12 01:04:38
*
*/


/*
*Question 2:
*Amazon is considering introducing a customer loyalty program, which rewards 
*members with Amazon Dollars on purchases. The program encourages members to be 
*sponsors and recruit other shoppers to join. Purchases made by recruits are 
*then rewarded to the sponsor. The chain of recruits can be arbitrarily deep. 
*Any purchase by a member is counted towards that member (10% of purchase price), 
*their sponsor (4%), their sponsor’s sponsor (4% of 4%), their sponsor’s 
*sponsor’s sponsor (4% of 4% of 4%), etc. Finally, a sponsor can have any number 
*of recruits, but any one recruit can only have one sponsor.Write a function 
*that calculates the payout for a given member.
*
*Given the following interface, please implement the MemberPayoutUtil.calculatePayout function.
*
*public interface Member {
*	public double getMonthlyAmazonDollars();
*    public Collection<Member> getRecruitedMembers(); 
*}
*
********************************************************************************
********************************************************************************
** 
** A quick preface: 
**	It has been a long time since I have used java with any regularity at all. 
**	As in since I complete my java classes, probably 18 months ago. I know I still
**	have the text book (A couple of different versions of it, iirc), and if I 
**	had found it I probably would have been able to do much better at this 
**	question. 
**	After getting back into using it with any regularity I am sure that I can
** 	turn out meaningful code in java quickly, one again. 
**
********************************************************************************
********************************************************************************
**
**	Assumptions:
**
**	the method getMonthlyAmazonDollars returns what the actual user would recieve
**		ie, the 10% number. 
**	To explain my understanding of the math:
**		Assuming that all users spent $100:
**			The primary user would get $10 (their 10 percent) plus $4 for each
**				recruit, plus $0.16 for each recruits recruit, plus $0.0064
**				for each recruits recruits recruit. etc. etc.
**
********************************************************************************
********************************************************************************
**
**	Approach:
**	
**	call calculatePayout method for member of interest(moi).
**	totalpayout= 10% of moi's sales.
**	add to totalpayout the return of calling calculate payupmethod for each recruit, recursively
**	return totalpayout
**
********************************************************************************
*******************************************************************************/


 public interface Member {
     public double getMonthlyAmazonDollars();
     public Collection<Member> getRecruitedMembers(); 
 } 
 public class MemberPayoutUtil implements Member
 {
 	public double calculatePayout()
 	{
 		private double totalPayout=this.getMonthlyAmazonDollars(); /*private because we do not want other processes to be able to affect the total*/
 		private list recruits=this.getRecruitedMembers();		   /*nor do we want them to be able to add amazon users to the calculation*/

 		for (Member thismember : recruits)
 		/* I think that I am doing this right, what I am attempting to do is 
 			iterate through the list of recruits. There are several things that 
 			I may have done incorrectly here because I do not remember enough
 			Java to quickly write a meaningful driver class for this. I am 
 			attempting to implement the iterator found at
 			http://stackoverflow.com/questions/5228687/java-best-way-to-iterate-through-an-collection-here-arraylist
 			*/						  
 		{
 			totalPayout+=thismember.calculatePayup();
 		}
 		return totalPayout;
 	}


 	public double calculatePayup()
 	{
 		private double payup=0.04*this.getMonthlyAmazonDollars();
 		private list recruits=this.getRecruitedMembers();

 		for (Member thismember : recruits)
 		{
 			payup+=thismember.calculatePayup();
 		}


 		return payup;
 	}

 }

