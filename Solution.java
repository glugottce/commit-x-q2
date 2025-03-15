import java.util.*;

public class Solution {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        int N=n/3;
        List<Integer>l=new ArrayList<>();
        HashMap<Integer,Integer>hm=new HashMap<>();
        for(int i=0;i<n;i++)
        {
            if(hm.containsKey(arr[i]))
            {
                hm.put(arr[i],hm.get(arr[i])+1);
            }
            else
            {
                hm.put(arr[i],1);
            }
        }
        for(int i:hm.keySet())
        {
            if(hm.get(i)>N)
              l.add(i);
        }
        if(l.isEmpty())
        {
            System.out.print("-1");
        }
        else{
            for(int i=0;i<l.size();i++)
            {
                System.out.print(l.get(i)+" ");
            }
        }
    }

}

