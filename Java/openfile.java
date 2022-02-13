import java.io.FileReader;
import java.io.*;

public class openfile {

 public static void main(String[] args) throws IOException {
  String path = "/Users/hongpochen/OneDrive - Nanyang Technological University/VSCODE/CZ3005 Re/G.json";
  FileReader fileReader = new FileReader(path);
  
  System.out.println(readAllCharactersOneByOne(fileReader));

 }
 
 public static String readAllCharactersOneByOne(Reader reader) throws IOException {
     StringBuilder content = new StringBuilder();
     int nextChar;
     while ((nextChar = reader.read()) != -1) {
         content.append((char) nextChar);
     }
     return String.valueOf(content);
 }

}