/* Demo of the Java Excel API (jxl library)
 * 
 * Requires junit and the jxl jar from: http://jexcelapi.sourceforge.net/
 *
 * Mark J. Nenadov (2013)
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



import junit.framework.TestCase;
import jxl.Sheet;
import jxl.Workbook;
import jxl.WorkbookSettings;
import jxl.write.Label;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;

import java.io.File;
import java.util.Locale;

public class JxlDemo extends TestCase {
    File excelFile = new File( "c:\\java\\test.xls" );

    public void testWriteExcelDocument() {
        WorkbookSettings wbSettings = new WorkbookSettings();
        wbSettings.setLocale( new Locale( "en", "EN" ) );
        try {
            WritableWorkbook workbook = Workbook.createWorkbook( excelFile, wbSettings );

            workbook.createSheet( "Test Sheet #1", 0 );
            workbook.createSheet( "Test Sheet #2", 1 );

            WritableSheet currentSheet = workbook.getSheet( 0 );
            currentSheet.addCell( new Label( 0, 0, "Dog" ) );
            currentSheet.addCell( new Label( 1, 0, "Cat" ) );
            currentSheet.addCell( new Label( 2, 0, "Hen" ) );

            currentSheet = workbook.getSheet( 1 );
            currentSheet.addCell( new Label( 0, 0, "Java" ) );
            currentSheet.addCell( new Label( 1, 0, "C" ) );
            currentSheet.addCell( new Label( 2, 0, "C++" ) );
            currentSheet.addCell( new Label( 0, 1, "Linux" ) );
            currentSheet.addCell( new Label( 1, 1, "Windows" ) );
            currentSheet.addCell( new Label( 2, 1, "BSD" ) );

            workbook.write();
            workbook.close();

        } catch ( Exception e ) {
            e.printStackTrace();
        }
    }

    public void testReadExcelDocument() {
        try {
            Workbook workbook = Workbook.getWorkbook( excelFile );
            Sheet sheet = workbook.getSheet( 0 );
            System.out.println( "The first cell of the first row on sheet 1 has: " + sheet.getCell( 0, 0 ).getContents() );
        } catch ( Exception e ) {
            e.printStackTrace();
        }
    }

}

