/* Demo of Google Guava Files class
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

import com.google.common.io.Files;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;

public class GuavaFiles {

    public static void main( String args[] ) {
        File srcFile = new File( "c:/SumOS.txt" );

        demonstrateCopy( srcFile );
        demonstrateEqual( srcFile );
        demonstrateAppend( srcFile );
    }

    private static void demonstrateCopy( File srcFile ) {
        try {
            Files.copy( srcFile, new File( "c:/users/mark/file2.txt" ) );
            System.out.println( "Just copied a file..." );
        }
        catch ( IOException e ) {
            System.out.println( "Exception occurred [" + e.getMessage() + "]");
        }
    }

    private static void demonstrateEqual( File srcFile ) {
        try {
            System.out.println( "The source file we copied is equal to the destination , so this should be true: " + Files.equal( srcFile, new File( "c:/users/mark/SumOS2.txt" ) ) );
        }
        catch ( IOException e ) {
            System.out.println( "Exception occurred [" + e.getMessage() + "]");
        }
    }

    private static void demonstrateAppend( File srcFile ) {
        try {
            Files.append( "test123", new File( "c:/users/mark/file2.txt"), Charset.defaultCharset() );
            System.out.println( "Now that we appended text to the destination file, the equal() check should be false: " + Files.equal( srcFile, new File( "c:/users/mark/file2.txt" ) ) );
        }
        catch ( IOException e ) {
            System.out.println( "Exception occurred [" + e.getMessage() + "]");
        }
    }
}
