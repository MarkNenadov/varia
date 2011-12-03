import com.google.common.base.Stopwatch;

import java.util.concurrent.TimeUnit;

public class GuavaStopwatch {
        public static void main( String args[] ) {
            demonstrateStopwatch();

        }

    private static void demonstrateStopwatch() {
        Stopwatch stopWatch = new Stopwatch();
        System.out.println( "Is stopwatch running? " + stopWatch.isRunning() );

        stopWatch.start();

        for ( int i=0; i<1000; i++ ) {
            System.out.println( "Is stopwatch running? " + stopWatch.isRunning() );
        }

        stopWatch.stop();
        System.out.println( "Our loop took : " + stopWatch.elapsedTime( TimeUnit.MILLISECONDS ) + " milliseconds" );
    }
}
