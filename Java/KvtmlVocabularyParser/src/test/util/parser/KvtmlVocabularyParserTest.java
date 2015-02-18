package test.util.parser;

import com.pythonbyte.util.parser.KvtmlVocabularyParser;
import junit.framework.TestCase;
import org.w3c.dom.Document;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.IOException;

public class KvtmlVocabularyParserTest extends TestCase {
    public void testTestGoodFile() {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        try {
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse("german.kvtml");

            KvtmlVocabularyParser parser = new KvtmlVocabularyParser( document );
            assertEquals( 171, parser.getVocabularyEntries().size() );
        } catch (ParserConfigurationException | SAXException | IOException e) {
            e.printStackTrace();
            fail();
        }
    }
}
