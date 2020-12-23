import java.io.*;
import java.util.Arrays;
public class gk1 {
	public static void main(String args[])throws IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t=Integer.parseInt(br.readLine());
		int op[]=new int[t];
		int q=0;
		int tt=t;
		while(t!=0) {
			int c=0;
			boolean flag=false;
			String  lines = br.readLine();    
			int[] a=new int[2];
			String[] strs = lines.trim().split("\\s+");
			for (int i = 0; i < strs.length; i++)
			{
				a[i] = Integer.parseInt(strs[i]);
			}
			String  lines2 = br.readLine();    
			int[] a2=new int[a[0]];
			String[] strs2 = lines2.trim().split("\\s+");
			for (int i = 0; i < strs2.length; i++)
			{
				a2[i] = Integer.parseInt(strs2[i]);
			}
			for(int i=0;i<=a[0]-a[1];i++)
			{
				if(a2[i]==a[1])
				{	int x=i+1;
				for(int y=a[1]-1;y>0;y--)
				{
					if(a2[x]==y)
					{
						flag=false;
						x++;
					}
					else
					{
						flag=true;
						break;
					}
				}
				if(flag==false)
				c++;
				}
			}
			op[q]=c;
			q++;
			t--;
		}
		for(int i=0;i<tt;i++)
		{
			System.out.println("Case #"+(i+1)+": "+ op[i]);
		}
	}
}
