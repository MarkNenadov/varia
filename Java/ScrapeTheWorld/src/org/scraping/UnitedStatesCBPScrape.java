package org.scraping;

import it.sauronsoftware.feed4j.FeedParser;
import it.sauronsoftware.feed4j.bean.Feed;

import java.net.URL;

public class UnitedStatesCBPScrape {
    public static String getNonCommercialBorderWaitTimeByPort( String port ) {
        String feedUrl = "http://apps.cbp.gov/bwt/customize_rss.asp?portList=" + port + "&lane=pov&action=rss&f=csv";
        String description = "Unknown";

        try {
            Feed feed = FeedParser.parse( new URL( feedUrl ) );
            description = feed.getItem( 0 ).getDescriptionAsText();
            description = description.split( ", " )[1];
            description = description.split( " " )[0] + " " + description.split( " " )[1];
        } catch ( Exception e ) {
            e.printStackTrace();
        }
        return description;
    }
}
