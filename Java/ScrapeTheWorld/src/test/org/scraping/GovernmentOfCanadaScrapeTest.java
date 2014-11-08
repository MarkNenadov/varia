package test.org.scraping;

import junit.framework.TestCase;
import org.scraping.GovernmentOfCanadaScrape;
import org.scraping.InternetHallOfFameScrape;

import java.util.List;

public class GovernmentOfCanadaScrapeTest extends TestCase {

    public void testGetCommercialBorderWaitTimeByLocationName() {
        assertTrue( GovernmentOfCanadaScrape.getCommercialBorderWaitTimeByLocationName( "Ambassador Bridge" ).contains( "minute" ) || GovernmentOfCanadaScrape.getCommercialBorderWaitTimeByLocationName( "Ambassador Bridge" ).contains( "hour" ) );
    }

    public void testGetNonCommercialBorderWaitTimeByLocationName() {
        assertTrue( GovernmentOfCanadaScrape.getNonCommercialBorderWaitTimeByLocationName( "Ambassador Bridge" ).contains( "minute" ) || GovernmentOfCanadaScrape.getNonCommercialBorderWaitTimeByLocationName( "Ambassador Bridge" ).contains( "hour" ) );
    }

}
