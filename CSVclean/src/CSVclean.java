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
	public static void specialCSV(ArrayList<LinkedHashMap<String,ArrayList<String>>> listOfMaps){
		
		for(LinkedHashMap<String,ArrayList<String>> map: listOfMaps){
			
			ArrayList<String> nextURLs = null;
			
			for(String query: map.keySet()){
				System.out.print(query);
				
				
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
	}//CSV
	
	
	
	
	public static void main(String[] args) throws FileNotFoundException{
		
		File file = new File("/Users/leemartie/Desktop/backup_summer_2017/overflow2/untitled folder/moreLikeThisWorkSpace/CSVclean/src/GoogleQueryLog.csv");
		
		LinkedHashMap<String,ArrayList<String>> map = new LinkedHashMap<String,ArrayList<String>>();
		
		
		ArrayList<LinkedHashMap<String,ArrayList<String>>> listOfMaps = new ArrayList<LinkedHashMap<String,ArrayList<String>>>();
		
		Scanner scan = new Scanner(file);
		
		boolean start = false;
		String currentQuery = "";
		
		while(scan.hasNext()){//while
			String line = scan.nextLine();		

			//start
			if(start){
					String[] words = line.split(",");
					currentQuery = "NewTask,"+words[0];	
					ArrayList<String> urls = new ArrayList<String>();
					for(int i = 1;i<words.length;i++){				
						urls.add(words[i]);//urls
					}//for
					
					map.put(currentQuery, urls);
	
				start = false;
				continue;
			}//start
			
			
			//if new task
			if(line.startsWith("NewTask")){
				start = true;
				if(map.size() > 0){
					listOfMaps.add(map);
					map = new LinkedHashMap<String,ArrayList<String>>();
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
					currentQuery = words[0];
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
		
		
		
	}

}
