public class tester
{
    
    public static void main(String[] args)
    {
            int year=2011;
            int month=10;
            int day=13;
            int hour=14;
            int min=22;
            String awesomename="applejack";
        ToDoItem apple=new ToDoItem(awesomename,year, month, day, hour, min);
        System.out.println(apple);
    }
}
