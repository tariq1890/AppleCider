import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

public class CSVclean {
	
	/**
	 * 
	 * @param listOfMaps
	 */
	public static void specialCSV(ArrayList<LinkedHashMap<Query,ArrayList<String>>> listOfMaps){
		int count2 = 0;
		for(LinkedHashMap<Query,ArrayList<String>> map: listOfMaps){
			
			ArrayList<String> nextURLs = null;
			
			for(Query query: map.keySet()){
				System.out.print(query);
				count2++;
				
				if(nextURLs != null){
					for(String url: nextURLs){
						System.out.print(","+url);
					}	
					if(nextURLs.size() == 0)
						System.out.print(",");
				}
				
				nextURLs = map.get(query);				
				System.out.println();
			}
		}
		System.out.println("count 2: "+count2);
	}//CSV
	
	
	
	
	
	
	public static void main(String[] args) throws FileNotFoundException{
		
		int count = 0;
		
		File file = new File("/Users/leemartie/Desktop/backup_summer_2017/overflow2/untitled folder/moreLikeThisWorkSpace/CSVclean/src/GoogleQueryLog.csv");
		
		LinkedHashMap<Query,ArrayList<String>> map = new LinkedHashMap<Query,ArrayList<String>>();
		
		
		ArrayList<LinkedHashMap<Query,ArrayList<String>>> listOfMaps = new ArrayList<LinkedHashMap<Query,ArrayList<String>>>();
		
		Scanner scan = new Scanner(file);
		
		boolean start = false;
		Query currentQuery = null;
		
		while(scan.hasNext()){//while
			String line = scan.nextLine();		

			//start
			if(start){
					String[] words = line.split(",");
					currentQuery = new Query("NewTask,"+words[0],count);	
					ArrayList<String> urls = new ArrayList<String>();
					for(int i = 1;i<words.length;i++){				
						urls.add(words[i]);//urls
					}//for
					
					map.put(currentQuery, urls);
	
					count++;
				start = false;
				continue;
			}//start
			
			
			//if new task
			if(line.startsWith("NewTask")){
				start = true;
				if(map.size() > 0){
					listOfMaps.add(map);
					map = new LinkedHashMap<Query,ArrayList<String>>();
				}
			}else{
				
				String[] words = line.split(",");
				
				//line with no query
				if(words[0].length() == 0){
					ArrayList<String> urls = map.get(currentQuery);
					//for
					for(int i = 1;i<words.length;i++){
						urls.add(words[i]);
					}
					map.put(currentQuery, urls);
				}else{//line starting with query
					
					start = false;
					currentQuery = new Query(words[0],count);
					count++;
					ArrayList<String> urls = new ArrayList<String>();
					//for
					for(int i = 1;i<words.length;i++){
						urls.add(words[i]);
					}
					map.put(currentQuery, urls);
					
				}
				
				
			}//else

		}//while
		
		specialCSV(listOfMaps);
		System.out.println("count: "+count);
		
		
		
	}

}
