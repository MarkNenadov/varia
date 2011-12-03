/* Demo of Google Guava String class
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

import com.google.common.base.Strings;

public class GuavaStrings {
    public static void main( String[] args )
    {
        demonstrateEmptyToNull();
        demonstrateNullToEmpty();
        demonstrateRepeat();
        demonstratePadEnd();
        demonstratePadStart();
    }

    public static void demonstrateEmptyToNull() {
        String string1 = "Hey you.";
        String string2 = "";

        String string3 = Strings.emptyToNull( string1 );
        System.out.println( "Strings.emptyToNull() called on non-empty string results in the string: " + string3 );

        string3 = Strings.emptyToNull( string2 );
        System.out.println( "Strings.emptyToNull() called on empty string results in null: " + string3 );

    }

    public static void demonstrateNullToEmpty() {
        String string1 = "Hey you.";
        String string2 = null;

        String string3 = Strings.nullToEmpty( string1 );
        System.out.println( "Strings.nullToEmpty() called on non-empty string results in the string: " + string3 );

        string3 = Strings.nullToEmpty( string2 );
        System.out.println( "Strings.nullToEmpty() called on null results in emptyString: " + string3 );

    }

    public static void demonstrateRepeat() {
        String sequence = "123";

        System.out.println( sequence + " repeated with Strings.repeat() ten times is: "  + Strings.repeat( sequence, 10 ) );
    }

    public static void demonstratePadEnd() {
        String message = "Alex went to sleep";
        Character padChar = '.';

        System.out.println( "Our string padded with Strings.padEnd() to 25 characters is: " + Strings.padEnd( message, 25, padChar ) );
    }

    public static void demonstratePadStart() {
        String message = "Alex went to sleep";
        Character padChar = '.';

        System.out.println( "Our string padded with Strings.padStart() to 25 characters is: " + Strings.padStart( message, 25, padChar ) );
    }

}