package test.org.scraping;

import junit.framework.TestCase;
import org.scraping.UnitedStatesCBPScrape;

public class UnitedStatesCBPScrapeTest extends TestCase {

    public void testGetNonCommercialBorderWaitTimeByPort() {
        assertTrue( UnitedStatesCBPScrape.getNonCommercialBorderWaitTimeByPort( "380001" ).contains( "min" ) || UnitedStatesCBPScrape.getNonCommercialBorderWaitTimeByPort( "380001" ).contains( "hr" ) );
    }
}
