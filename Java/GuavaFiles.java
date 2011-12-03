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
