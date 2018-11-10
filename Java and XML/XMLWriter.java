import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;


public class XMLWriter {
		
	public static void writeXML(String filename){

		try {

			DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
			
			// root - gyoker
			Document doc = docBuilder.newDocument();
			Element vallalat = doc.createElement("vallalat");
			doc.appendChild(vallalat);

			// alkalmazott elem
			Element alkalmazott = doc.createElement("alkalmazott");
			vallalat.appendChild(alkalmazott);

			// alkalmazott attributum
			Attr attr = doc.createAttribute("id");
			attr.setValue("1");
			alkalmazott.setAttributeNode(attr);

			// rividites
			// staff.setAttribute("id", "1");
			
			// vezetek nev elem
			Element vezetek_nev = doc.createElement("vezetek_nev");
			vezetek_nev.appendChild(doc.createTextNode("Kovacs"));
			alkalmazott.appendChild(vezetek_nev);

			// kereszt nev elem
			Element kereszt_nev = doc.createElement("kereszt_nev");
			kereszt_nev.appendChild(doc.createTextNode("Margit"));
			alkalmazott.appendChild(kereszt_nev);

			// becenev elem
			Element becenev = doc.createElement("becenev");
			becenev.appendChild(doc.createTextNode("KoMa"));
			alkalmazott.appendChild(becenev);

			// fizetes elem
			Element fizetes = doc.createElement("fizetes");
			fizetes.appendChild(doc.createTextNode("10,000,000"));
			alkalmazott.appendChild(fizetes);
			
			// writing to XML
			TransformerFactory transformerFactory = TransformerFactory.newInstance();
			Transformer transformer = transformerFactory.newTransformer();
			transformer.setOutputProperty(OutputKeys.INDENT, "yes"); // these two lines are for the pretty printing
			transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4"); // indentation level is 4
			DOMSource source = new DOMSource(doc);
			StreamResult result = new StreamResult(new File("out/" + filename + ".xml"));

			transformer.transform(source, result);

			System.out.println("File saved...");
			
		} catch (ParserConfigurationException pce) {
			pce.printStackTrace();
		} catch (TransformerException tfe) {
			tfe.printStackTrace();
		}
	}
}
