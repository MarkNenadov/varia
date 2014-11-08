package test.org.scraping;

import junit.framework.TestCase;
import org.scraping.InternetHallOfFameScrape;

import java.util.List;

public class InternetHallOfFameScrapeTest extends TestCase {

    public void testGetInducteeNames() {
        List<String> inducteeNames = InternetHallOfFameScrape.getInducteeNames();
        assertNotNull( inducteeNames );
        assertTrue( inducteeNames.size() > 0 );
    }

    public void testIsNameAnInductee() {
        assertFalse( InternetHallOfFameScrape.isNameAnInductee( "Mark Nenadov" ) );
        assertTrue( InternetHallOfFameScrape.isNameAnInductee( "Philip Zimmerman" ) );
    }

}
