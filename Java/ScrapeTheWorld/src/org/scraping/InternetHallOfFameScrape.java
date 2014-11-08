package org.scraping;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.util.ArrayList;
import java.util.List;

public class InternetHallOfFameScrape {
    private static String INDUCTEE_PAGE = "http://www.internethalloffame.org/inductees/all";

    public static List<String> getInducteeNames() {
        try {
            List<String> inducteeNames = new ArrayList<String>();

            Document cfiaPageDocument = Jsoup.connect( INDUCTEE_PAGE ).get();
            Elements spanElements = cfiaPageDocument.select( "span[class=field-content]" );

            for ( Element spanElement: spanElements ) {
                Element hrefElement = spanElement.select( "a" ).first();
                if ( hrefElement != null ) {
                    inducteeNames.add( hrefElement.text() );
                }
            }
            return inducteeNames;
        } catch ( Exception e ) {
            e.printStackTrace();
            return new ArrayList<String>();
        }
    }

    public static boolean isNameAnInductee( String fullName ) {
        return getInducteeNames().contains( fullName );
    }
}
