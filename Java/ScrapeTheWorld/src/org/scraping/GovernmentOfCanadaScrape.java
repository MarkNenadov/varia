package org.scraping;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.util.ArrayList;
import java.util.List;

public class GovernmentOfCanadaScrape {
    private static String BORDER_WAIT_TIMES_PAGE = "http://www.cbsa-asfc.gc.ca/bwt-taf/menu-eng.html";

    public static String getNonCommercialBorderWaitTimeByLocationName( String locationName ) {
        try {
            Document borderWaitTimePageDocument = Jsoup.connect( BORDER_WAIT_TIMES_PAGE ).get();
            Element borderWaitTimeTable = borderWaitTimePageDocument.select( "table[class=bwt]" ).first();

            Elements borderWaitTimeTableRows = borderWaitTimeTable.select( "tr" );

            for ( Element rowElement: borderWaitTimeTableRows ) {
                if ( rowElement.select( "td[headers=Office]" ).first() != null ) {
                    Element officeTdBold = rowElement.select( "td[headers=Office]" ).first().select( "b" ).first();

                    if ( officeTdBold.text().equals( locationName ) ) {
                        return rowElement.select( "td[headers=Trav TravCanada]" ).first().text();
                    }
                }
            }
        } catch ( Exception e ) {
            e.printStackTrace();
        }
        return "Unknown";
    }

    public static String getCommercialBorderWaitTimeByLocationName( String locationName ) {
        try {
            Document borderWaitTimePageDocument = Jsoup.connect( BORDER_WAIT_TIMES_PAGE ).get();
            Element borderWaitTimeTable = borderWaitTimePageDocument.select( "table[class=bwt]" ).first();

            Elements borderWaitTimeTableRows = borderWaitTimeTable.select( "tr" );

            for ( Element rowElement: borderWaitTimeTableRows ) {
                if ( rowElement.select( "td[headers=Office]" ).first() != null ) {
                    Element officeTdBold = rowElement.select( "td[headers=Office]" ).first().select( "b" ).first();

                    if ( officeTdBold.text().equals( locationName ) ) {
                        return rowElement.select( "td[headers=Com ComCanada]" ).first().text();
                    }
                }
            }
        } catch ( Exception e ) {
            e.printStackTrace();
        }
        return "Unknown";
    }

}
