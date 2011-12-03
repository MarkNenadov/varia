/* Demo of Google Guava Stopwatch class
 *
 * Mark J. Nenadov (2011)
 * Essex, Ontario
 * Email: <marknenadov@gmail.com>
 *
 * LICENSING
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version
 *
 * This program is distributed in the hope that it will be useful
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>. 
 *
 */

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
