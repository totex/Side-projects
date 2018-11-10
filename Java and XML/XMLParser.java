import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;


public class XMLParser {

	public static void main(String[] args) {
		try {
			File inputFile = new File("data/filmek.xml");
			DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
			Document doc = dBuilder.parse(inputFile);
			doc.getDocumentElement().normalize();
			
			System.out.println("Root element is: " + doc.getDocumentElement().getNodeName());
			System.out.println("----------------------------------------------");

			NodeList filmLista = doc.getElementsByTagName("film");
		 	
			for (int temp = 0; temp < filmLista.getLength(); temp++){
			 
				Node nNode = filmLista.item(temp);

				Element eElement = (Element) nNode;
				 
				System.out.println("film id : " + eElement.getAttribute("id"));
				System.out.println("film cim : " + eElement.getElementsByTagName("cim").item(0).getTextContent());
				System.out.println("foszereplo : " + eElement.getElementsByTagName("foszereplo").item(0).getTextContent());
				System.out.println("kiadas eve : " + eElement.getElementsByTagName("ev").item(0).getTextContent());
				System.out.println("----------------------------------------------"); 
			}
		}
		catch (Exception e) {
			e.printStackTrace();
		}
	}
}
