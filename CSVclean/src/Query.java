
public class Query {

	public String keywords = "";
	public int number;
	
	public Query(String keywords, int num){
		this.keywords = keywords;
		this.number = num;
	}
	
	public boolean equals(Query q){
		return q.number == this.number;
	}
	
	public final int hashCode() {
		return number;
	}
	
	public String toString(){
		return keywords;
	}
	
}
