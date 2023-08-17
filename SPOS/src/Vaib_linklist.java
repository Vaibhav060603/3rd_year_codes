import java.util.Scanner;

class node
{

		
	int data;
	node next;
	
	node()
	{
		this.data=-1;
		this.next=null;
	}
	
	node(int data)
	{
		this.data=data;
		this.next=null;
	}
}


class linklist extends node
{
	node head = new node();
	node tail = head;
	
	void ask()
	{
		System.out.println("Enter the data :\n");
		
	}
	
	void create(int data)
	{
		tail.data=data;
		System.out.println("First node created.");
		
	}
	
	void insert(int data)
	{
		
		if(tail==null)
		{
			tail.data=data;
			System.out.println("First node created.");
		}
		
		else
		{
			node temp=new node(data);
			
			tail.next=temp;
			tail=temp;
			System.out.println("New node created.");
		}
		
	}
	
	void delete(int ele)
	{
		node temp=head;
		node prev=head;
		
		if(head.data==ele)
		{
			if(head.next==null)
			{
				head.data=-1;
				System.out.println("First node deleted, no further nodes present.");
			}
			
			else
			{
				
				head=head.next;
				temp.next=null;
				System.out.println("First node deleted.");
			}
		}
		else
		{
			temp=head.next;
			while(temp.data!=ele)
			{
				temp=temp.next;
				prev=prev.next;
			}
			
			if(temp.data==ele)
			{
				prev.next=temp.next;
				temp.next=null;
			}
			
		}
	}
	
	
	void display()
	{
		node temp = head.next;
		while(temp.next!= null)
		{
			System.out.println(temp.data);
			temp=temp.next;
		}
		System.out.println(temp.data);
	}
	
	
	
	
}

public class Vaib_link 
{
public static void main(String [] args)
{

	Scanner sc = new Scanner(System.in);
	linklist l=new linklist();
	
	while(true)
	{
		
		System.out.println("---------------------------------------------Enter the operation you want to perform---------------------------------" );
		System.out.println("\n1. Create \n2.Insert \n3. Display \n4. Delete \n5. Exit");
		int option=sc.nextInt();
		
		switch(option)
		{
		case 1:
		{
			l.ask();
			int value=sc.nextInt();
			l.create(value);
			break;
		}
		
		case 2:
		{
			l.ask();
			int value=sc.nextInt();
			l.insert(value);
			break;
		}
		
		case 3:
		{
			l.display();			
			break;
		}
		
		case 4:
		{
			l.ask();
			int value=sc.nextInt();
			l.delete(value);
			break;
		}
		
		case 5:
		{
			break;
			
		}
		
		}	
	}
}	
}