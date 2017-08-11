import java.io.*;
import java.util.*;

public class Splitter {
	private int counter;

	public Splitter() {
		this.counter = 1;
	}

	public void splitFileByNewTask(String fileName) {
		List<String> taskLines = new ArrayList<>();

		try(BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(fileName)))) {
			for(String line; (line = br.readLine()) != null; ) {
				if(line.startsWith("NewTask")) {
					if(taskLines.size() > 0) {
						this.writeListToFile(taskLines);
					}

					taskLines = new ArrayList<>();
					taskLines.add(line);
				} else {
					taskLines.add(line);
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public void writeListToFile(List<String> list) {
		try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("./splits/" + counter + ".csv", true)))) {
			for(String line : list) {
				bw.write(line + "\n");
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

		this.counter++;
	}

	public static void main(String[] args) {
		Splitter obj = new Splitter();
		obj.splitFileByNewTask("./SpecialGoogleFinalv2.csv");
	}
}