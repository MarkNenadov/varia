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