/* Gadhnami - Determines whether a particular name is
 * a variation of the Libyan leader Gadaffi's name.
 * 
 * A special thanks goes out to Czechnology who posted the
 * regular expression utilized here to Stack Overflow in 
 * the interesting "Regular expression to search for 
 * Gadaffi" post.
 *
 * AUTHOR
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

package gadhnami;

import java.util.regex.*;

public class Gadhnami {
	static String gadaffi_regex = "\\b[KGQ]h?add?h?af?fi\\b";
	
	public static boolean isThisNameGadaffi(String name)
	{
		Pattern p = Pattern.compile(gadaffi_regex);
		Matcher m = p.matcher(name);
		
		return m.find();
	}
	
	public static void main(String[] args) {
		System.out.println(isThisNameGadaffi("Gadaffi"));
	}
}
